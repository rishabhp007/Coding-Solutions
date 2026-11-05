class Solution:
    def findMin(self, nums: list[int]) -> int:
        n = len(nums)
        mini = float("inf")
        low = 0
        high = n-1
        while low <= high:
            mid = (low + high)//2
            if nums[low] == nums[mid] == nums[high]:
                if mini > nums[mid]:
                    mini = nums[mid]
                low += 1
                high -= 1
                continue
            if nums[mid] <= nums[high]:
                if mini > nums[mid]:
                    mini = nums[mid]
                high = mid -1
            else:
                if mini > nums[low]:
                    mini = nums[low]
                low = mid + 1
        return mini
        