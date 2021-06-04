import re 

def isPalindrome(s) -> bool:
    s = re.sub("[^a-z|^0-9]","", s.lower())
    l, r = 0 , len(s) - 1
    while l < r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1        
    return True


# s = "A man, a plan, a canal: Panama"
# isPalindrome(s)
