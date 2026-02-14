"""Advanced UI module with themes and styling"""
import sys
import time
try:
    from colorama import Fore, Back, Style, init
    init(autoreset=True)
    COLORS = True
except ImportError:
    COLORS = False
    class Fore:
        BLACK = RED = GREEN = YELLOW = BLUE = MAGENTA = CYAN = WHITE = LIGHTBLACK_EX = LIGHTRED_EX = LIGHTGREEN_EX = LIGHTYELLOW_EX = LIGHTBLUE_EX = LIGHTMAGENTA_EX = LIGHTCYAN_EX = LIGHTWHITE_EX = RESET = ''
    class Back:
        BLACK = RED = GREEN = YELLOW = BLUE = MAGENTA = CYAN = WHITE = RESET = ''
    class Style:
        BRIGHT = DIM = NORMAL = RESET_ALL = ''

THEMES = {
    'default': {
        'primary': Fore.CYAN,
        'secondary': Fore.YELLOW,
        'success': Fore.GREEN,
        'error': Fore.RED,
        'info': Fore.BLUE,
        'accent': Fore.MAGENTA
    },
    'dark': {
        'primary': Fore.LIGHTBLUE_EX,
        'secondary': Fore.LIGHTYELLOW_EX,
        'success': Fore.LIGHTGREEN_EX,
        'error': Fore.LIGHTRED_EX,
        'info': Fore.LIGHTCYAN_EX,
        'accent': Fore.LIGHTMAGENTA_EX
    },
    'matrix': {
        'primary': Fore.GREEN,
        'secondary': Fore.LIGHTGREEN_EX,
        'success': Fore.WHITE,
        'error': Fore.RED,
        'info': Fore.GREEN,
        'accent': Fore.LIGHTGREEN_EX
    }
}

current_theme = 'default'

def set_theme(theme_name):
    """Set UI theme"""
    global current_theme
    if theme_name in THEMES:
        current_theme = theme_name
        return True
    return False

def get_color(color_type):
    """Get color from current theme"""
    if not COLORS:
        return ''
    return THEMES[current_theme].get(color_type, '')

def print_banner():
    """Print animated banner"""
    banner = [
        "  ╔═══════════════════════════════════════════════════════════════════════════╗",
        "  ║                                                                           ║",
        "  ║        ███████╗ ██████╗██╗███████╗███╗   ██╗████████╗██╗███████╗██╗      ║",
        "  ║        ██╔════╝██╔════╝██║██╔════╝████╗  ██║╚══██╔══╝██║██╔════╝██║      ║",
        "  ║        ███████╗██║     ██║█████╗  ██╔██╗ ██║   ██║   ██║█████╗  ██║      ║",
        "  ║        ╚════██║██║     ██║██╔══╝  ██║╚██╗██║   ██║   ██║██╔══╝  ██║      ║",
        "  ║        ███████║╚██████╗██║███████╗██║ ╚████║   ██║   ██║██║     ██║      ║",
        "  ║        ╚══════╝ ╚═════╝╚═╝╚══════╝╚═╝  ╚═══╝   ╚═╝   ╚═╝╚═╝     ╚═╝      ║",
        "  ║                                                                           ║",
        "  ║              ██████╗ █████╗ ██╗      ██████╗██╗   ██╗██╗      █████╗     ║",
        "  ║             ██╔════╝██╔══██╗██║     ██╔════╝██║   ██║██║     ██╔══██╗    ║",
        "  ║             ██║     ███████║██║     ██║     ██║   ██║██║     ███████║    ║",
        "  ║             ██║     ██╔══██║██║     ██║     ██║   ██║██║     ██╔══██║    ║",
        "  ║             ╚██████╗██║  ██║███████╗╚██████╗╚██████╔╝███████╗██║  ██║    ║",
        "  ║              ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝    ║",
        "  ║                                                                           ║",
        "  ║                    PROFESSIONAL EDITION v4.0 - ULTIMATE                  ║",
        "  ║                                                                           ║",
        "  ╚═══════════════════════════════════════════════════════════════════════════╝"
    ]
    
    primary = get_color('primary')
    accent = get_color('accent')
    
    for line in banner:
        if COLORS:
            print(f"{primary}{Style.BRIGHT}{line}{Style.RESET_ALL}")
        else:
            print(line)
        time.sleep(0.03)

def print_box(title, content, width=80, color='primary'):
    """Print content in a styled box"""
    c = get_color(color)
    print(f"\n{c}{'='*width}")
    print(f"{Style.BRIGHT if COLORS else ''}{title.center(width)}{Style.RESET_ALL if COLORS else ''}")
    print(f"{'='*width}{Style.RESET_ALL if COLORS else ''}")
    for line in content:
        print(f"{c}{line}{Style.RESET_ALL if COLORS else ''}")
    print(f"{c}{'='*width}{Style.RESET_ALL if COLORS else ''}")

def print_table(headers, rows, title=""):
    """Print data in table format"""
    col_widths = [max(len(str(row[i])) for row in [headers] + rows) + 2 for i in range(len(headers))]
    total_width = sum(col_widths) + len(headers) + 1
    
    primary = get_color('primary')
    secondary = get_color('secondary')
    
    if title:
        print(f"\n{primary}{Style.BRIGHT if COLORS else ''}{title.center(total_width)}{Style.RESET_ALL if COLORS else ''}")
    
    print(f"{primary}+{'+'.join('-'*w for w in col_widths)}+{Style.RESET_ALL if COLORS else ''}")
    
    header_row = "|".join(f"{str(headers[i]).center(col_widths[i])}" for i in range(len(headers)))
    print(f"{primary}|{secondary}{Style.BRIGHT if COLORS else ''}{header_row}{Style.RESET_ALL if COLORS else ''}{primary}|{Style.RESET_ALL if COLORS else ''}")
    
    print(f"{primary}+{'+'.join('-'*w for w in col_widths)}+{Style.RESET_ALL if COLORS else ''}")
    
    for row in rows:
        row_str = "|".join(f"{str(row[i]).center(col_widths[i])}" for i in range(len(row)))
        print(f"{primary}|{row_str}|{Style.RESET_ALL if COLORS else ''}")
    
    print(f"{primary}+{'+'.join('-'*w for w in col_widths)}+{Style.RESET_ALL if COLORS else ''}")

def loading_animation(text="Processing", duration=1):
    """Show loading animation"""
    frames = ['|', '/', '-', '\\']
    end_time = time.time() + duration
    i = 0
    while time.time() < end_time:
        sys.stdout.write(f'\r{get_color("info")}{frames[i % len(frames)]} {text}...{Style.RESET_ALL if COLORS else ""}')
        sys.stdout.flush()
        time.sleep(0.1)
        i += 1
    sys.stdout.write('\r' + ' ' * 50 + '\r')
    sys.stdout.flush()

def progress_bar(current, total, prefix='Progress:', length=40):
    """Display progress bar"""
    percent = current / total
    filled = int(length * percent)
    bar = '#' * filled + '-' * (length - filled)
    print(f'\r{get_color("info")}{prefix} |{bar}| {percent*100:.1f}%{Style.RESET_ALL if COLORS else ""}', end='')
    if current == total:
        print()
