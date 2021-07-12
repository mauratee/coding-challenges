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

    # if txt parameter empty, return empty string
    if not txt:
        return ""

    # create lists of upper and lower case letters
    alpha_lower = "abcdefghijklmnopqrstuvwxyz"
    alpha_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    # create empty dictionaries to assign num value to each upper
    # and lower case letter
    alpha_lower_dict = {}
    alpha_upper_dict = {}

    # loop over lower case letter list and add letter and unique number value to empty dict
    i = 1
    for char in alpha_lower:
        alpha_lower_dict[char] = i
        i += 1

    # loop over upper case letter list and add letter and unique number vlaue to empty dict
    i = 1
    for char in alpha_upper:
        alpha_upper_dict[char] = i
        i += 1
    
    # print(alpha_lower_dict)
    # print(alpha_upper_dict)

    # variable to capture txt after shifting
    shifted_txt = ""
    
    # loop over each character of txt parameter
    for char in txt:
        # check if character in alpha lower, if so retrieve associated 
        # value from dict and add shift from parameter
        if char in alpha_lower:
            val = alpha_lower_dict[char]
            shift_val = val + shift
            # if we're at the end of the alphabet, loop back to beginning
            if shift_val > 26:
                shift_val = shift_val - 26
            # unpack each letter and value in dict, look for value that
            # matches shifted value
            for letter, value in alpha_lower_dict.items():
                # if matching value found, assign new char to shifted_val key
                # and append new char to shifted txt
                if value == shift_val:
                    new_char = letter
                    shifted_txt = shifted_txt + new_char
        # check if character in alpha upper, if so follow same process as above
        elif char in alpha_upper:
            val = alpha_upper_dict[char]
            shift_val = val + shift
            if shift_val > 26:
                shift_val = shift_val - 26
            for letter, value in alpha_upper_dict.items():
                if value == shift_val:
                    new_char = letter
                    shifted_txt = shifted_txt + new_char
        # if character non-alpha, append to shifted txt as is
        else:
            shifted_txt = shifted_txt + char

    
    return shifted_txt





if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')
