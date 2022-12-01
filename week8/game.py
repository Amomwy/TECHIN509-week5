import random
import uuid
from typing import Tuple

from log import Log
from logic import Board, other_player, validate_input, get_winner
from statistics import GlobalRank


class Game:
    def __init__(self):
        self.game_id = uuid.uuid4()
        self.game_mode = 0  # 1 means one-gamer (user vs bot), 2 means two-player (user vs user)
        self.board = Board()
        # self.players = ["X", other_player("X")]
        self.players = []
        self.winner = None

    def get_game_id(self):
        return self.game_id

    def add_player(self, player):
        self.players.append(player)

    def get_players(self):
        return self.players

    def get_winner(self):
        return self.winner

    def game_interface(self):
        pass


class SingleModeGame(Game):
    def __init__(self):
        super().__init__()
        self.is_user_turn = True

    def _get_empty_space(self):
        space = []

        for i in range(3):
            for j in range(3):
                if self.board.get_board_element(i, j) is None:
                    space.append((i, j))

        return space

    def bot_random_step(self) -> Tuple:
        _empty_space = self._get_empty_space()

        return _empty_space[random.randint(0, len(_empty_space) - 1)]

    def game_interface(self):
        while self.winner is None:
            if not self.is_user_turn:
                print("Bot takes a turn!")

                bot_step = self.bot_random_step()

                print("Bot takes " + str(bot_step))

                self.board.set_board(bot_step[0], bot_step[1], "O")  # bot always takes O

            else:
                print("Player takes a turn!")

                # Show the board to the user.
                print("CURRENT BOARD: ")
                print(self.board)

                # Input a move from the player.
                valid_input = False
                _x, _y = "", ""

                while not valid_input:
                    _x = input("Enter Coordinate For Row (zero-index): ")
                    _y = input("Enter Coordinate For Col (zero-index): ")

                    valid_input = validate_input(self.board.get_board(), _x, _y)

                    if not valid_input:
                        print("INVALID INPUT. PLEASE RE-ENTER.")

                print("Your input is (%s, %s)" % (_x, _y))

                # Update the board.
                coordinate = (int(_x), int(_y))
                self.board.set_board(coordinate[0], coordinate[1], "X")  # User always takes O

            # Print the board
            print("CURRENT BOARD: ")
            print(self.board)

            # Update who's turn it is.
            self.is_user_turn = not self.is_user_turn

            self.winner = get_winner(self.board.get_board())  # X, O, DRAW, None

            print("---------------------------------------")

        if self.winner == "DRAW":
            print("GAME OVER. DRAW.")
        else:
            print("GAME OVER. " + self.winner + " WINS.")

        Log(self).log()

        print(GlobalRank())


class TwoPlayerModeGame(Game):
    def __init__(self):
        super().__init__()
        self.current_player = "X"

    def game_interface(self):
        while self.winner is None:
            print(self.current_player + " take a turn!")

            # Show the board to the user.
            print("CURRENT BOARD: ")
            print(self.board)

            # Input a move from the player.
            valid_input = False
            _x, _y = "", ""

            while not valid_input:
                _x = input("Enter Coordinate For Row (zero-index): ")
                _y = input("Enter Coordinate For Col (zero-index): ")

                valid_input = validate_input(self.board.get_board(), _x, _y)

                if not valid_input:
                    print("INVALID INPUT. PLEASE RE-ENTER.")

            print("Your input is (%s, %s)" % (_x, _y))

            # Update the board.
            coordinate = (int(_x), int(_y))
            self.board.set_board(coordinate[0], coordinate[1], self.current_player)

            # Print the board
            print("CURRENT BOARD: ")
            print(self.board)

            # Update who's turn it is.
            self.current_player = other_player(self.current_player)

            self.winner = get_winner(self.board.get_board())

            print("---------------------------------------")

        if self.winner == "DRAW":
            print("GAME OVER. DRAW.")
        else:
            print("GAME OVER. " + self.winner + " WINS.")

        Log(self).log()

        print(GlobalRank())
