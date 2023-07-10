"""
Module used to read and parse .FAB files


Returns:
    - data_list: a list of strings of the FAB file
    - line_fracture_index: the list of fracture indexes (obtained from the .fab file
    - vertex_list: the list of the number of vertices fo the given fracture (triangle, rectangle, pentagon etc...)

TODO:
    - Rewrite to be more organized and efficient (maybe use dicts?)
    - Check for inefficiencies
"""

import numpy as np


def fab_parser(path: str) -> tuple[list, list, np.ndarray]:

    with open(path, 'r') as file:
        line_list = file.readlines()

    start_idx = line_list.index('BEGIN FRACTURE\n')+1
    end_idx = line_list.index('END FRACTURE\n')

    data_list = line_list[start_idx:end_idx]

    vertex_list = []
    line_fracture_index = []

    for i, line in enumerate(data_list):
        line_values = line.split()

        if i == 0:
            fracture_line = data_list[i]

            # fracture_number = fracture_line.split()[0]
            vertex_number = fracture_line.split()[1]
            line_fracture_index.append(i)
            vertex_list.append(int(vertex_number))

        elif i == len(data_list)-1:
            continue

        elif line_values[0] == '0':
            fracture_line = data_list[i+1]

            vertex_number = fracture_line.split()[1]
            line_fracture_index.append(i+1)
            vertex_list.append(int(vertex_number))

    vertex_list = np.array(vertex_list)

    return data_list, line_fracture_index, vertex_list
