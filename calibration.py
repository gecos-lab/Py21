from fab_parser import fab_parser
from fab2vtk import fab2vtk
from slices import slice_frac_net
import pyvista as pv
import numpy as np

# path = 'data/test_DFN.fab'
#
# data_list, line_fracture_index, vertex_list = fab_parser(path)
#
# frac_net = fab2vtk(data_list, line_fracture_index, vertex_list)

mesh = pv.read("dfnworks_tests/output/final_mesh.vtk")

slices, grids = slice_frac_net(mesh, n_slices=3, grid_cell_xdim=40, grid_cell_ydim=40)

for grid in grids:
    print(np.mean(grid.cell_data['p21']))

plotter = pv.Plotter()
# plotter.show_grid()
plotter.add_camera_orientation_widget()
# plotter.add_mesh(fracture_net, render_points_as_spheres=True)
# plotter.add_mesh(slices, line_width=2, color='white')
plotter.add_mesh(grids, scalars='p21', line_width=2, cmap='rainbow')

# plotter.add_mesh_slice(pv_points, assign_to_axis='z', color='k')
plotter.show()

