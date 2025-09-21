class Player:
    def __init__(self):
        self.__attack_score=1
        self.__health_score=6
        self.__item_inventory=("", "")
        self.__location=(0,0)

    def clear_inventory(self):
        pass

    def set_location(self, x_location, y_location):
        pass

    def get_location(self):
        """ Returns Position """
        pass