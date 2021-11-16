import unittest

# Given a string as input, return a string that has any character
# that repeats 3 or more times consecutively removed

# TEST CASES
# "CAABBBACDD" -> "CCDD"
# "" -> ""
# "CCC" -> ""
# "ABABB" -> "ABABB"
# "ABBBAA" -> ""
# "ABBBA" -> "AA"

def compress_string(astring):
    stack = []

