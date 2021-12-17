def func(a):
    if a <= 0:
        return 1
    if a % 2 == 0:
        return a;
    else:
        return func(a-1) + func(a-2)

print(func(14))