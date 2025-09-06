from controller.game_controller import GameController



def main():
    game_controller = GameController()
    game_controller.set_up()
    game_controller.begin_game()



if __name__ == "__main__":
    main()

