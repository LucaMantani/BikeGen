import numpy as np
from matplotlib.patches import Circle, Polygon
import matplotlib.pyplot as plt
import matplotlib.animation as animation


class Visualiser:

    def __init__(self, bike, ground, updateFunc):
        self.bike = bike
        self.ground = ground
        self.updateFunc = updateFunc


    def run(self):

        # Initialize figure
        figure = plt.figure()
        axes = figure.add_subplot('111', aspect='equal')
        axes.set_xlim(-1, 1)
        axes.set_ylim(-1, 1)

        # Initialize graphics objects
        vertices = []
        for wheel in self.bike.wheels:
            newVertex = Circle((wheel.pos.x, wheel.pos.y), wheel.radius)
            newVertex.set_visible(False)
            vertices.append(newVertex)
            axes.add_patch(newVertex)

        lines = []
        for line in self.bike.springVertices(): 
            newLine = Polygon([ [ line[0].x, line[0].y ], [ line[1].x, line[1].y] ], fill=False)
            newLine.set_visible(False)
            lines.append(newLine)
            axes.add_patch(newLine)

        ground = Polygon([[-1, -1]] + [ [ p.x, p.y ] for p in self.ground.vertices ] + [[1, -1]])
        axes.add_patch(ground)

        def animate(frameNumber):
            # Without this, a copy of the figure will always be shown at its original position
            # Probably an easier way to do this, but the workaround is fine
            if frameNumber == 1:
                for vertex in vertices:
                    vertex.set_visible(True)
                for line in lines:
                    line.set_visible(True)

            # Call the user updateFunc
            self.updateFunc(frameNumber)

            # Update position of graphical objects
            for i in range(len(vertices)):
                vertices[i].center = (self.bike.vertices[i].x, self.bike.vertices[i].y)
            
            l = self.bike.springVertices()
            for i in range(len(lines)):
                lines[i].set_xy([ [ l[i][0].x, l[i][0].y ], [ l[i][1].x, l[i][1].y ]])

            return lines + vertices


        ani = animation.FuncAnimation(figure,
                                        animate,
                                        interval=25,
                                        blit=True)

        plt.show()
