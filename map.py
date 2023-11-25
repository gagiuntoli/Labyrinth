
def get_cell(position, cell_size):
    return (int(position[1]/cell_size), int(position[0]/cell_size))

def is_inside_map(map, i, j):
    return i >= 0 and i < len(map) and j >= 0 and j < len(map[0])

