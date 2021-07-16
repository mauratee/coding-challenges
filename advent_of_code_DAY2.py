

# creates passwords list with newline characters at the end of each item
# with open("AOC_day2_input.txt") as f:
#         passwords = f.readlines()

# print(passwords)

# creates data list without newline characters
with open("AOC_day2_input.txt") as f:
    data = f.read().splitlines()

# print(data)
# example item: "9-12 k: qkhxrknkkzpk"




# import re

# def part1(passwords):

#     valid_pwd = 0
#     for password in passwords:
#         ltr = re.search(r"[a-z]", password) # note r"pattern"
#         print(ltr)

#     return valid_pwd



# if __name__ == "__main__":
    