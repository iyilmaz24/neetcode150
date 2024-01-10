

s = "()[]{}"

def isValid(s):

    stack = []
    dict1 = {"(":")", "{":"}", "[":"]"}
    dict2 = {")":"(", "}":"{", "]":"["}

    for char in s:
        if char in dict1:
            stack.append(char)
        else:
            if len(stack) == 0:
                return False 

            if dict2[char] == stack[-1]:
                stack.pop()
            else:
                return False

    return len(stack) == 0

print(isValid(s))