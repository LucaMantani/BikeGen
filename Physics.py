from Point import Point
from Bike import Bike
import numpy as np

def timestep(bike):
    "Evaluate the physics for the bike in a small dt timestep"

    #for now set some values manually
    #spring constants=1, masses=1, damping=0.1
    #maybe include this in the bike class?!
    masses = np.ones(4)
    spring_constants = np.ones(6)

    #split the computation in 4 subfunctions
    compute_spring_forces(bike,spring_constants,masses)
    compute_wheel_force(bike)
    for i in range(len(bike.vertices)):
        bike.vertices[i] +=Point(0,-0.003)
    #for vert in bike.vertices:
    #    vert = compute_gravity(vert)
    compute_ground_collision(bike)

    #do the dt timestep by updating the velocities and the vertices

    #return updated bike
    return bike
    
def compute_spring_forces(bike,spring_constants,masses):
    "Solve the dgl for the springs for a dt timestep, return 4 forces?"
    damping = 0.1


def compute_wheel_force(bike):
    "Compute the force on the wheel due to the constant torque"
    #first point of bike is the wheel, add constant force
    bike.vertices[0] += Point(0.002,0)

#def compute_gravity(vert):
#    "Include a simple form of gravity"
#    vert += Point(0,-0.002)
#    return vert
    
def compute_ground_collision(bike):
    "Check if point of the bike hit the ground"
    for i in range(len(bike.vertices)):
        if bike.vertices[i].y() < 0.0:
            bike.vertices[i] = Point(bike.vertices[i].x(),0)
    #for vert in bike.vertices:
    #    if float(vert.y()) < 0.0:
    #        vert.y = 0.0
