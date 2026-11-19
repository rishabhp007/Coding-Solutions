class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        n = len(nums)
        count = 0
        result = 0
        for i in range(0,n):
            if nums[i] == 1:
                count += 1
                if count > result:
                    result = count
            else:
                count = 0
        return result 

