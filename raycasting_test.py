
from math import pi, sqrt

from raycasting import compute_rays

TOL = 1e-1

def test_distance_3x3():
    map = [
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1]
    ]

    position = (150, 150)
    angle = 0.0
    rays = compute_rays(map, position, angle, 1, 0.0)
    assert abs(rays[0][1] - 50) < TOL

    position = (150, 150)
    angle = pi
    rays = compute_rays(map, position, angle, 1, 0.0)
    assert abs(rays[0][1] - 50) < TOL
    
    position = (150, 150)
    angle = pi/2
    rays = compute_rays(map, position, angle, 1, 0.0)
    assert abs(rays[0][1] - 50) < TOL

    position = (150, 150)
    angle = 3*pi/2
    rays = compute_rays(map, position, angle, 1, 0.0)
    assert abs(rays[0][1] - 50) < TOL

def test_distance_5x5():
    map = [
        [1, 1, 1, 1, 1],
        [1, 0, 0, 0, 1],
        [1, 0, 0, 0, 1],
        [1, 0, 0, 0, 1],
        [1, 1, 1, 1, 1]
    ]

    position = (250, 250)
    angle = 0.0
    rays = compute_rays(map, position, angle, 1, 0.0)
    assert abs(rays[0][1] - 150) < TOL

    position = (250, 250)
    angle = pi
    rays = compute_rays(map, position, angle, 1, 0.0)
    assert abs(rays[0][1] - 150) < TOL

    position = (250, 250)
    angle = pi/2
    rays = compute_rays(map, position, angle, 1, 0.0)
    assert abs(rays[0][1] - 150) < TOL

    position = (250, 250)
    angle = 3*pi/2
    rays = compute_rays(map, position, angle, 1, 0.0)
    assert abs(rays[0][1] - 150) < TOL

    position = (250, 250)
    angle = pi/4
    rays = compute_rays(map, position, angle, 1, 0.0)
    assert abs(rays[0][1] - sqrt(2 * 150**2)) < TOL

    position = (250, 250)
    angle = 3*pi/4
    rays = compute_rays(map, position, angle, 1, 0.0)
    assert abs(rays[0][1] - sqrt(2 * 150**2)) < TOL

    position = (250, 250)
    angle = 5*pi/4
    rays = compute_rays(map, position, angle, 1, 0.0)
    assert abs(rays[0][1] - sqrt(2 * 150**2)) < TOL

