# tictactoe

Tic-tac-toe rules with an unbeatable minimax opponent.

## Usage

```bash
python3 -c "from tictactoe import *; b=new_board(); play(b, 4, 'X'); print(render_board(b))"
python3 -c "from tictactoe import *; print(replay([4, 0, 8, 2, 6]))"
python3 -c "from tictactoe import *; print(winner_line(replay([0, 3, 1, 4, 2])))"
python3 -c "from tictactoe import *; print(evaluate(['X', 'X', 'X', 'O', 'O', ' ', ' ', ' ', ' '], 'X'))"
```

## Features

- Win, draw, and move validation
- Unbeatable minimax opponent with alpha-beta pruning
- Text board rendering with render_board(board)
- Replay move sequences with replay(moves, first)
- Winning line lookup with winner_line(board)
- Heuristic scoring with evaluate(board, mark)

## Tests

```bash
python3 -m unittest -q
```

## Additional API

- `from_text(text)` parses a nine-cell board string, treating `.`, `-`, and `_` as empty cells.

## License

MIT
