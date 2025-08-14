#!/usr/bin/env python


from .utils.get_value import get_value


# Constants
MAX_SUPPORTED_VALUE = 6.022e23


# Resource constant
RES = "resources"


# Helper functions
def print_splash():
    splash = r"""

                 ███╗   ██╗ ██████╗██╗  ██╗ █████╗ ██████╗ ████████╗
                 ████╗  ██║██╔════╝██║  ██║██╔══██╗██╔══██╗╚══██╔══╝
                 ██╔██╗ ██║██║     ███████║███████║██████╔╝   ██║   
                 ██║╚██╗██║██║     ██╔══██║██╔══██║██╔══██╗   ██║   
                 ██║ ╚████║╚██████╗██║  ██║██║  ██║██║  ██║   ██║   
                 ╚═╝  ╚═══╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   
                                                   


		                   N C H A R T
                              Terminal Numerics Tool
"""
    print(splash)


def print_border(char="=", width=80):
    """Prints a border of the given character and width."""
    print(char * width)


def print_header(title, width=80):
    """Prints a centered header with a border, supporting multi-line titles."""
    print_border()
    lines = title.split("\n")  # Split the title into multiple lines
    for line in lines:
        print(f"{line.center(width)}")  # Center each line
    print_border()


def print_author(title, width=80):
    """Prints author and release information"""
    print_border()
    print(f"{title.center(width)}")
    print_border()


# Define program resources
HEADER_1 = "header_1"
HEADER_2 = "header_2"
AUTHOR = "author"
MIN_N = "min_n"
MAX_N = "max_n"
TABLE_HEADER = "table_header"
INVISIBLE = "invisible"



resources = {
    RES: {
        HEADER_1: "Welcome to the NChart number Conversion Tool\nNumChart",
        HEADER_1: "Welcome to the NChart number Conversion Tool\nNumChart",
        HEADER_2: "Converts from Decimal into Binary, Octal, Hexadecimal, and Character formats!",
        AUTHOR: "Pavle Džakula, 2025, GPLv3",
        MIN_N: "Enter the minimum desired value for your range: ",
        MAX_N: "Enter the maximum desired value for your range: ",
        TABLE_HEADER: f"{'Decimal':>10s}\t{'Binary':>10s}\t{'Octal':>10s}\t{'Hexadecimal':>15s}\t     {'Character':>10s}",
        INVISIBLE: "Non-Visual",
    },
}


def get_valid_int(prompt, min_allowed=None, max_allowed=None):
    while True:
        try:
            return get_value(prompt, int, min_value=min_allowed, max_value=max_allowed)
        except ValueError:
            print(errors["illegal_argument"])


def generate_row(n):
    """Formats a single row of the chart."""
    binary = format(n, 'b')
    octal = format(n, 'o')
    hexa = format(n, 'x')
    ascii_char = chr(n) if chr(n).isprintable() else resources[RES][INVISIBLE]
    return f"{n:>10d}\t{binary:>10s}\t{octal:>10s}\t{hexa:>15s}\t     {ascii_char:>10s}"


def display_chart(min_n, max_n):
    """Displays formatted output between min and max."""
    # Print the table header
    print_border()	
    print(resources[RES][TABLE_HEADER])
    print_border()
    for n in range(min_n, max_n + 1):
        print(generate_row(n))


def show_headers():
    print_splash()
    print_header(resources[RES][HEADER_1], width=80)
    print_header(resources[RES][HEADER_2], width=80)
    print_author(resources[RES][AUTHOR])
    print_border()


def main():
    show_headers()
    def read_int(label: str, low: int | None = None, high: int | None = None) -> int:
        """Read an integer with 'q' to quit, range-check after conversion."""
        while True:
            raw = get_value(
                prompt=f"{label} (or 'q' to quit): ",
                convert_type=str
            ).strip().lower()

            if raw == "q":
                print("Goodbye!")
                raise SystemExit
            try:
                val = int(raw)
            except ValueError:
                print("Error: please enter an integer or 'q' to quit.")
                continue
            if low is not None and val < low:
                print(f"Out of range: expected ≥ {low}.")
                continue
            if high is not None and val > high:
                print(f"Out of range: expected ≤ {high}.")
                continue
            return val
    while True:
        min_n = read_int("Enter the minimum desired value for your range", low=0)
        max_n = read_int("Enter the maximum desired value for your range", low=min_n)
        display_chart(min_n, max_n)
        print_border()
        again = get_value(
            prompt="Press Enter to make another chart, or 'q' to quit:\t",
            convert_type=str
        ).strip().lower()
        if again == "q":
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
