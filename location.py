__author__ = 'stewartpj'
from collections import defaultdict
import weakref


class Location(object):
    """
        This class will be used to contain the details of particular location.
    """
    __refs__ = defaultdict(list)

    def __init__(self, x, y, z, category=None):
        self.__refs__[self.__class__].append(weakref.ref(self))
        self.x_coord = x
        self.y_coord = y
        self.z_coord = z
        self.category = category
    #
    # def __del__(self):
    #     for inst_ref in self.__class__.__refs__[self.__class__]:
    #         if inst_ref() == self:
    #             self.__class__.__refs__[self.__class__].remove(inst_ref)
    #             print("removing {} from location list.".format(self))

    def __repr__(self):
        return "<Location: {}, {}, {}, {}>".format(self.x_coord, self.y_coord, self.z_coord, self.category)

    def __eq__(self, other):
        if isinstance(other, self.__class__) and self.x_coord == other.x_coord and self.y_coord == other.y_coord \
                and self.z_coord == other.z_coord and self.category == other.category:
            return True
        return False

    def location_matches(self, x, y, z):
        """
            >>> location = Location(1, 2, 3)
            >>> location.location_matches(1, 2, 3)
            True
            >>> location.location_matches(5, 2, 3)
            False
            >>> location.location_matches(1, 5, 3)
            False
            >>> location.location_matches(1, 2, 5)
            False
        """
        return self.x_coord == x and self.y_coord == y and self.z_coord == z


if __name__ == "__main__":
    import doctest
    doctest.testmod()