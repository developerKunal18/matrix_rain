import os
import random
import time
import shutil
import sys
from colorama import Fore, Style, init

# Initialize colorama for Windows terminal color support
init(autoreset=True)

# Settings
PHRASES = ["KUNAL", "PYTHON", "CODE", "MATRIX", "AI", "DEVELOPER", "FUTURE"]
SPEED = 0.05  # Time delay between frames (seconds)
DEFAULT_WIDTH = 100   # Fallback characters per line
START_PROBABILITY = 0.02  # probability a column starts a new drop each frame

def get_terminal_size():
    """Return (columns, rows) of the terminal or sensible defaults."""
    try:
        size = shutil.get_terminal_size()
        return size.columns, size.lines
    except Exception:
        return DEFAULT_WIDTH, 24

def get_random_symbol():
    """Return a random symbol or an occasional phrase."""
    if random.random() < 0.06:
        return random.choice(PHRASES)
    return chr(random.randint(33, 126))

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def hide_cursor():
    sys.stdout.write('\033[?25l')
    sys.stdout.flush()

def show_cursor():
    sys.stdout.write('\033[?25h')
    sys.stdout.flush()

def matrix_rain():
    """Vertical Matrix-style rain animation (columns of falling characters)."""
    cols, rows = get_terminal_size()
    # Keep at least a small margin
    cols = max(10, cols)
    rows = max(10, rows - 1)

    # Each column maintains its head position, length, and active state
    columns = []
    for _ in range(cols):
        columns.append({
            'active': False,
            'head': random.randint(-rows, 0),
            'length': random.randint(4, max(6, rows // 4)),
        })

    print(Fore.GREEN + Style.BRIGHT + "Starting Matrix Rain... (Ctrl+C to stop)")
    time.sleep(0.6)
    try:
        hide_cursor()
        while True:
            # Recompute size occasionally to handle resize
            term_cols, term_rows = get_terminal_size()
            if term_cols != cols or term_rows - 1 != rows:
                cols = max(10, term_cols)
                rows = max(10, term_rows - 1)
                # Reinitialize columns to new width preserving existing state approximately
                new_columns = []
                for i in range(cols):
                    if i < len(columns):
                        new_columns.append(columns[i])
                    else:
                        new_columns.append({'active': False, 'head': random.randint(-rows, 0), 'length': random.randint(4, max(6, rows // 4))})
                columns = new_columns

            # create empty frame buffer
            frame = [[(' ', '')] * cols for _ in range(rows)]

            # update each column
            for x in range(cols):
                col = columns[x]
                # chance to start new drop
                if not col['active'] and random.random() < START_PROBABILITY:
                    col['active'] = True
                    col['head'] = 0
                    col['length'] = random.randint(4, max(6, rows // 4))

                if col['active']:
                    head = col['head']
                    length = col['length']
                    # draw drop body
                    for t in range(length):
                        y = head - t
                        if 0 <= y < rows:
                            # Determine color: head bright white, next bright green, tail dimmer
                            if t == 0:
                                color = Fore.WHITE + Style.BRIGHT
                            elif t == 1:
                                color = Fore.LIGHTGREEN_EX + Style.BRIGHT
                            else:
                                color = Fore.GREEN
                            ch = get_random_symbol()
                            # If phrase, pick a single char from it for columned appearance
                            if isinstance(ch, str) and len(ch) > 1:
                                ch = ch[random.randint(0, len(ch)-1)]
                            frame[y][x] = (ch, color)

                    col['head'] += 1
                    # deactivate when the tail passed the screen
                    if col['head'] - col['length'] > rows:
                        col['active'] = False

            # Render frame: join each row's colored characters
            clear_screen()
            for y in range(rows):
                row_chars = []
                for x in range(cols):
                    ch, color = frame[y][x]
                    if ch == ' ':
                        row_chars.append(' ')
                    else:
                        row_chars.append(color + ch + Style.RESET_ALL)
                print(''.join(row_chars))

            time.sleep(SPEED)
    except KeyboardInterrupt:
        pass
    finally:
        show_cursor()
        print(Fore.CYAN + "\nMatrix Rain Interrupted. Goodbye 👋")

if __name__ == "__main__":
    matrix_rain()
