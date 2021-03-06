

# creates passwords list with newline characters at the end of each item
# with open("AOC_day2_input.txt") as f:
#         passwords = f.readlines()

# print(passwords)

# creates data list without newline characters


# print(data)
# example item: "9-12 k: qkhxrknkkzpk"

from collections import Counter

def validate_pw_1(ch_min, ch_max, ch, pw):
    chars = Counter(pw)
    print(chars)

    return ch_min <= chars[ch] <= ch_max

print(validate_pw_1(5, 6, 'g', 'rvfgnggjgk'))

def parse_policy_and_pw(policies_and_pws):
    for policy_and_pw in policies_and_pws:
        policy_range, policy_char, pw = policy_and_pw.split(" ")

        # (5, 6, 'g', 'rvfgnggjgk')
        # (2, 6, 'c', 'fcpwjqhcgtffzlbj')
        return tuple(int(n) for n in policy_range.split("-")) + (
            policy_char[0],
            pw
        )




# import re

# def part1(passwords):

#     valid_pwd = 0
#     for password in passwords:
#         ltr = re.search(r"[a-z]", password) # note r"pattern"
#         print(ltr)

#     return valid_pwd



if __name__ == "__main__":
    with open("AOC_day2_input.txt") as f:
        data = f.read().splitlines()

    print(parse_policy_and_pw(data))
    