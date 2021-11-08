"""Find the subsequence with the largest sum.

Given a list of integers, like:

  [1, 0, 3, -8, 4, -2, 3]

Return the contiguous subsequence with the largest sum. For
that example, the answer would be [4, -2, 3], which sums to 5.


    >>> largest_sum([1, 0, 3, -8, 4, -2, 3])
    [4, -2, 3]

    >>> largest_sum([1, 0, 3, -8, 4, -2, 3, -2])
    [4, -2, 3]

    >>> largest_sum([1, 0, 3, -8, 19, -20, 4, -2, 3, -2])
    [19]

For ties, return the first one:

    >>> largest_sum([2, 2, -10, 1, 3, -20])
    [2, 2]

Return the shortest version:

    >>> largest_sum([2, -2, 3, -1])
    [3]

If the list is all negative numbers, the subsequence
with the highest sum will be empty (ie, we can do no better
than pick nothing!):

    >>> largest_sum([-1, -2])
    []
"""


def largest_sum(nums):
    """Find subsequence with largest sum."""
    left_pointer = 0
    right_pointer = 0

    largest_substring = []
    largest_sum = 0

    # sums = [nums[0]]
    # for i in range(len(nums)-1):
    #     sums.append(sums[i] + nums[i + 1])

    # print(sums)

    for i in range(len(nums)):
        temp_sum = 0
        # print(f"i = {i}")
        if nums[i] >= largest_sum:
            largest_sum = nums[i]
            left_pointer = i
        for j in range(i, len(nums)):
            temp_sum += nums[j]
            if (temp_sum > largest_sum):
                # print(f"j = {j}")
                largest_sum = temp_sum
                right_pointer = j
                left_pointer = i

    # print(f"left pointer = {left_pointer}")
    # print(f"right pointer = {right_pointer}")
    if largest_sum == 0:
        return []
    else:
        return nums[left_pointer:right_pointer + 1]



    # if left_pointer at nums is greater than largest_sum
        # set largest_sum equal to left_pointer at nums

    

    # while left_pointer < len(nums):
    #     print(f"left_pointer = {left_pointer}")
    #     while right_pointer < len(nums):
    #         print(f"right_pointer = {right_pointer}")
    #         if (nums[left_pointer] + nums[right_pointer]) > largest_sum:
    #             largest_sub.append(nums[left_pointer])
    #             right_pointer += 1
    #         else:
    #             left_pointer +=1
    

    

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. YOU HANDLED THIS SUMMARILY!\n")
