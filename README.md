# tictactoe

Tic-tac-toe rules with an unbeatable minimax opponent.

## Usage

```bash
python3 -c "from tictactoe import *; b=new_board(); play(b, 4, 'X'); print(render_board(b))"
```

## Features

- Win, draw, and move validation
- Unbeatable minimax opponent with alpha-beta pruning
- Text board rendering with render_board(board)

## Tests

```bash
python3 -m unittest -q
```

## License

MIT
