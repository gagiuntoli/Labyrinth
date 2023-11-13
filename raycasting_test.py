
from math import pi

from raycasting import compute_rays

def test_distance_3x3():
    map = [
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1]
    ]

    position = (150, 150)
    angle = 0.0
    rays = compute_rays(map, position, angle, 1, 0.0)
    assert rays == [(angle, 50.0)]

    position = (150, 150)
    angle = 0.0
    rays = compute_rays(map, position, angle, 3, pi/2)
    assert rays[1] == (angle, 50.0)

    position = (150, 150)
    angle = pi
    rays = compute_rays(map, position, angle, 1, 0.0)
    assert rays == [(angle, 50.0)]

    position = (150, 150)
    angle = pi/2
    rays = compute_rays(map, position, angle, 1, 0.0)
    assert rays == [(angle, 50.0)]

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
    assert rays == [(angle, 150.0)]

    position = (250, 250)
    angle = 0.0
    rays = compute_rays(map, position, angle, 3, pi/2)
    assert rays[1] == (0.0, 150.0)

    position = (250, 250)
    angle = pi
    rays = compute_rays(map, position, angle, 1, 0.0)
    assert rays == [(angle, 150.0)]

