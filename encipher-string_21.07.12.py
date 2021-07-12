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

    if not txt:
        return ""

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
    
    # print(alpha_lower_dict)
    # print(alpha_upper_dict)

    shifted_txt = ""

    for char in txt:
        if char in alpha_lower:
            val = alpha_lower_dict[char]
            shift_val = val + shift
            if shift_val > 26:
                shift_val = shift_val - 26
            for letter, value in alpha_lower_dict.items():
                if value == shift_val:
                    new_char = letter
                    shifted_txt = shifted_txt + new_char
    
    return shifted_txt





if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')
