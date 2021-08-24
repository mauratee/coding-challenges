def removeDuplicates(self, nums: List[int]) -> int:
    # test case: OUT: 2, [1,2,_]
    # test Case: OUT: 1, nums = [0,_,_]
    # test case OUT: 0, nums = []
    # test case OUT: 3, nums = [1,2,3]
    # [0,0,0]
    # []
    # [1,2,3]
        
    # current_num is first num in list
        
    # track index, i
     # i = 1
    # count number of unique integers
    unique_nums = 0 # unique_nums = 2
        # current num = 1 # current_num = '_'
        
    # for num in nums
    for x in range (1, len(nums)):
        i = 0
        current_num = nums[i]
        # x = 
    #for num in nums:
        if nums[x] == current_num:
        # if 2 == 1
            nums[x] = '_'
            # nums[1] = _
            # nums = [1,_,2]
        else:
            unique_nums += 1
        i += 1
            
            
    def f(s):
        if s == '_':
            s = 1000
        return s
            
    nums = nums.sort(key=f)
        
        # nums = sorted(nums)
        # for num in nums:
        #     if num != '_':
        #         unique_nums += 1
        
        # return unique counter, nums
    print(unique_nums)
    return unique_nums