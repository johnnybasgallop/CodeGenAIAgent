class MathOperations:
    def __init__(self, base: float):
        self.base = base

    def add(self, value: float) -> float:
        return self.base + value

    def multiply(self, factor: float) -> float:
        return self.base * factor


def process_numbers(numbers: list, operation: str = 'sum') -> float:
    if operation == 'sum':
        return sum(numbers)
    elif operation == 'average':
        return sum(numbers) / len(numbers)
    else:
        raise ValueError("Unsupported operation")


def main():
    math_op = MathOperations(10)
    result1 = math_op.add(5)
    result2 = math_op.multiply(3)
    processed = process_numbers([result1, result2], operation='sum')
    print("Add:", result1)
    print("Multiply:", result2)
    print("Processed:", processed)


if __name__ == "__main__":
    main()
