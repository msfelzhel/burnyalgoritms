def longestCommonPrefix(v: list[str]) -> str:
    ans=""
    v=sorted(v)
    first=v[0]
    last=v[-1]
    for i in range(min(len(first),len(last))):
        if(first[i]!=last[i]):
            return ans
        ans+=first[i]
    return ans
print(longestCommonPrefix(["flower","flow","flight"]))
print(longestCommonPrefix(["dog","racecar","car"]))
