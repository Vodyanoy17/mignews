"""Point that the given point is considered
"""


class Point:
    """_summary_"""

    def __init__(self, x_coord, y_coord):
        """AI  the coordinates of the point.

        Args:
            x_coord ([type]): [description]
            y_coord ([type]): [description]
        """
        self.__x_coord = x_coord
        self.__y_coord = y_coord
    def get_point(self):
        """Return the point"""
        return (self.__x_coord, self.__y_coord)
