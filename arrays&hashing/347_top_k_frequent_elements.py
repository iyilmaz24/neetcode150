

nums = [1,1,1,2,2,3]
k = 2

def topKFrequent(nums, k):
    
    dict = {}
    for num in nums:
        if num not in dict:
            dict[num] = 1
        else:
            dict[num] += 1

    def sortFilter(item):
        return item[1]
    
    list1 = [[key, dict[key]] for key in dict]
    list1.sort(key=sortFilter, reverse=True)
    list1 = [i[0] for i in list1[:k]]
    return list1

print(topKFrequent(nums, k))