def twoSum(nums: list[int], target: int) -> list[int]:
    numMap = {}
    n = len(nums)
    for i in range(n):
        complement = target - nums[i]
        if complement in numMap:
                return [numMap[complement],i]
        numMap[nums[i]] = i
print(twoSum([2,7,11,15],9))
