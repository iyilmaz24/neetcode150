

numbers = [2,7,11,15]
target = 9

def twoSum(numbers, target):
        
        # dict = {} 
        # for index, num in enumerate(numbers): 
        #     compliment = target - num

        #     if compliment not in dict:
        #         dict[num] = index + 1
        #     else:
        #         return [dict[compliment], index+1]

        for index, num in enumerate(numbers):
            compliment = target - num

            if compliment in numbers:
                if numbers.index(compliment) < index:
                    return [numbers.index(compliment) + 1, index + 1]
                if numbers.index(compliment) > index:
                    return [index + 1, numbers.index(compliment) + 1]
                
print(twoSum(numbers, target))