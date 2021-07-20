import math
import os
import random
import re
import sys

# Given the time in numerals we may convert it into words, as shown below:
# At 0 minutes, use o' clock. For , use past, and for

# use to. Note the space between the apostrophe and clock in o' clock. 
# Write a program which prints the time in words for the input given in the format described.

# timeInWords has the following parameter(s):

#     int h: the hour of the day
#     int m: the minutes after the hour

# Returns

#     string: a time string as described

# Input Format

# The first line contains
# , the hours portion The second line contains , the minutes portion 
#
# Complete the 'timeInWords' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER h
#  2. INTEGER m
#

def timeInWords(h, m):
    # create list of strings of numbers 1-12
    hour_dict = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six",
                 7: "seven", 8: "eight", 9: "nine", 10: "ten", 11: "eleven", 12: "twelve"}
    min_dict = {0o1: "one", 0o2: "two", 0o3: "three", 0o4: "four", 0o5: "five", 0o6: "six",
                 0o7: "seven", 8: "eight", 9: "nine", 10: "ten", 11: "eleven", 12: "twelve",
                 13: "thirteen", 14: "fourteen", 15: "quarter", 16: "sixteen", 17: "seventeen",
                 18: "eighteen", 19: "nineteen", 20: "twenty", 21: "twenty one", 22: "twenty two",
                 23: "twenty three", 24: "twenty four", 25: "twenty five", 26: "twenty six",
                 27: "twenty seven", 28: "twenty eight", 29: "twenty nine", 30: "half"}
    # 
    time_words = ""

    if m == 00:
       time_words += (hour_dict[h] + " o' clock")
       return time_words


    if m >= 1 and m <= 30:
        time_words += (min_dict[m] + " past " + hour_dict[h])
        return time_words
    
    if m >= 31:
        until_hour = (60 - m)
        time_words += (min_dict[until_hour] + " to " + hour_dict[h+1])

    

    return time_words