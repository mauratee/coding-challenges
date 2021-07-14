
with open("AOC_day2_input.txt") as f:
        passwords = f.readlines()

# print(passwords)
import re

# match_obj = re.search(r"[0-9]+", "a 123 b")   # note r"pattern"
# expect: c,x,w,q,g,q,


def part1(passwords):

    valid_pwd = 0
    for password in passwords:
        ltr = re.search(r"[a-z]", password) # note r"pattern"
        print(ltr)

        

    #return valid_pwd


# test = part1(passwords)

# if __name__ == "__main__":
    