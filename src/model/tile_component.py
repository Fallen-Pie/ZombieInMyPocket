class Tile:
    def __init__(self):
        self.__rotation=0
        self.__door=[] # e.g. could be a dict with 1:true,2:false,3:true
        self.__encounter=""  # references the encounter component

