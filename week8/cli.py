from game import SingleModeGame, TwoPlayerModeGame
import logic
from player import Player


if __name__ == '__main__':
    print("Please Select a Game Mode:")
    print("1 - One Player Mode")
    print("2 - Two Player Mode")

    valid_input_game_mode = False
    _game_mode = ""

    while not valid_input_game_mode:
        _game_mode = input("Enter number: ")

        valid_input_game_mode = logic.validate_game_mode_input(_game_mode)

        if not valid_input_game_mode:
            print("INVALID INPUT. PLEASE RE-ENTER.")

    game_mode = int(_game_mode)

    game = None

    x_player, o_player = None, None

    if game_mode == 1:
        print("You are on One Player Mode")
        game = SingleModeGame()

        # TODO: Add validation for username
        _input_username = input("Please enter your username: ")

        x_player = Player(username=_input_username, is_x=True, is_bot=False)
        o_player = Player(username="BOT", is_x=False, is_bot=True)

        game.add_player(x_player)
        game.add_player(o_player)

    elif game_mode == 2:
        print("You are on Two Player Mode")

        # TODO: Add validation for username
        _x_input_username = input("Please enter X username: ")
        _o_input_username = input("Please enter O username: ")

        x_player = Player(username=_x_input_username, is_x=True, is_bot=False)
        o_player = Player(username=_o_input_username, is_x=False, is_bot=False)

        game = TwoPlayerModeGame()

        game.add_player(x_player)
        game.add_player(o_player)

    board = game.board.get_board()
    winner = game.get_winner()

    current_player = "X"

    print()
    print("GAME START")
    print("---------------------------------------")

    game.game_interface()
