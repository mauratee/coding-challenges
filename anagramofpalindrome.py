"""Is the word an anagram of a palindrome?

A palindrome is a word that reads the same forward and backwards
(eg, "racecar", "tacocat"). An anagram is a rescrambling of a word
(eg for "racecar", you could rescramble this as "arceace").

Determine if the given word is a re-scrambling of a palindrome.
The word will only contain lowercase letters, a-z.

Examples::

    >>> is_anagram_of_palindrome("a")
    True

    >>> is_anagram_of_palindrome("ab")
    False

    >>> is_anagram_of_palindrome("aab")
    True

    >>> is_anagram_of_palindrome("arceace")
    True

    >>> is_anagram_of_palindrome("arceaceb")
    False

"""


def is_anagram_of_palindrome(word):
    """Is the word an anagram of a palindrome?"""
    # create dictionary
    word_dict = {}
    # for loop over each char in word:
    for char in word:
        # if char count not in dict:
        if word.count(char) not in word_dict:
            # add char count as key to dict
            word_dict[word.count(char)] = True
            # add True as value to dict
        # else:
        else:
            # if char count == 1:
            if word.count(char) == 1:
                # return False
                return False
            # if char count % 2 == 0:
                # continue
    
    return True


if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print("\n*** ALL TEST PASSED. AWESOMESAUCE!\n")
