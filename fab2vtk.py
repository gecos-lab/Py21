"""
Module used to convert a FAB parsed file in vtk object

Returns:
    - fracture_net: pyvista PolyData object
"""

import numpy as np

from pyvista import PolyData


def fab2vtk(data_list, line_fracture_index, vertex_list) -> PolyData:

    all_points = np.array([])

    connectivity_list = []
    fracture_number_list = []

    for c, (line_index, n_vertex) in enumerate(zip(line_fracture_index, vertex_list)):

        jump = n_vertex+2

        fracture_number = int(data_list[line_index].split()[0])
        point_lines = data_list[line_index+1:line_index+jump]

        connectivity_list.append(n_vertex)

        points = np.empty((n_vertex, 3))
        normal = np.empty((1, 3))

        for i, item in enumerate(point_lines):

            point_string = item[9:].strip().split()
            point_float = [float(number) for number in point_string]

            if i < n_vertex:
                points[i, :] = point_float
                connectivity_list.append(len(all_points)+i)
            else:
                normal[0, :] = point_float

        all_points = np.append(all_points, points).reshape(-1, 3)
        fracture_number_list.append(fracture_number)

        # fracture_table.loc[c] = [fracture_number, points, normal]

    fracture_net = PolyData(all_points, faces=connectivity_list)

    fracture_net.cell_data['Fracture number'] = fracture_number_list
    fracture_net.cell_data['lengths'] = [0.0]*len(fracture_number_list)

    fracture_net.cell_data_to_point_data()

    return fracture_net
