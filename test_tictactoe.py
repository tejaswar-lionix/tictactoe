import unittest

from tictactoe import (
    available_moves,
    best_move,
    is_draw,
    new_board,
    play,
    winner,
)


class TicTacToeTests(unittest.TestCase):
    def test_new_board(self):
        self.assertEqual(new_board(), [" "] * 9)

    def test_winner_rows_columns_and_diagonals(self):
        board = ["X", "X", "X", "O", "O", " ", " ", " ", " "]
        self.assertEqual(winner(board), "X")
        board = ["O", "X", " ", "O", "X", " ", "O", " ", " "]
        self.assertEqual(winner(board), "O")
        board = ["X", "O", " ", " ", "X", "O", " ", " ", "X"]
        self.assertEqual(winner(board), "X")

    def test_no_winner(self):
        self.assertIsNone(winner(new_board()))

    def test_is_draw(self):
        board = ["X", "O", "X", "X", "O", "O", "O", "X", "X"]
        self.assertTrue(is_draw(board))

    def test_play_validates_moves(self):
        board = new_board()
        play(board, 0, "X")
        with self.assertRaises(ValueError):
            play(board, 0, "O")
        with self.assertRaises(ValueError):
            play(board, 9, "O")
        with self.assertRaises(ValueError):
            play(board, 1, "Z")

    def test_available_moves(self):
        board = play(new_board(), 4, "X")
        self.assertEqual(len(available_moves(board)), 8)

    def test_best_move_takes_win(self):
        board = ["X", "X", " ", "O", "O", " ", " ", " ", " "]
        self.assertEqual(best_move(board, "X"), 2)

    def test_best_move_blocks_opponent(self):
        board = ["X", "X", " ", "O", " ", " ", " ", " ", " "]
        self.assertEqual(best_move(board, "O"), 2)

    def test_best_move_does_not_mutate_board(self):
        board = ["X", "X", " ", "O", " ", " ", " ", " ", " "]
        before = list(board)
        best_move(board, "O")
        self.assertEqual(board, before)

    def test_best_move_alpha_beta_keeps_win_block_and_board(self):
        winning_board = ["X", "X", " ", "O", "O", " ", " ", " ", " "]
        self.assertEqual(best_move(winning_board, "X"), 2)
        blocking_board = ["X", "X", " ", "O", " ", " ", " ", " ", " "]
        before = list(blocking_board)
        self.assertEqual(best_move(blocking_board, "O"), 2)
        self.assertEqual(blocking_board, before)

    def test_best_move_empty_board_picks_center_or_corner(self):
        board = new_board()
        self.assertIn(best_move(board, "X"), (0, 2, 4, 6, 8))


class ReplayTests(unittest.TestCase):
    def test_empty_list_returns_new_board(self):
        from tictactoe import replay

        self.assertEqual(replay([]), new_board())

    def test_sequence_produces_expected_board(self):
        from tictactoe import replay

        board = replay([4, 0, 8, 2, 6])
        self.assertEqual(
            board,
            ["O", " ", "O", " ", "X", " ", "X", " ", "X"],
        )

    def test_custom_first_mark(self):
        from tictactoe import replay

        self.assertEqual(replay([0], first="O")[0], "O")

    def test_occupied_move_raises(self):
        from tictactoe import replay

        with self.assertRaises(ValueError):
            replay([0, 0])

    def test_out_of_range_raises(self):
        from tictactoe import replay

        with self.assertRaises(ValueError):
            replay([9])


class RenderTests(unittest.TestCase):
    def test_render_board(self):
        from tictactoe import render_board

        board = ["X", " ", "O", " ", "X", " ", " ", " ", "O"]
        rendered = render_board(board)
        lines = rendered.splitlines()
        self.assertEqual(len(lines), 5)
        self.assertEqual(lines[0], " X |   | O")
        self.assertEqual(lines[1], "---+---+---")

    def test_render_rejects_bad_board(self):
        from tictactoe import render_board

        with self.assertRaises(ValueError):
            render_board(["X"])


if __name__ == "__main__":
    unittest.main()
