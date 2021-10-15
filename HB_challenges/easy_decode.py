"""Decode a string.

A valid code is a sequence of numbers and letter, always starting with a number
and ending with letter(s).

Each number tells you how many characters to skip before finding a good letter.
After each good letter should come the next next number.

For example, the string "hey" could be encoded by "0h1ae2bcy". This means
"skip 0, find the 'h', skip 1, find the 'e', skip 2, find the 'y'".

A single letter should work::

    >>> decode("h0")
    'h'

    >>> decode("2abh")
    'h'

Longer patterns should work::

    >>> decode("0h1ae2bcy")
    'hey'
"""


def decode(s):
    """Decode a string."""

    decoded = ""
    idx = 0

    while idx < len(s):
        
        if int(s[idx]) + 1 <= len(s):
            # print(idx)
            # print(int(s[idx]) + 1)
            decoded = decoded + s[idx + int(s[idx]) + 1]
            idx = idx + int(s[idx]) + 2
            # print(f"idx = {idx}")


    return decoded


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED; 0G1ar0e1ba0t2ab! ***\n")
