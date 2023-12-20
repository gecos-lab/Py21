from pydfnworks import *
import os
import pyvista as pv
import numpy as np
from slices import slice_frac_net

x_dim = 135
y_dim = 100
z_dim = 15

points = np.array([[-x_dim/2, -y_dim/2, z_dim/2],
                   [-x_dim/2, y_dim/2, z_dim/2],
                   [x_dim/2, y_dim/2, z_dim/2],
                   [x_dim/2, -y_dim/2, z_dim/2],
                   [-x_dim / 2, -y_dim / 2, -z_dim / 2],
                   [-x_dim / 2, y_dim / 2, -z_dim / 2],
                   [x_dim / 2, y_dim / 2, -z_dim / 2],
                   [x_dim / 2, -y_dim / 2, -z_dim / 2]
                   ])

bounding_box = pv.PolyData(points, lines=[5, 0, 3, 2, 1, 0,
                                          5, 0, 4, 7, 3, 0,
                                          5, 4, 7, 6, 5, 4,
                                          5, 3, 7, 6, 2, 3,
                                          5, 2, 6, 5, 1, 2,
                                          5, 1, 5, 4, 0, 1])

log_mean = 17.05
log_std = 33.87

var_normal = np.log((log_std**2/(log_mean**2))+1)

m_normal = np.log(log_mean)-var_normal/2

std_normal = np.sqrt(var_normal)

jobname = os.getcwd() + "/dfnworks_tests/output"

DFN = DFNWORKS(jobname,
               ncpu=8)

DFN.params['domainSize']['value'] = [x_dim, y_dim, z_dim]
DFN.params['h']['value'] = 0.15
DFN.params['stopCondition']['value'] = 1
DFN.params['nPoly']['value'] = 10
DFN.params['outputFinalRadiiPerFamily']['value'] = True
DFN.params['outputAcceptedRadiiPerFamily']['value'] = True
DFN.params['forceLargeFractures']['value'] = True
DFN.params['domainSizeIncrease']['value'] = [5, 5, 5]
DFN.params['ignoreBoundaryFaces']['value'] = True
DFN.params['keepIsolatedFractures']['value'] = True
DFN.params['visualizationMode']['value'] = True
DFN.params['boundaryFaces']['value'] = [0, 0, 0, 0, 1, 1]
DFN.params['rejectsPerFracture']['value'] = 350
DFN.params['seed']['value'] = 0
DFN.params['orientationOption']['value'] = 2


# The strike angle is calculated counterclockwise with 0 at Est (0 = E, 90 = N, 180 = W, 270 = S).
# To calculate the correct value from geological dip and dir we subtract from 360 the dip_dir and add 180.

dip_dir = 348
dip = 69
strike_corrected = ((360-dip_dir)+180) % 360

DFN.add_fracture_family(shape="rect",
                        distribution="log_normal",
                        kappa=36.77,
                        probability=.5,
                        aspect=1.0,
                        beta_distribution=0,
                        dip=dip,
                        strike=strike_corrected,
                        log_mean = m_normal,
                        log_std = std_normal,
                        min_radius=2.0,
                        max_radius=20.0,
                        p32=0.43)

# DFN.add_fracture_family(shape="rect",
#                         distribution="log_normal",
#                         kappa=32.0,
#                         probability=.5,
#                         aspect=1.0,
#                         beta_distribution=1,
#                         beta=0.0,
#                         theta=1.42,
#                         phi=26.81,
#                         log_mean=2.08,
#                         log_std=.06,
#                         min_radius=2.0,
#                         max_radius=20.0,
#                         p32=0.22)

DFN.print_family_information(1)

DFN.make_working_directory(delete=True)

DFN.check_input()

DFN.create_network()
# DFN.output_report()
DFN.mesh_network(coarse_factor=10)
DFN.inp_file = 'reduced_mesh.inp'

DFN.inp2vtk_python()

mesh = pv.read(jobname+"/reduced_mesh.vtk")
mesh.cell_data['Fracture number'] = np.arange(0, mesh.number_of_cells)
mesh.save('final_mesh.vtk')

slices, grids = slice_frac_net(mesh, n_slices=3, grid_cell_xdim=20, grid_cell_ydim=20)

for grid in grids:
    print(np.mean(grid.cell_data['p21']))

plotter = pv.Plotter()
plotter.add_camera_orientation_widget()
plotter.add_mesh(slices, line_width=2, color='white')
plotter.add_mesh(grids, scalars='p21', line_width=2, cmap='rainbow')
plotter.add_mesh(bounding_box, color='k', line_width=2, name='bounding_box')
plotter.background_color = 'gray'

plotter.show()
