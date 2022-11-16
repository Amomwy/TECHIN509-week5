import random
from typing import Tuple
from typing import List

class Board:
    def __init__(self):
        self.board = [
            [None, None, None],
            [None, None, None],
            [None, None, None],
        ]

    def __str__(self):
        rows = ""
        for i in range(3):
            current_row = ""
            for j in range(3):
                if self.board[i][j] is not None:
                    current_row += self.board[i][j]
                else:
                    current_row += "_"

                current_row += " "

            rows += current_row + "\n"

        return rows

    def set_board(self, x: int, y: int, player: str):
        self.board[x][y] = player

    def get_board_element(self, i: int, j: int):
        return self.board[i][j]

    def get_board(self):
        return self.board

def empty_board():
    return [
        [None, None, None],
        [None, None, None],
        [None, None, None],
    ]

    
def get_winner(board):
   
    wins = [
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)],
    ]

    def check_win(S) -> bool:
        """
        Check if a set of a player's pieces leads to win.
        :param S: a set
        :return: True if the set can lead to win otherwise False
        """
        for win in wins:
            flag = True
            for pos in win:
                if pos not in S:
                    flag = False
                    break
            if flag:
                return True

        return False

    x_set, o_set = set(), set()

    for i in range(3):
        for j in range(3):
            if board[i][j] == "X":
                x_set.add((i, j))
                if check_win(x_set):
                    return "X"
            elif board[i][j] == "O":
                o_set.add((i, j))
                if check_win(o_set):
                    return "O"

    # Otherwise let the game continue
    return None


def other_player(player):
    """Given the character for a player, returns the other player."""
    return "O" if player == "X" else "X"


class Game:
    def __init__(self):
        self.game_mode = 0  # 1 means one-gamer (user vs bot), 2 means two-player (user vs user)
        self.board = Board()
        self.players = ["X", other_player("X")]
        self.winner = None

    def get_winner(self):
        return self.winner

    def game_interface(self):
        pass


def validate_game_mode_input(user_input: str) -> bool:
    try:
        game_mode = int(user_input)
    except ValueError:
        return False

    return game_mode == 1 or game_mode == 2
    
def validate_input(board: List[List[str]], user_input_x: str, user_input_y: str) -> bool:
    try:
        x_coordinate = int(user_input_x)
    except ValueError:
        return False

    try:
        y_coordinate = int(user_input_y)
    except ValueError:
        return False

    return 0 <= x_coordinate <= 2 and 0 <= y_coordinate <= 2 and board[x_coordinate][y_coordinate] is None


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

            self.winner = get_winner(self.board.get_board())

            print("---------------------------------------")

        if self.winner is not None:
            print("GAME OVER. " + self.winner + " WINS.")
        else:
            print("GAME OVER. DRAW.")


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

        if self.winner is not None:
            print("GAME OVER. " + self.winner + " WINS.")
        else:
            print("GAME OVER. DRAW.")