__author__ = 'stewartpj'

from location import Location

class World(object):
    x_size = int()
    y_size = int()
    z_size = int()
    locations = list()

    def __init__(self, x_size, y_size, z_size):
        self.x_size = x_size
        self.y_size = y_size
        self.z_size = z_size

    def __repr__(self):
        return "<World: {}, {}, {}>".format(self.x_size, self.y_size, self.z_size)

    def add_location(self, location):
        """
            >>> import location
            >>> new_world = World(10, 10, 10)
            >>> new_location = location.Location(5, 4, 3)
            >>> new_world.add_location(new_location)
            >>> new_world.add_location(location.Location(11, 5, 4))
            Traceback (most recent call last):
             ...
            ValueError: Location coordinates are outside the world
            >>> new_world.add_location(location.Location(1, 15, 4))
            Traceback (most recent call last):
             ...
            ValueError: Location coordinates are outside the world
            >>> new_world.add_location(location.Location(1, 5, 14))
            Traceback (most recent call last):
             ...
            ValueError: Location coordinates are outside the world
        """
        if self.location_is_in_world(location):
            self.locations.append(location)
        else:
            raise ValueError("Location coordinates are outside the world")

    def location_is_in_world(self, location):
        return location.x_coord <= self.x_size and location.y_coord <= self.y_size and location.z_coord <= self.z_size

    def get_locations_at(self, x, y, z):
        """
            >>> world = World(5, 5, 5)
            >>> world.add_location(Location(1, 2, 3, category="test1"))
            >>> world.add_location(Location(1, 2, 3, category="test2"))
            >>> test = world.get_locations_at(1, 2, 3)
            >>> test
            [<Location: 1, 2, 3, test1>, <Location: 1, 2, 3, test2>]
        """
        result = list()
        for location in self.locations:
            if location.location_matches(x, y, z):
                result.append(location)
        return result

if __name__ == "__main__":
    import doctest
    doctest.testmod()