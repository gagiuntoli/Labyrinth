from math import sin, cos, sqrt

def polar_to_cartesian(module, angle):
    return (module * cos(angle), module * sin(angle))

def get_norm(vector):
    return sqrt(vector[0]**2 + vector[1]**2)

def normalize(vector, new_norm):
    norm = get_norm(vector)
    factor = new_norm/norm
    return (vector[0]*factor, vector[1]*factor)

