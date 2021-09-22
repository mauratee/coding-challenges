"""Given a list of numbers 1...max_num, find which one is missing in a list."""


def missing_number(nums, max_num):
    """Given a list of numbers 1...max_num, find which one is missing.

    *nums*: list of numbers 1..[max_num]; exactly one digit will be missing.
    *max_num*: Largest potential number in list

    >>> missing_number([7, 3, 2, 4, 5, 6, 1, 9, 10], 10)
    8

    >>> missing_number([7, 3, 2, 8, 5, 6, 1, 9, 10], 10)
    4
    
    """

    # || This solution is O(n) runtime:

    nums_dict = {}

    for num in nums:
        if num in nums_dict:
            pass
        else:
            nums_dict[num] = num
    
    for i in range(1, max_num + 1):
        if i not in nums_dict:
            return i


    # || This solution is O(n log n) runtime but doesn't use additional memory:

    # sort list in-place, doesn't take up more memory
    nums.sort()
    # print(nums)

    for idx, num in enumerate(nums):
        if (num - idx) != 1:
            # print(num)
            return (num - 1)

    nums.append(max_num + 1)


    # HB solution to adding no additional memory
    nums.sort()
    last = 1

    for i in nums:
        if i != last:
            return last
        last += 1

    raise Exception("None are missing!")


    # || Solution that takes O(n) runtime and O(1) space:

    # expected = sum(range(max_num +1))
    # or:
    expected = (max_num + 1) * (max_num // 2)
    
    return expected - sum(nums)



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASS. NICELY DONE!\n")
