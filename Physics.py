from Vector import Vector
from Bike import Bike
import numpy as np


mass = 1
springk = 0.01
springx0 = 0.7
radius = 0.03
g_N = 0.0001
driving = 0.001

damping = 0.01

def springs(bike):
    forces = [ Vector(0, 0) for _ in bike.vertices ]

    for i1, i2 in bike.pairs():
        d = bike.vertices[i2] - bike.vertices[i1]
        F = springk * (d.r - springx0) * d.unitVector()
        forces[i1] += F - damping * bike.velocities[i1]
        forces[i2] -= F + damping * bike.velocities[i2]

    for i in range(len(forces)):
        bike.velocities[i] += forces[i] / mass


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
        bike.velocities[0] += driving / mass * Vector(1.0, 0.0)

#    for wheel in bike.vertices:

        # Compute force from gravity and springs

        # Update position based on forces

        # Detect collisions with ground

        # Update position again based on collisions




