from Vector import Vector
from Bike import Bike
import numpy as np


# mass = 1
springx0 = 0.7
radius = 0.03
g_N = 0.0005
driving = 0.001

def springs(bike):
    forces = [ Vector(0, 0) for _ in bike.vertices ]

    for s in bike.springs:
        d = bike.vertices[s.i2] - bike.vertices[s.i1]

        F = s.k * (d.r - springx0) * d.unitVector()

        forces[s.i1] += F - s.damping * bike.velocities[s.i1]
        forces[s.i2] -= F + s.damping * bike.velocities[s.i2]

    for i in range(len(forces)):
        bike.velocities[i] += forces[i] / bike.masses[i]


def gravity(bike):
    gravity_force = Vector(0.0, -g_N)

    for i in range(len(bike.vertices)):
        bike.velocities[i] += gravity_force

def ground_collision(bike):
    for i in range(len(bike.vertices)):
        if bike.vertices[i].y < -1.0:
            bike.vertices[i] = Vector(bike.vertices[i].x, -1.0)
            bike.velocities[i] = Vector(bike.velocities[i].x, 0.0)


def timestep(bike):
    springs(bike)
    gravity(bike)

    for i in range(len(bike.vertices)):
        bike.vertices[i] += bike.velocities[i]

    ground_collision(bike)

    if bike.vertices[0].y == -1.0:
        bike.velocities[0] += driving / bike.masses[0] * Vector(1.0, 0.0)




