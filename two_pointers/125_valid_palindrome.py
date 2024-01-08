

s = "A man, a plan, a canal: Panama"

def isPalindrome(s):

    string = ""
    for char in s:
        if char.isalnum():
            string += char.lower()

    return string  == string[::-1]

print(isPalindrome(s))