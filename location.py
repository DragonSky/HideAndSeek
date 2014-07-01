__author__ = 'stewartpj'
from collections import defaultdict
import weakref


class Location():
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
        return "<Location: {}, {}, {}>".format(self.x_coord, self.y_coord, self.z_coord)

    def __eq__(self, other):
        if isinstance(other, self.__class__) and self.x_coord == other.x_coord and self.y_coord == other.y_coord \
                and self.z_coord == other.z_coord and self.category == other.category:
            return True
        return False

    def location_matches(self, x, y, z):
        if self.x_coord == x and self.y_coord == y and self.z_coord == z:
            return True
        return False

    @classmethod
    def get_instances(cls):
        for inst_ref in cls.__refs__[cls]:
            inst = inst_ref()
            if inst is not None:
                yield inst

    @classmethod
    def find_locations(cls, x, y, z):
        locations = list()
        for inst_ref in cls.__refs__[cls]:
            inst = inst_ref()
            if inst.location_matches(x, y, z):
                locations.append(inst)
        return locations




