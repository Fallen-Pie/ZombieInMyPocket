from src.model.game_pieces.tile_builder import TileBuilder

class TileDirector:
    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> TileBuilder:
        return self._builder

    def set_builder(self, builder: TileBuilder) -> None:
        self._builder = builder

    def build_minimal_tite(self, name, direction) -> None:
        self.builder.set_name(name)
        self.builder.set_direction(direction)

    def build_tite_with_encounter(self, name, direction, encounter) -> None:
        self.builder.set_name(name)
        self.builder.set_direction(direction)
        self.builder.set_encounter(encounter)

    def build_tite_with_exit(self, name, direction, exit) -> None:
        self.builder.set_name(name)
        self.builder.set_direction(direction)
        self.builder.set_front_door(exit)
