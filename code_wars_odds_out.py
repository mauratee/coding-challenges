import unittest

def odd_ones_out(numbers):
    # create list of odds
    odd_list = []
    odds_removed = []
    
    for number in numbers:
        if number in odd_list:
            odd_list.remove(number)
        else:
            odd_list.append(number)
    
    if odd_list:
        for number in numbers:
            if number not in odd_list:
                odds_removed.append(number)
                
    return odds_removed

class Test(unittest.TestCase):

    def test_1(self):
        actual = odd_ones_out([1,2,3,1,3,3])
        expected = [1, 1]
        self.assertEqual(actual, expected)

    def test_2(self):
        actual = odd_ones_out([75, 68, 75, 47, 68])
        expected = [75, 68, 75, 68]
        self.assertEqual(actual, expected)

    def test_3(self):
        actual = odd_ones_out([42, 72, 32, 4, 94, 82, 67, 67])
        expected = [67, 67]
        self.assertEqual(actual, expected)

    def test_4(self):
        actual = odd_ones_out([100, 100, 5, 5, 100, 50, 68, 50, 68, 50, 68, 5, 100])
        expected = [100, 100, 100, 100]
        self.assertEqual(actual, expected)
    
    def test_5(self):
        actual = odd_ones_out([82, 86, 71, 58, 44, 79, 50, 44, 79, 67, 82, 82, 55, 50])
        expected = [44, 79, 50, 44, 79, 50]
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)