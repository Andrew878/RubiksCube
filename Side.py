import numpy as np


class Side(object):

    def __init__(self, identifier,
                 initial_colour):  # , top_neighbour, left_neighbour, right_neighbour, bottom_neighbour):
        """Create a side of the rubix cube"""
        self.identifier = identifier
        self.initial_colour = initial_colour
        self.top_neighbour = None
        self.left_neighbour = None
        self.right_neighbour = None
        self.bottom_neighbour = None
        # row = [initial_colour, initial_colour, initial_colour]
        self.array_of_squares = [initial_colour, initial_colour, initial_colour], [initial_colour, initial_colour,
                                                                                   initial_colour], [initial_colour,
                                                                                                     initial_colour,
                                                                                                     initial_colour]

    def setNeighbours(self, top_neighbour, left_neighbour, right_neighbour, bottom_neighbour):
        self.top_neighbour = top_neighbour
        self.left_neighbour = left_neighbour
        self.right_neighbour = right_neighbour
        self.bottom_neighbour = bottom_neighbour

    def printSide(self):
        print("Side:", self.identifier)
        for row in self.array_of_squares[:]:
            print(row)
        print("")

    def rotateFromFront(self, direction_clockwise=True):
        c = list.copy(self.array_of_squares)

        if (direction_clockwise):
            self.array_of_squares = [[c[2][0], c[1][0], c[0][0]], [c[2][1], c[1][1], c[0][1]],
                                     [c[2][2], c[1][2], c[0][2]]]
        else:
            self.array_of_squares = [[c[0][2], c[1][2], c[2][2]], [c[0][1], c[1][1], c[2][1]],
                                     [c[0][0], c[1][0], c[2][0]]]
