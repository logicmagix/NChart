#!/usr/bin/env python


# Constants
MAX_SUPPORTED_VALUE = 6.022e23  # Max limit constant

# Language constant
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
ERROR_INVALID_INPUT = "error_invalid_input"
EXIT_PROMPT = "exit_prompt"

resources = {
    RES: {
        HEADER_1: "Welcome to the NChart number Conversion Tool\nNumChart",
        HEADER_1: "Welcome to the NChart number Conversion Tool\nNumChart",
        HEADER_2: "Converts from Decimal into Binary, Octal, Hexadecimal, and Character formats!",
        AUTHOR: "Pavle Džakula, 2025, GPLv3",
        MIN_N: "Enter the minimum desired value for your range: ",
        MAX_N: "Enter the maximum desired value for your range: ",
        TABLE_HEADER: f"{'Decimal':>10s}\t{'Binary':>10s}\t{'Octal':>10s}\t{'Hexadecimal':>15s}\t{'Character':>10s}",
        INVISIBLE: "Non-Visual",
        ERROR_INVALID_INPUT: "Invalid input. Please try an integer.",
        EXIT_PROMPT: "Press Enter to exit...",
    },
}

def main():
    print_splash()
    print_header(resources[RES][HEADER_1], width=80)
    print_header(resources[RES][HEADER_2], width=80)
    print_author(resources[RES][AUTHOR])
    print_border()

    
    # Prompt user for the range
    while True:
        try:
            min_n = int(input(resources[RES][MIN_N]))
            break  # Exit the loop if input is valid
        except ValueError:
            print(resources[RES][ERROR_INVALID_INPUT])  # Localized error message
    
    while True:
        try:
            max_n = int(input(resources[RES][MAX_N]))
            break  # Exit the loop if input is valid
        except ValueError:
            print(resources[RES][ERROR_INVALID_INPUT])  # Localized error message
    
    # Clamp max_n to the supported maximum
    max_n = min(max_n, int(MAX_SUPPORTED_VALUE))
    
    # Print table header with a border
    print_border()
    print(resources[RES][TABLE_HEADER])
    print_border()
    
    # Generate and print the table
    for n in range(min_n, max_n + 1):
        binary = format(n, 'b')
        octal = format(n, 'o')
        hexa = format(n, 'x')
        ascii_char = chr(n) if chr(n).isprintable() else resources[RES][INVISIBLE]
        print(f"{n:>10d}\t{binary:>10s}\t{octal:>10s}\t{hexa:>15s}\t{ascii_char:>10s}")
    
    # End with a border
    print_border()
    input(resources[RES][EXIT_PROMPT])

if __name__ == "__main__":
    main()
