def isPalindrome(x: int) -> bool:
    if x > -1:
        ans = ''
        for i in str(x):
            ans = i + ans
        return True if int(ans) == x else False
    else:
        return False

print(isPalindrome(121))      
print(isPalindrome(-121))
print(isPalindrome(10))   
