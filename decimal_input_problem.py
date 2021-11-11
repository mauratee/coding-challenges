import unittest

# define a function that returns True if an input string has 0 or 2 decimal places

# "100" -> True
# "1.1" -> False
# "Hello. I" -> False
# "-10" -> True
# "%^^^%.($" -> False
# "100.20" -> True


def isAmount(input):

    if not input:
        return False

    dec_idx = None

    for idx, char in enumerate(input):
        # print(char != ".")
        if not char.isdigit() and char != "." and char != "-":
            return False
        
        if char == ".":
            dec_idx = idx
    
    if dec_idx:
        # print(dec_idx)
        count = len(input) - dec_idx
        # print(count)
        return count == 3

    return True


class Test(unittest.TestCase):

    def test_zer_decimal(self):
        actual = isAmount("100")
        expected = True
        self.assertEqual(actual, expected)

    def test_empty_string(self):
        actual = isAmount("")
        expected = False
        self.assertEqual(actual, expected)

    def test_one_decimal(self):
        actual = isAmount("1.1")
        expected = False
        self.assertEqual(actual, expected)

    def test_alpha(self):
        actual = isAmount("Hello. I")
        expected = False
        self.assertEqual(actual, expected)

    def test_negative(self):
        actual = isAmount("-10")
        expected = True
        self.assertEqual(actual, expected)
    
    def test_special_char(self):
        actual = isAmount("%^^^%.($")
        expected = False
        self.assertEqual(actual, expected)
    
    def test_two_decimal(self):
        actual = isAmount("100.20")
        expected = True
        self.assertEqual(actual, expected)

    def test_three_decimal(self):
        actual = isAmount("100.200")
        expected = False
        self.assertEqual(actual, expected)

    def test_lots_decimals(self):
        actual = isAmount("100.2000000000000")
        expected = False
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)