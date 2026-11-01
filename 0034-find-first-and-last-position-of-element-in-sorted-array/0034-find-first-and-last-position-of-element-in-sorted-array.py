class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)
        
        def first():
            left = 0
            right = n -1
            ans = -1
            while left <= right:
                mid = (left+right)//2
                if nums[mid] < target :
                    left = mid + 1
                elif nums[mid] > target :
                    right = mid - 1
                elif nums[mid] == target :
                    ans = mid
                    right = mid - 1
            return ans
        def last ():
            left = 0
            right = n -1
            ans = -1
            while left <= right :
                mid = (left + right)//2
                if nums[mid] < target:
                    left = mid +1
                elif nums[mid] > target:
                    right = mid -1
                elif nums[mid] == target:
                    ans = mid
                    left = mid + 1
            return ans
                
        return [first(), last()]
        