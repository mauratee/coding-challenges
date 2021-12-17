array = [1,2,3,4,5,6,7,8,9,10,11,12]
a = 0
idx = 0
while a < 12:
    if array[idx] % 2 == 0:
        a += array[idx]
    idx += 1;
print(str(a) + ", " + str(idx))