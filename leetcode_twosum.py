# def twoSum(nums, target):
#         dict_of_x={}
#         len_of_nums=len(nums)
#         i=0
#         while i<len_of_nums:
#             val= target - nums[i]
#             if(val in dict_of_x):
#                 return [dict_of_x[val],i]
#             dict_of_x[nums[i]]=i
#             i+=1

def twoSum(nums, target):
        if not nums:
            return []
        
        indices = []
        length_nums = len(nums)
        i = 0
    
        while i < length_nums:
            
            for j in range(i + 1, length_nums):
                # print(f"i={i}")
                # print(f"j={j}")
                # print(nums[j])
                if nums[i] + nums[j] == target:
                    return [i, j]
                
                j += 1
                
            i +=1
        
        return indices

print(twoSum([2,7,11,15], 9))
print(twoSum([3,2,4], 6))
print(twoSum([3,2,3], 6))