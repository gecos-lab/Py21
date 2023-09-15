import pyvista as pv
from vtkmodules.all import *


def cell_selector(bid, dataset):

    print(f'cell id: {dataset["cid"]}')
    print(f'block id: {bid}')
    plotter.add_mesh(dataset, name='sel_cell', style='wireframe', color='yellow')


x_dim = 300 # grid dimension along x
y_dim = 300 # grid dimension along y

x_res = 20 # the resolution is the n of cells along the direction (so for one cell of 15x15 we have 20 cells)
y_res = 20

grid = pv.Plane(i_size=x_dim,
                j_size=y_dim,
                i_resolution=x_res,
                j_resolution=y_res)


# plot the grid

cells = pv.MultiBlock()

for cid in range(grid.n_cells):
    cell = grid.get_cell(cid)
    cell_poly = pv.PolyData(cell.points, faces=[4, 0, 1, 2, 3])
    cell_poly.cell_data["cid"] = [cid]
    cells.append(cell_poly)


# plotter = pv.Plotter()
#
# plotter.add_mesh(cells)
# plotter.background_color = 'gray'
# plotter.add_camera_orientation_widget()
# plotter.enable_block_picking(callback=cell_selector)
# plotter.show()


# Penso che si possa usare questo https://vtk.org/doc/nightly/html/classvtkCutter.html#details con un loop per ogni cella
# della griglia. Questo è per estrarre le celle:
# https://vtk.org/doc/nightly/html/classvtkPolyData.html#a711ed1ebb7bdf4a4e2ed6896081cd1b2