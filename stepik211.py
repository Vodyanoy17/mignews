"""Point that the given point is considered
"""


class Point:
    """hhggjk ,kuyhuhy.lk ,kuyhuhy  hhggjk"""

    def prosto(self):
        """_summary_    method"""
        print("Point with respect to " + self)

    def __init__(self, x_coord, y_coord):
        """AI  the coordinates of the point.
        Args:
            x_coord : [description]
            y_coord ([type]): [description]
        """
        self.__x_coord = x_coord
        self.__y_coord = y_coord

    def get_coord(self):
        """Return the point"""
        return (self.__x_coord, self.__y_coord)

    def set_coord(self, x_coord, y_coord):
        """Set the coordinates of the point"""
        self.__x_coord = x_coord
        self.__y_coord = y_coord
