def romanToInt(s: str) -> int:
    numMap = {'I': 1, 'V': 5, 'X' : 10 , 'L' : 50, 'C' : 100, 'D' : 500 , 'M': 1000}
    ans = 0 
    n = len(s)
    for i in range(n):
        if i < n - 1 and numMap[s[i]] < numMap[s[i+1]]:
            ans -= numMap[s[i]]
        else:
            ans += numMap[s[i]]
    return ans 

print(romanToInt('III'))
print(romanToInt('LVIII'))
print(romanToInt("MCMXCIV"))
