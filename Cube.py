import numpy as np
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGl.GLU import *

SCREEN_SIZE = (800, 600)

VERTICES = ((-1, -1, -1), (-1, -1, 1), (-1, 1, -1), (-1, 1, 1),
            (1, -1, -1), (1, -1, 1), (1, 1, -1), (1, 1, 1))

# Edges connecting the Vertices.
EDGES = ((0, 1), (0, 2), (0, 4), (1, 3), (1, 5), (2, 3), (2, 6), (3, 7), (4, 5), (4, 6), (5, 7), (6, 7))

# Surfaces of made from Vertices going clockwise from the starting point.
# ( B, L, D, U, R, F)
SURFACES = ((0, 2, 3, 1), (0, 1, 5, 4), (0, 4, 6, 2), (1, 3, 7, 5),
            (2, 6, 7, 3), (4, 5, 7, 6))

# Red, Green, Blue, White, Yellow, Orange as RGB
COLOURS = ((1, 0, 0), (0 , 1, 0), (0, 0, 1), (1, 1, 1), (1, 1, 0), (1, 0.5, 0))


class Cubie():
    def __init__(self, id, N, scale):
        self.N = N
        self.scale = scale
        self.init_pos = [*id]
        self.current_pos = [*id]
        self.rot = [[1 if i==j else 0 for i in range(3)] for j in range(3)]


class Cube():
    def __init__(self, N, scale):
        self.N = N
        cube_range = range(self.N)
        self.cubies = [Cubie((x, y, z), self.N, scale) for x in cube_range for y in cube_range for z in cube_range]
    
    def mainloop(self):
        while True:
            #do something
            continue



def main():
    pygame.init()
    pygame.display.set_mode(SCREEN_SIZE, DOUBLEBUF|OPENGL)
    glEnable(GL_DEPTH_TEST)
    glMatrixMode(GL_PROJECTION)
    gluPerspective(45, (SCREEN_SIZE[0]/SCREEN_SIZE[1]), 0.1, 50.0)

    NewCube = Cube(3, 1.0)
    NewCube.mainloop()


if __name__ == "__main__":
    main()
    pygame.quit()
    quit()