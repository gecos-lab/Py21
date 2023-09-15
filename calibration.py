from fab_parser import fab_parser
from fab2vtk import fab2vtk
from slices import slice_frac_net
import pyvista as pv

path = 'data/test_DFN.fab'

data_list, line_fracture_index, vertex_list = fab_parser(path)

frac_net = fab2vtk(data_list, line_fracture_index, vertex_list)

slices, grids = slice_frac_net(frac_net, n_slices=3, grid_cell_xdim=14, grid_cell_ydim=14)

plotter = pv.Plotter()
# plotter.show_grid()
plotter.add_camera_orientation_widget()
# plotter.add_mesh(fracture_net, render_points_as_spheres=True)
plotter.add_mesh(slices, line_width=2, color='white')
plotter.add_mesh(grids, scalars='p21', line_width=2, cmap='rainbow')

# plotter.add_mesh_slice(pv_points, assign_to_axis='z', color='k')
plotter.show()

