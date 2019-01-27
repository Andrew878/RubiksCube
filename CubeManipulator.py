import Side as Side


class CubeManipulator(object):

    def __init__(self, all_sides):
        self.all_sides = all_sides
        self.front = all_sides[0]
        self.top = all_sides[1]
        self.right = all_sides[2]
        self.left = all_sides[3]
        self.bottom = all_sides[4]
        self.back = all_sides[5]


    def printCubeState(self):
        for side in self.all_sides:
            side.printSide()

    def rotateSide(self, side_from_front_view, direction_clockwise=True):
        side_from_front_view.rotateFromFront(direction_clockwise)

        if side_from_front_view.identifier == "Right" or side_from_front_view.identifier == "Left":
            True






