"""Write a function that encrypts a string with a variable rotary cipher.

The function should take in a number and string and shift the string's
characters by that number:

>>> rot_encode(1, 'abcxyz')
'bcdyza'

It should be able to shift characters by any number:

>>> rot_encode(3, 'abcxyz')
'defabc'

It should preserve capitalization, whitespace, and any special characters:

>>> rot_encode(1, 'Wow! This is 100% amazing.')
'Xpx! Uijt jt 100% bnbajoh.'
"""


def rot_encode(shift, txt):
    """Encode `txt` by shifting its characters to the right."""

    # if not txt:
        # return ''

    alpha_lower = "abcdefghijklmnopqrstuvwxyz"
    alpha_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alpha_lower_dict = {}
    alpha_upper_dict = {}

    i = 1
    for char in alpha_lower:
        alpha_lower_dict[char] = i
        i += 1

    i = 1
    for char in alpha_upper:
        alpha_upper_dict[char] = i
        i += 1
    
    print(alpha_lower_dict)
    print(alpha_upper_dict)





if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')
