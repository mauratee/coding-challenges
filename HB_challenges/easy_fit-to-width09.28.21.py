"""
Write a function that prints a string, fitting its characters within char
limit.

It should take in a string and a character limit (as an integer). It should
print the contents of the string without going over the character limit
and without breaking words. For example:

>>> fit_to_width('hi there', 50)
hi there

Spaces count as characters, but you do not need to include trailing whitespace
in your output:

>>> fit_to_width('Hello, world! I love Python and Hackbright',
...              10)
...
Hello,
world! I
love
Python and
Hackbright

Your test input will never include a character limit that is smaller than
the longest continuous sequence of non-whitespace characters:

>>> fit_to_width('one two three', 8)
one two
three
"""

def fit_to_width(string, limit):
    """Print string within a character limit."""

    # split the string along whitespace characters
    word_list = string.split(" ")
    # reverse list of words
    word_list.reverse()
    # out put is list of words

    # make another list, lines
    lines = []
    # make another list, current_line
    current_line = []

    # if length of current line plus space plus last item in list of words is less than limit:
    while word_list:
        # print("*"* 20)
        # print(f"last in word list = {word_list[-1]}")
        # print(f"current line = {current_line}")
        if len((" ").join(current_line + [word_list[-1]])) <= limit:
        # append last item in list of words to current line
            current_line.append(word_list.pop())
            # print(f"current line appended = {current_line}")
    # else, 
        else:
        # if item in current line,
            if current_line:
            # append current line to lines
                lines.append((" ").join(current_line))
                # print(f"lines = {lines}")
                current_line = []
            # set current line to blank list

    # append last current line to lines
    lines.append((" ").join(current_line))

    # print(f"lines = {lines}")

    # for line in lines, print line
    for line in lines:
        print(line)


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')
