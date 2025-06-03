#! /usr/bin/env python3

"""
Get user input and error handling
"""

def get_value(prompt, lower=None, upper=None, convert_type=str):
    while True:
        value = input(prompt)
        if convert_type == str:
            return value
        try:
            value = convert_type(value)
            if lower is not None and value <= lower:
                if upper is not None and upper <= lower:
                    error = f"Illegal argument: lower = {lower}. " \
                            f"Lower must be lower than {upper}."
                    print(error)
                    return None
                error = f"Illegal argument: value = {value}. " \
                        f"Entered value must be higher than {lower}."
                print(error)
            elif upper is not None and value >= upper:
                if lower is not None and upper <=lower:
                    error = f"Illegal argument: upper = {upper}. " \
                            f"Upper must be higher than {lower}."
                    print(error)
                    return None
                error = f"Illegal argument: value = {value}. " \
                        f"Entered value must be lower than {upper}."
                print(error)
            else:
                return value
        except ValueError:
            error = f"Illegal argument: value = {value}. " \
                    f"Entered value must be of type:  \n {convert_type.__doc__}."
            print(error)


def main():
    prompt = "Enter value:\t"
    value = get_value(prompt, convert_type=int)
    print(f"Value = {value}.")


if __name__ == "__main__":
    main()
