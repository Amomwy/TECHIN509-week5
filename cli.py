from typing import List
from logic import empty_board, other_player, get_winner


def print_board(board):
    """
    Print the board by rows and columns separating by blank space.
    """
    for i in range(3):
        current_row = ""
        for j in range(3):
            if board[i][j] is not None:
                current_row += board[i][j]
            else:
                current_row += "_"

            current_row += " "

        print(current_row)


def validate_input(board: List[List[str]], user_input_x: str, user_input_y: str) -> bool:
    """
    Validate the user's input coordinate of x and y.
    """
    try:
        x_coordinate = int(user_input_x)
    except ValueError:
        return False

    try:
        y_coordinate = int(user_input_y)
    except ValueError:
        return False

    return 0 <= x_coordinate <= 2 and 0 <= y_coordinate <= 2 and board[x_coordinate][y_coordinate] is None


if __name__ == '__main__':
    board = empty_board()
    winner = None
    current_player = "X"

    while winner is None:
        print(current_player + " take a turn!")

        # Show the board.
        print("CURRENT BOARD: ")
        print_board(board)

        valid_input = False
        _x, _y = "", ""

        while not valid_input:
            _x = input("Enter Coordinate For Row (zero-index): ")
            _y = input("Enter Coordinate For Col (zero-index): ")

            valid_input = validate_input(board, _x, _y)

            if not valid_input:
                print("INVALID INPUT. PLEASE RE-ENTER.")

        print("Your input is (%s, %s)" % (_x, _y))

        # Update the board.
        coordinate = (int(_x), int(_y))
        board[coordinate[0]][coordinate[1]] = current_player

        # Print the board
        print("CURRENT BOARD: ")
        print_board(board)

        current_player = other_player(current_player)

        winner = get_winner(board)

        print("---------------------------------------")

    if winner is not None:
        print("GAME OVER. " + winner + " WIN!")
    else:
        print("GAME OVER. DRAW.")