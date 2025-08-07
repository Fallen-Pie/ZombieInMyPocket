from tile_component import Tile

class EnvironmentComponent(object):
    def __init__(self):
        self.__tile_sequence =[]
        pass

    def clear_tiles(self):
        """ Remove all tiles (indoor and outdoor tiles) during reset & start of the game """
        pass
        # self.__tile_sequence = []

    def place_tile(self, tile, x_location, y_location, rotation):
        """ Place a tile on the environment """
        # tile -> Tile object
        # x & y location -> int
        # rotation -> enum 0 | 90 | 180 | 360
        pass