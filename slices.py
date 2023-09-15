"""
Module used to slice a pyvista 3D fracture network object and calculate the length of each fracture line.

Returns:
    - slices: slices PolyData (multiblock) of the FractureNetwork
    - p21_list: list of p21 values for the given slice

TODO:
    - Add p21 differentiation depending on the slices axis
"""

from pyvista import PolyData, Plane, MultiBlock
from vtkmodules.vtkFiltersGeometry import vtkGeometryFilter
import numpy as np
from typing import Tuple #for python version <3.9

from vtkmodules.vtkFiltersModeling import vtkCookieCutter


def slice_frac_net(frac_net: PolyData,
                   n_slices: int = 5,
                   axis: 'str' = 'z',
                   grid_cell_xdim: int = 15,
                   grid_cell_ydim: int = 15) -> Tuple[PolyData, MultiBlock]:

    slices = frac_net.slice_along_axis(n=n_slices, axis=axis)

    grids = MultiBlock()

    for s in slices:
        # print(s)
        centre = s.center

        x_min, x_max, y_min, y_max, z_min, z_max = s.bounds

        x_dim = int(x_max-x_min)
        y_dim = int(y_max-y_min)

        x_res = int(x_dim/grid_cell_xdim)
        y_res = int(y_dim/grid_cell_ydim)

        grid = Plane(centre, i_size=x_dim, j_size=y_dim, i_resolution=x_res, j_resolution=y_res)
        n_cells = grid.n_cells
        p21_list = np.zeros(n_cells)
        for cid in range(n_cells):
            cell = grid.get_cell(cid)
            cell_poly = PolyData(cell.points, faces=[4, 0, 1, 2, 3])
            cutter = vtkCookieCutter()
            cutter.SetInputData(s)
            cutter.SetLoopsData(cell_poly)
            cutter.Update()

            pixel = PolyData(cutter.GetOutput())
            id_list = pixel.cell_data['Fracture number']
            geometry_filter = vtkGeometryFilter()

            lengths = []
            for idx in id_list:

                line = pixel.extract_cells(pixel.cell_data['Fracture number'] == idx)
                geometry_filter.SetInputData(line)
                geometry_filter.Update()

                pv_line = PolyData(geometry_filter.GetOutput())
                length = pv_line.compute_arc_length()['arc_length']

                lengths.append(sum(length))

            p21 = sum(lengths)/(grid_cell_xdim*grid_cell_ydim)
            p21_list[cid] = p21

        grid.cell_data['p21'] = p21_list
        grids.append(grid)

    return slices, grids




