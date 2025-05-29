#!/usr/bin/env python


"""
Prompt the user for an integer input with limited retries.

Parameters
----------
prompt : str
    The message displayed to the user.
attempts : int, optional
    Number of attempts allowed before failing (default is 3).
error_msg : str, optional
    Message to display on invalid input (default is "Illegal argument").

Returns
-------
int
    The valid integer entered by the user.

Raises
------
ValueError
    If the maximum number of attempts is exceeded without valid input.
"""


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

    try:
        min_n = get_value(prompt="Enter the minimum desired value for your range: ", lower=1-1, convert_type=int)
        max_n = get_value(prompt="Enter the maximum desired value for your range: ", lower=1-1, convert_type=int)
    except ValueError as e:
        print(e)
        return

    display_chart(min_n, max_n)
    print_border()


if __name__ == "__main__":
    main()
