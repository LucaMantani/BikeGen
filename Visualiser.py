import numpy as np
from matplotlib.patches import Circle, Polygon
import matplotlib.pyplot as plt
import matplotlib.animation as animation


class Visualiser:

    def __init__(self, bike, updateFunc):
        self.bike = bike
        self.updateFunc = updateFunc


    def run(self):

        # Initialize figure
        figure = plt.figure()
        axes = figure.add_subplot('111', aspect='equal')
        axes.set_xlim(0, 1)
        axes.set_ylim(0, 1)

        # Initialize graphics objects
        vertices = []
        for vertex in self.bike.vertices:
            newVertex = Circle((vertex.x(), vertex.y()), 0.01)
            newVertex.set_visible(False)
            vertices.append(newVertex)
            axes.add_patch(newVertex)

        lines = []
        for line in self.bike.springs(): 
            newLine = Polygon([ [ line[0].x(), line[0].y() ], [ line[1].x(), line[1].y()] ], fill=False)
            newLine.set_visible(False)
            lines.append(newLine)
            axes.add_patch(newLine)


        def animate(frameNumber):
            # Without this, a copy of the figure will always be shown at its original position
            # Probably an easier way to do this, but the workaround is fine
            if frameNumber == 1:
                for vertex in vertices:
                    vertex.set_visible(True)
                for line in lines:
                    line.set_visible(True)

            # Call the user updateFunc
            self.updateFunc()

            # Update position of graphical objects
            for i in range(len(vertices)):
                vertices[i].center = (self.bike.vertices[i].x(), self.bike.vertices[i].y())
            
            l = self.bike.springs()
            for i in range(len(lines)):
                lines[i].set_xy([ [ l[i][0].x(), l[i][0].y() ], [ l[i][1].x(), l[i][1].y() ]])

            return lines + vertices


        ani = animation.FuncAnimation(figure,
                                      animate,
                                      interval=25,
                                      blit=True)

        plt.show()
