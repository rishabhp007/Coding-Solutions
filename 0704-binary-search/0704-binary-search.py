class Solution:
    def search(self, nums: list[int], target: int) -> int:
        n = len(nums)
        left  = 0
        right = n-1
        ans = -1
        while left <= right:
            mid = (left + right)//2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] == target:
                return mid
            else:
                left = mid + 1
            
        return ans
        