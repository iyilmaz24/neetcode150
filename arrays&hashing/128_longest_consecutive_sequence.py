

nums = [100,4,200,1,3,2]

def longestConsecutive(nums):
        if(len(nums) == 0):
            return 0
        nums.sort()

        highScore = 1
        currScore = 1
        for i in range(0, len(nums) - 1):
            if nums[i] == nums[i + 1]:
                continue
            if nums[i] == (nums[i + 1] - 1):
                currScore += 1
            else:
                if currScore > highScore:
                    highScore = currScore
                currScore = 1

        if currScore > highScore:
            return currScore
        return highScore

print(longestConsecutive(nums))