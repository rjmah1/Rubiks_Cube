import numpy as np
import pygame
import OpenGL

Vertices = ((-1, -1, -1), (-1, -1, 1), (-1, 1, -1), (-1, 1, 1),
            (1, -1, -1), (1, -1, 1), (1, 1, -1), (1, 1, 1))

# Edges connecting the Vertices.
Edges = ((0, 1), (0, 2), (0, 4), (1, 3), (1, 5), (2, 3), (2, 6), (3, 7), (4, 5), (4, 6), (5, 7), (6, 7))

# Surfaces of made from Vertices going clockwise from the starting point.
# ( B, L, D, U, R, F)
Surfaces = ((0, 2, 3, 1), (0, 1, 5, 4), (0, 4, 6, 2), (1, 3, 7, 5),
            (2, 6, 7, 3), (4, 5, 7, 6))

# Red, Green, Blue, White, Yellow, Orange as RGB
Colours = ((1, 0, 0), (0 , 1, 0), (0, 0, 1), (1, 1, 1), (1, 1, 0), (1, 0.5, ))





if __name__ == "__main__":
    run()
    pygame.quit()
    quit()