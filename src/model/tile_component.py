class Tile:
    def __init__(self):
        self.__name=""
        self.__type= "" #Could be enum INDOOR|OUTDOOR
        self.__exits=[] # Refers to the door (indoor tile) and open-grassy-edge (outdoor) e.g. could be a dict with 1:true,2:false,3:true
        self.__encounter=""  # references the encounter component