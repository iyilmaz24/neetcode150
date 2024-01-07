

s = "anagram"
t = "nagaram"

def isAnagram(s, t):
    
    s1 = s.replace(" ", "").lower()
    s2 = t.replace(" ", "").lower()

    return sorted(s1) == sorted(s2)

# ALTERNATIVE SOLUTION:
    # dict = {}
    # for char in s:
    #     if char not in dict:
    #         dict[char] = 1
    #     else:
    #         dict[char] += 1

    # for char in t:
    #     if char not in dict:
    #         return False
    #     else:
    #         dict[char] -= 1

    # for key in dict:
    #     if dict[key] != 0:
    #         return False
    # return True

print(isAnagram(s, t))