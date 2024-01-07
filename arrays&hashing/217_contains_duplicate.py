

listInput = [1,1,1,3,3,4,3,2,4,2]

def containsDuplicate(nums):
    
    if len(set(nums)) == len(nums):
        return False
    return True

print(containsDuplicate(nums=listInput))