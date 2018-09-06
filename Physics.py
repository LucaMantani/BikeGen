from Vector import Vector
from Bike import Bike
import numpy as np


springx0 = 0.7
radius = 0.03
g_N = 0.0005
driving = 0.001

def springs(bike):
    forces = [ Vector(0, 0) for _ in bike.vertices ]

    for s in bike.springs:
        d = bike.vertices[s.i2] - bike.vertices[s.i1]

        F = s.k * (d.r - springx0) * d.unitVector()

        forces[s.i1] += F - s.damping * bike.wheels[s.i1].vel
        forces[s.i2] -= F + s.damping * bike.wheels[s.i2].vel

    for i in range(len(forces)):
        bike.wheels[i].vel += forces[i] / bike.wheels[i].mass


def gravity(bike):
    gravity_force = Vector(0.0, -g_N)

    for i in range(len(bike.vertices)):
        bike.wheels[i].vel += gravity_force

def ground_collision(bike):
    for i in range(len(bike.vertices)):
        if (bike.vertices[i].y - bike.wheels[i].radius) < -1.0:
            bike.wheels[i].pos = Vector(bike.vertices[i].x, -1.0 + bike.wheels[i].radius)
            bike.wheels[i].vel = Vector(bike.wheels[i].vel.x, 0.0)


def timestep(bike):
    springs(bike)
    gravity(bike)

    for i in range(len(bike.vertices)):
        bike.wheels[i].pos += bike.wheels[i].vel

    ground_collision(bike)

    if bike.vertices[0].y == -1.0 + bike.wheels[i].radius:
        bike.wheels[0].vel += driving / bike.wheels[0].mass * Vector(1.0, 0.0)




