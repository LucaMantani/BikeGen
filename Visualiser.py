import numpy as np
from matplotlib.patches import Circle
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class Visualiser:

    def run(self):
        
        figure = plt.figure()
        axes = figure.add_subplot('111',aspect='equal')
        axes.set_xlim(-2,7)
        axes.set_ylim(-2,7)

        # add a patch to the axis
        ball = Circle((0.1,0.1), radius=2)
        axes.add_patch(ball)

        def init():
            ball.set_visible(False)
            return [ball]

        def animate(i):
            # shift the ball's position
            if i == 1: ball.set_visible(True)
            ball.center = (i/10.,i/15.)
            return ball,

        # afterwards, switch to zoomable GUI mode
        ani = animation.FuncAnimation(figure, 
                                    animate, 
                                    np.arange(1, 50), 
                                    init_func = init,
                                    interval=25,
                                    blit=True)

        plt.show()
