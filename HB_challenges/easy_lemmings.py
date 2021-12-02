"""Lazy lemmings.

Find the farthest any single lemming needs to travel for food.

    >>> furthest(3, [0, 1, 2])
    0

    >>> furthest(3, [2])
    2

    >>> furthest(3, [0])
    2

    >>> furthest(6, [2, 4])
    2

    >>> furthest(7, [0, 6])
    3

    # >>> furthest_optimized(7, [0, 6])
    # 3

    # >>> furthest_optimized(3, [0, 1, 2])
    # 0

    # >>> furthest_optimized(3, [2])
    # 2

    # >>> furthest_optimized(3, [0])
    # 2

    # >>> furthest_optimized(6, [2, 4])
    # 2
"""


def furthest(num_holes, cafes):
    """Find longest distance between a hole and a cafe."""
    
    worst = 0

    if len(cafes) == num_holes:
        return worst

    for x in range(num_holes):
        # print(x)
        distances = []
        for cafe in cafes:
            distance = abs(x - cafe)
            distances.append(distance)
            # print(f"distances = {distances}")
        current_worst = min(distances)
        # print(f"current_worst = {current_worst}")
        worst = max(current_worst, worst)
        # print(f"worst = {worst}")
    
    return worst

    #### || HB SOLUTION || ####
    # worst = 0

    # for hole in range(num_holes):
    #     print(f"hole = {hole}")
    #     # Looking at all cafes, find distance to this hole,
    #     # and choose the smallest distance.

    #     dist = min([abs(hole - cafe) for cafe in cafes])
    #     print(f"dist = {dist}")

    #     # Keep track of the longest distance we've seen

    #     worst = max(worst, dist)
    #     print(f"inside for loop, worst = {worst}")

    # print(f"outside for loop, worst = {worst}")
    # return worst


    

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED; GREAT JOB!\n")
