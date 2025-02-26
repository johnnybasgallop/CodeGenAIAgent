
"""Module docstring: This module defines a Counter class and demonstrates its usage."""

class Counter:
    """Class docstring: Represents a counter with increment, decrement, reset, and multiplication functionalities.

    Attributes:
        count (int): The current value of the counter.
        step (int): The increment/decrement step.
        history (list): A list storing the history of counter values.
    """
    def __init__(self, start=0, step=1):
        """Constructor for the Counter class.

        Args:
            start (int, optional): The starting value of the counter. Defaults to 0.
            step (int, optional): The increment/decrement step. Defaults to 1.

        Raises:
            ValueError: If the step is zero.
        """
        if step == 0:
            raise ValueError("Step cannot be zero")
        self.count = start
        self.step = step
        self.history = [start]

    def increment(self):
        """Increments the counter by the step value.

        Returns:
            None
        """
        self.count += self.step
        self.history.append(self.count)


    def decrement(self):
        """Decrements the counter by the step value.

        Returns:
            None
        """

        self.count -= self.step
        self.history.append(self.count)


    def reset(self, to_value=0):
        """Resets the counter to a specified value.

        Args:
            to_value (int, optional): The value to reset the counter to. Defaults to 0.

        Returns:
            None
        """

        self.count = to_value
        self.history = [to_value]

    def get_value(self):
        """Returns the current value of the counter.

        Returns:
            int: The current value of the counter.
        """

        return self.count

    def set_step(self, new_step):
        """Sets a new step value for the counter.

        Args:
            new_step (int or float): The new step value.

        Raises:
            ValueError: If the new step is zero or not a number.
        """
        if not isinstance(new_step, (int, float)):
            raise ValueError("Step must be a number")
        if new_step == 0:
            raise ValueError("Step cannot be zero")

        self.step = new_step


    def multiply(self, factor):
        """Multiplies the counter's value by a given factor.

        Args:
            factor (int or float): The factor to multiply the counter by.

        Raises:
            ValueError: If the factor is not a number.
        """
        if not isinstance(factor, (int, float)):
          raise ValueError("Multiplication factor must be numeric")
        self.count *= factor
        self.history.append(self.count)

    def get_history(self):
        """Returns the history of the counter's values.

        Returns:
            list: A list containing the history of counter values.
        """

        return self.history

def main():
    """Main function to demonstrate the Counter class."""
    my_counter = Counter(5, 2)
    print(my_counter.get_value())
    my_counter.increment()
    print(my_counter.get_value())
    my_counter.decrement()
    print(my_counter.get_value())
    my_counter.reset()
    print(my_counter.get_value())
    another_counter = Counter()
    print(another_counter.get_value())
    another_counter.set_step(5)
    another_counter.increment()
    print(another_counter.get_value())
    my_counter.multiply(3)
    print(my_counter.get_value())
    print(my_counter.get_history())
    another_counter.reset(10)
    print(another_counter.get_history())
    try:
        another_counter.set_step("abc")
    except ValueError as e:
        print(f"Error: {e}")

    try:
        another_counter.set_step(0)
    except ValueError as e:
        print(f"Error: {e}")

    try:
      another_counter.multiply("hello")
    except ValueError as e:
        print(f"Error: {e}")
    print(another_counter.get_value())

if __name__ == "__main__":
    main()
