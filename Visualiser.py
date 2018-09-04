import numpy as np
from matplotlib.patches import Circle
import matplotlib.pyplot as plt
import matplotlib.animation as animation


class Visualiser:

    def __init__(self, pts, updateFunc):
        self.pts = pts
        self.updateFunc = updateFunc

    def run(self):

        figure = plt.figure()
        axes = figure.add_subplot('111', aspect='equal')
        axes.set_xlim(0, 1)
        axes.set_ylim(0, 1)

        line, = axes.plot([], [], 'b.', ms=16)

        def animate(i):
            self.updateFunc()
            xs = [ p.x() for p in self.pts ]
            ys = [ p.y() for p in self.pts ]
            line.set_data(xs, ys)
            return line,

        # afterwards, switch to zoomable GUI mode
        ani = animation.FuncAnimation(figure,
                                      animate,
                                      interval=25,
                                      blit=True)

        plt.show()
