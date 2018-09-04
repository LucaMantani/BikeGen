from Point import Point
from Visualiser import Visualiser

pts = [ Point(0, 0), Point(0, 0.1), Point(0, 0.2) ]

def updatePoints():
    for i in range(len(pts)):
        pts[i] += Point(0.01, 0.01)

v = Visualiser(pts, updatePoints)

v.run()
