"""How many days are there in a month?

Given a string with a month and a year (separated by a space),
returns the number of days in that month.

For example::

    >>> for i in range(1, 13):
    ...     date = str(i) + " 2016"
    ...     print("%s has %s days." % (date, days_in_month(date)))
    1 2016 has 31 days.
    2 2016 has 29 days.
    3 2016 has 31 days.
    4 2016 has 30 days.
    5 2016 has 31 days.
    6 2016 has 30 days.
    7 2016 has 31 days.
    8 2016 has 31 days.
    9 2016 has 30 days.
    10 2016 has 31 days.
    11 2016 has 30 days.
    12 2016 has 31 days.

    >>> days_in_month("02 2015")
    28
    >>> days_in_month("1 1984")
    31
    >>> days_in_month("05 1984")
    31
    >>> days_in_month("02 1904")
    29
    >>> days_in_month("02 1900")
    28
"""


def is_leap_year(year):
    """Is this year a leap year?

    Every 4 years is a leap year::

        >>> is_leap_year(1904)
        True

    Except every hundred years::

        >>> is_leap_year(1900)
        False

    Except-except every 400::

        >>> is_leap_year(2000)
        True
    """

    if year % 400 == 0:
        return True

    if year % 100 == 0:
        return False

    if year % 4 == 0:
        return True


def days_in_month(date):
    """How many days are there in a month?"""
    # create hash table of months and days
    months = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

    # break string into month and year at space
    date = date.split(' ')
    month = date[0]
    year = int(date[1])
    
    # if month starts with 0, discard 0
    if int(month[0]) == 0:
        month = month[1]
    # print(month)

    # if month is 2, check if leap year
    if int(month) == 2:
        # if leap year, return 29
        if is_leap_year(year):
            return 29
        else:
            return 28
    
    return months[int(month)]

        


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. W00T!\n")

