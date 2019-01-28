import numpy as np


class Side(object):

    def __init__(self, identifier,
                 initial_colour,
                 able_to_rotate_with_row_objects, LENGTH_OF_CUBE=3):
        """Create a side of the rubix cube"""
        self.identifier = identifier
        self.initial_colour = initial_colour
        self.LENGTH_OF_CUBE = LENGTH_OF_CUBE
        self.top_neighbour = None
        self.left_neighbour = None
        self.right_neighbour = None
        self.bottom_neighbour = None
        self.all_neighbours = None
        self.able_to_rotate_with_row_objects = able_to_rotate_with_row_objects
        self.array_of_squares = [[self.initial_colour] * self.LENGTH_OF_CUBE] * self.LENGTH_OF_CUBE

    def setNeighbours(self, top_neighbour, left_neighbour, right_neighbour, bottom_neighbour):
        """Sets the relative neighbours of a side object"""
        self.top_neighbour = top_neighbour
        self.left_neighbour = left_neighbour
        self.right_neighbour = right_neighbour
        self.bottom_neighbour = bottom_neighbour
        self.all_neighbours = {"Top": self.top_neighbour, "Bottom": self.bottom_neighbour,
                               "Right": self.right_neighbour, "Left": self.left_neighbour}

    def printSide(self):
        """Prints the side's elements"""
        print("Side:", self.identifier)
        for row in self.array_of_squares[:]:
            print(row)
        print("")

    def rotateFromFront(self, direction_clockwise=True):
        """As if the viewer was facing the front of the side, this function rotates the side (and its elements)
        clockwise/clockwise"""

        c = list.copy(self.array_of_squares)

        if (direction_clockwise):
            self.array_of_squares = [[c[2][0], c[1][0], c[0][0]], [c[2][1], c[1][1], c[0][1]],
                                     [c[2][2], c[1][2], c[0][2]]]
        else:
            self.array_of_squares = [[c[0][2], c[1][2], c[2][2]], [c[0][1], c[1][1], c[2][1]],
                                     [c[0][0], c[1][0], c[2][0]]]

    def getRowOrColumnCopyForRotation(self, orientation):
        c = list.copy(self.array_of_squares)

        if orientation == "Top":
            return c[0]

        elif orientation == "Bottom":
            return c[2]

        elif orientation == "Right":
            return [c[0][2], c[1][2], c[1][2]]

        elif orientation == "Left":
            return [c[0][0], c[1][0], c[1][0]]
        else:
            raise ValueError("Needs to 'Top'/'Bottom/'Right'/'Left'")

    def replaceRowOrColumnCopyForRotation(self, orientation, replacement_list):

        if orientation == "Top":
            self.array_of_squares[0] = replacement_list

        elif orientation == "Bottom":
            self.array_of_squares[2] = replacement_list

        elif orientation == "Right":

            for i in range(0, self.LENGTH_OF_CUBE):
                self.array_of_squares[i][2] = replacement_list[i]

        elif orientation == "Left":

            for i in range(0, self.LENGTH_OF_CUBE):
                self.array_of_squares[i][0] = replacement_list[i]

        else:
            raise ValueError("Needs to be 'Top'/'Bottom/'Right'/'Left'")


