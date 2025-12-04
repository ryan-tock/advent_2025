def get_neighbors(point, x_max, y_max):
    neighbors = [(point[0] + i, point[1] + j) for i in range(-1, 2) for j in range(-1, 2)]
    neighbors = [n for n in neighbors if n != point]
    neighbors = [n for n in neighbors if 0 <= n[0] < x_max and 0 <= n[1] < y_max]

    return neighbors