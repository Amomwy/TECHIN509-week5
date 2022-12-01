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


def board_is_filled(board):
    filled_num = 0

    for i in range(3):
        for j in range(3):
            if board[i][j] is not None:
                filled_num += 1

    return filled_num == 9


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

    # Otherwise let the game continue, or draw
    return None if not board_is_filled(board) else "DRAW"


def other_player(player):
    """Given the character for a player, returns the other player."""
    return "O" if player == "X" else "X"


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
