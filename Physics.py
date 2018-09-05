from Point import Point
from Bike import Bike
import numpy as np

def timestep(bike):
    "Evaluate the physics for the bike in a small dt timestep"

    #for now set some values manually
    #spring constants=1, damping=0.1
    masses = np.ones(4)
    spring_constants = np.ones(6)

    #first point of bike is the wheel with constant force
    driving_wheel = bike.vertices[0]

    #split the computation in 4 subfunctions
    compute_spring_forces(bike,spring_constants,masses)
    compute_wheel_force(bike)
    compute_gravity(bike)
    compute_ground_collision(bike)

    #do the dt timestep by updating the velocities and the vertices

    #return updated bike
    return bike
    
def compute_spring_forces(bike,spring_constants,masses):
    "Solve the dgl for the springs for a dt timestep, return 4 forces?"

    
