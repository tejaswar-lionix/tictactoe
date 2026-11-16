# tictactoe

Tic-tac-toe rules with an unbeatable minimax opponent.

## Usage

```bash
python3 -c "from tictactoe import *; b=new_board(); play(b, 4, 'X'); print(render_board(b))"
python3 -c "from tictactoe import *; print(replay([4, 0, 8, 2, 6]))"
```

## Features

- Win, draw, and move validation
- Unbeatable minimax opponent with alpha-beta pruning
- Text board rendering with render_board(board)
- Replay move sequences with replay(moves, first)

## Tests

```bash
python3 -m unittest -q
```

## License

MIT
