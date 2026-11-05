class Solution:
    def findMin(self, nums: list[int]) -> int:
        n = len(nums)
        minimum = float("inf")
        low = 0
        high = n-1
        while low <= high:
            mid = (low + high)//2
            if nums[mid] <= nums[high]:
                if minimum > nums[mid]:
                    minimum = nums[mid]
                high = mid -1
            else:
                if minimum > nums[low]:
                    minimum = nums[low]
                low = mid + 1
        return minimum
        