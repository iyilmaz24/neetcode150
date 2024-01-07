

strList = ["eat","tea","tan","ate","nat","bat"]

def groupAnagrams(strs):
    
    dict = {}

    for string in strs:
        temp = list(string)
        temp.sort()
        temp = "".join(temp)

        if temp in dict:
            dict[temp].append(string)
        else:
            dict[temp] = [string]

    return dict.values()

print(groupAnagrams(strList))