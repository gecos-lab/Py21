"""
Module used to slice a pyvista 3D fracture network object and calculate the length of each fracture line.

Returns:
    - slices: slices PolyData (multiblock) of the FractureNetwork
    - p21_list: list of p21 values for the given slice

TODO:
    - Add p21 differentiation depending on the slices axis
"""

from pyvista import PolyData
from vtkmodules.vtkFiltersGeometry import vtkGeometryFilter
import numpy as np
from typing import Tuple #for python version <3.9


def slice_frac_net(frac_net: PolyData, n: int = 5, axis: 'str' = 'z') -> Tuple[PolyData, list]:

    slices = frac_net.slice_along_axis(n=n, axis=axis)

    p21_list = []

    for s in slices:
        x_min, x_max, y_min, y_max, z_min, z_max = s.bounds

        area_xy = (x_max-x_min)*(y_max-y_min)
        area_xz = (x_max-x_min)*(z_max-z_min)
        area_yz = (y_max-y_min)*(z_max-z_min)

        id_list = s.cell_data['Fracture number']

        geometry_filter = vtkGeometryFilter()
        for idx in id_list:

            line = s.extract_cells(s.cell_data['Fracture number'] == idx)
            geometry_filter.SetInputData(line)
            geometry_filter.Update()

            pv_line = PolyData(geometry_filter.GetOutput())
            length = pv_line.compute_arc_length()['arc_length']

            s.cell_data['lengths'][np.where(s.cell_data['Fracture number'] == idx)] = max(length)

        p21 = sum(s.cell_data['lengths'])/area_xy
        p21_list.append(p21)

    return slices, p21_list




