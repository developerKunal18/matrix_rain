# Matrix Rain

A small Python script that displays a "Matrix"-style falling characters animation in your terminal, inspired by the classic hacker/PC aesthetic.

## Features
- Column-based vertical "rain" with colored head and dimmer tails
- Adapts to terminal size and handles resizing
- Hides the cursor while running and restores it on exit
- Occasional words/phrases appear as characters

## Requirements
- Python 3.8+
- `colorama` for Windows terminal color support

Install dependencies:

```powershell
python -m pip install -r .\requirements.txt
```

## Run

```powershell
python .\matrix_rain.py
```

Press `Ctrl+C` to stop; the cursor will be restored.

## Configuration
- Edit `SPEED` in `matrix_rain.py` to adjust animation speed.
- Tweak `START_PROBABILITY` to change drop density.

## Contributing
Pull requests are welcome. Open an issue for feature requests or bugs.

## License
This project is provided as-is. Add a license file if you plan to publish publicly.

