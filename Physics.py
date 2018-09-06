from Vector import Vector
from Bike import Bike
import numpy as np
from Ground import Ground

springx0 = 0.7
g_N = 0.0005
driving = 0.000

def springs(bike):
    forces = [ Vector(0, 0) for _ in bike.wheels ]

    for s in bike.springs:
        w1, w2 = bike.wheels[s.i1], bike.wheels[s.i2]
        d = w2.pos - w1.pos

        F = s.k * (d.r - springx0) * d.unitVector()
        forces[s.i1] += F - s.damping * w1.vel
        forces[s.i2] -= F + s.damping * w2.vel

    for i in range(len(forces)):
        bike.wheels[i].vel += forces[i] / bike.wheels[i].mass


def gravity(bike):
    gravity_force = Vector(0.0, -g_N)

    for wheel in bike.wheels:
        wheel.vel += gravity_force


def ground_collision(bike, ground):
    for wheel in bike.wheels:
        distanceVector = ground.distance(wheel.pos)
        if distanceVector.r < wheel.radius:
            dPerp = distanceVector.unitVector()
            dPar  = Vector(dPerp.y, -dPerp.x)

            vPar = wheel.vel.scalarProduct(dPar)

            wheel.pos += (wheel.radius - distanceVector.r) * dPerp
            wheel.vel = vPar * dPar

            

def timestep(bike, ground):
    springs(bike)
    gravity(bike)

    for wheel in bike.wheels:
        wheel.pos += wheel.vel

    ground_collision(bike, ground)

    if bike.vertices[0].y == -1.0 + bike.wheels[0].radius:
        bike.wheels[0].vel += driving / bike.wheels[0].mass * Vector(1.0, 0.0)




