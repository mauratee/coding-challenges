"""Calculator

    >>> calc("+ 1 2")  # 1 + 2
    3

    >>> calc("* 2 + 1 2")  # 2 * (1 + 2)
    6

    >>> calc("+ 9 * 2 3")   # 9 + (2 * 3)
    15

Let's make sure we have non-commutative operators working:

    >>> calc("- 1 2")  # 1 - 2
    -1

    >>> calc("- 9 * 2 3")  # 9 - (2 * 3)
    3

    >>> calc("/ 6 - 4 2")  # 6 / (4 - 2)
    3
"""


def calc(s):
    """Evaluate expression."""
    operators = {"+": "add", "-": "sub", "*": "mul", "/": "div"}

    expression = s.split(" ")
    # print(expression)

    int_stack = []
    to_compute = 0

    # while expression[-1] not in operators:
    #     int_stack.append(expression.pop())

    # print(int_stack)

    while expression:
        # print(expression)
        if expression[-1] not in operators:
            int_stack.append(expression.pop())
            # print(int_stack)
        else:
            operator = expression.pop()
            # print(operator)
            to_compute = int(int_stack.pop())
            # print(to_compute)
            num_2 = int(int_stack.pop())
            # print(to_compute)
            to_compute = eval(f"{to_compute} {operator} {num_2}")
            # to_compute = operators[expression.pop()] int(int_stack.pop())
            # print(to_compute)
            int_stack.append(to_compute)
    
    return int(to_compute)
        




if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED; WELL-CALCULATED! ***\n")
