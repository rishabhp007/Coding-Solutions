class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        n = len(nums)
        result = float("-inf")
        index = 0
        for i in range (0,n):
            if nums[i] > result:
                result = nums[i]
                index = i
        return index
        