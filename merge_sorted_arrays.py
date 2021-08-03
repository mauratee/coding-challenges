
def merge_sorted_arrays(array1, array2):
    sorted_array = []
    idx = 0
    jdx = 0
    flag = 0

    if array1 == []:
        return array2
    
    if array2 == []:
        return array1

    
    while not (idx >= len(array1) or jdx >= len(array2)):
            print(f"array1[idx] = {array1[idx]}")
            print(f"array2[jdx] = {array2[jdx]}")
            if array1[idx] <= array2[jdx]:
                sorted_array.append(array1[idx])
                idx += 1
            else:
                sorted_array.append(array2[jdx])
                jdx += 1

            if idx == len(array1):
                flag = 1
    print(flag)
    if flag == 1:
        for num in array2[jdx:]:
            sorted_array.append(num)

    else:
        for num in array1[idx:]:
            sorted_array.append(num)

    print(sorted_array)
    return sorted_array

merge_sorted_arrays([0,3,4,31], [3,4,6,30])