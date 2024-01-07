

nums = [2,7,11,15]
target = 9

def twoSum(nums, target):
        
        dict = {}
        for index, num in enumerate(nums):
            compliment = target - num
            if compliment in dict:
                return index, dict[compliment]
            else:
                dict[num] = index

print(twoSum(nums, target))