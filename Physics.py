from Vector import Vector
from Bike import Bike
import numpy as np


mass = 1
springk = 0.001
springx0 = 1
radius = 0.03

damping = 0.01

def springs(bike):
    forces = [ Vector(0, 0) for _ in bike.vertices ]

    for i1, i2 in bike.pairs():
        d = bike.vertices[i2] - bike.vertices[i1]
        F = springk * (d.r - springx0) * d.unitVector()
        forces[i1] += F
        forces[i2] -= F

    for i in range(len(forces)):
        bike.velocities[i] += forces[i] / mass


def gravity(bike):
    pass

def damping(bike):
    pass

def timestep(bike):
    springs(bike)
    gravity(bike)
    damping(bike)

    for i in range(len(bike.vertices)):
        bike.vertices[i] += bike.velocities[i]

#    for wheel in bike.vertices:

        # Compute force from gravity and springs

        # Update position based on forces

        # Detect collisions with ground

        # Update position again based on collisions




