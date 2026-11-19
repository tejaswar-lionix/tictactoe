#!/usr/bin/env python3
"""Tic-tac-toe rules and an unbeatable minimax opponent."""
WIN_LINES = (
    (0, 1, 2), (3, 4, 5), (6, 7, 8),
    (0, 3, 6), (1, 4, 7), (2, 5, 8),
    (0, 4, 8), (2, 4, 6),
)


def new_board():
    return [" "] * 9


def validate(board):
    if len(board) != 9:
        raise ValueError("board must have 9 cells")
    if any(cell not in (" ", "X", "O") for cell in board):
        raise ValueError("cells must be space, X, or O")
    return board


def winner(board):
    validate(board)
    for first, second, third in WIN_LINES:
        if board[first] != " " and board[first] == board[second] == board[third]:
            return board[first]
    return None


def winner_line(board):
    validate(board)
    for line in WIN_LINES:
        first, second, third = line
        if board[first] != " " and board[first] == board[second] == board[third]:
            return line
    return None


def evaluate(board, mark):
    validate(board)
    if mark not in ("X", "O"):
        raise ValueError("mark must be X or O")
    opponent = "O" if mark == "X" else "X"
    score = 0
    for first, second, third in WIN_LINES:
        cells = (board[first], board[second], board[third])
        if cells == (mark, mark, mark):
            score += 10
        elif cells == (opponent, opponent, opponent):
            score -= 10
    return score


def is_draw(board):
    return winner(board) is None and all(cell != " " for cell in board)


def available_moves(board):
    validate(board)
    return [index for index, cell in enumerate(board) if cell == " "]


def play(board, index, mark):
    validate(board)
    if mark not in ("X", "O"):
        raise ValueError("mark must be X or O")
    if not 0 <= index < 9:
        raise ValueError("index must be between 0 and 8")
    if board[index] != " ":
        raise ValueError("cell is already taken")
    board[index] = mark
    return board


def replay(moves, first="X"):
    """Replay a sequence of move indices starting with the given mark."""
    if first not in ("X", "O"):
        raise ValueError("first must be X or O")
    board = new_board()
    mark = first
    for index in moves:
        play(board, index, mark)
        mark = "O" if mark == "X" else "X"
    return board


def best_move(board, mark):
    validate(board)
    if mark not in ("X", "O"):
        raise ValueError("mark must be X or O")
    opponent = "O" if mark == "X" else "X"

    def minimax(state, current, alpha, beta):
        win = winner(state)
        if win == mark:
            return 1
        if win == opponent:
            return -1
        if all(cell != " " for cell in state):
            return 0
        if current == mark:
            score = -2
            for move in available_moves(state):
                state[move] = current
                score = max(score, minimax(state, opponent, alpha, beta))
                state[move] = " "
                alpha = max(alpha, score)
                if alpha >= beta:
                    break
            return score
        score = 2
        for move in available_moves(state):
            state[move] = current
            score = min(score, minimax(state, mark, alpha, beta))
            state[move] = " "
            beta = min(beta, score)
            if alpha >= beta:
                break
        return score

    best_score = -2
    best_index = None
    for move in available_moves(board):
        board[move] = mark
        score = minimax(board, opponent, -2, 2)
        board[move] = " "
        if score > best_score:
            best_score = score
            best_index = move
    return best_index


def render_board(board):
    """Render the board as a three-row text grid."""
    validate(board)
    rows = []
    for start in range(0, 9, 3):
        rows.append(" " + " | ".join(board[start:start + 3]))
        if start < 6:
            rows.append("---+---+---")
    return "\n".join(rows)
