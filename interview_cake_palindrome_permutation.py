import unittest


def has_palindrome_permutation(the_string):

    # Check if any permutation of the input is a palindrome
    
    # MY SOLUTION:
    if not the_string:
        return True
    
    string_dict = {}
    counter = 0
    
    for char in the_string:
        if char in string_dict:
            string_dict[char] += 1
        else:
            string_dict[char] = 1
    
    for value in string_dict.values():
        if value % 2 == 1:
            counter += 1
            
    if counter >= 2:
        return False
    
    return True


# INTERVIEW CAKE SOLUTION:
def has_palindrome_permutation(the_string):
    # Track characters we've seen an odd number of times
    unpaired_characters = set()

    for char in the_string:
        if char in unpaired_characters:
            unpaired_characters.remove(char)
        else:
            unpaired_characters.add(char)

    # The string has a palindrome permutation if it
    # has one or zero characters without a pair
    return len(unpaired_characters) <= 1









# Tests

class Test(unittest.TestCase):

    def test_permutation_with_odd_number_of_chars(self):
        result = has_palindrome_permutation('aabcbcd')
        self.assertTrue(result)

    def test_permutation_with_even_number_of_chars(self):
        result = has_palindrome_permutation('aabccbdd')
        self.assertTrue(result)

    def test_no_permutation_with_odd_number_of_chars(self):
        result = has_palindrome_permutation('aabcd')
        self.assertFalse(result)

    def test_no_permutation_with_even_number_of_chars(self):
        result = has_palindrome_permutation('aabbcd')
        self.assertFalse(result)

    def test_empty_string(self):
        result = has_palindrome_permutation('')
        self.assertTrue(result)

    def test_one_character_string(self):
        result = has_palindrome_permutation('a')
        self.assertTrue(result)


unittest.main(verbosity=2)