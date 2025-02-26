import random


"""Module to generate a random number and print a greeting.

This module contains a single function, greet(), which generates a random
number between 1 and 100 and prints a greeting message including the
random number.
"""
def greet():
    """Generates a random number and prints a greeting message.

    This function generates a random integer between 1 and 100 (inclusive)
and prints a greeting message in the format "hello {random_number}",
where {random_number} is the generated random number.

    Returns:
        None. Prints a greeting message to the console.

    Raises:
        None.
    """
    random_number = random.randint(1, 100)
    print(f"hello {random_number}")


if __name__ == "__main__":
    greet()
