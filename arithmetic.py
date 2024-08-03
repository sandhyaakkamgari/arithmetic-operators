def arithmetic_operations(num1, num2, operator):
    """
    Performs arithmetic operations on two numbers.

    Args:
        num1: The first number.
        num2: The second number.
        operator: The arithmetic operator (+, -, *, /).

    Returns:
        The result of the operation.
    """

    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            return "Division by zero not allowed!"
        else:
            return num1 / num2
    else:
        return "Invalid operator!"

# Example usage:
result = arithmetic_operations(15, 5, '+')
print(result)

result = arithmetic_operations(15, 5, '/')
print(result)