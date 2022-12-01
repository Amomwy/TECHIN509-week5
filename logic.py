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

    return None


def other_player(player):
    return "O" if player == "X" else "X"
