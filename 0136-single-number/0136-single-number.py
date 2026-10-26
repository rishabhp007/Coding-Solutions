class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        n = len(nums)
        my_set = {}
        for i in range(0,n):
            if nums[i] in my_set:
                my_set[nums[i]] += 1
            else:
                my_set[nums[i]] = 1

        for i in range(0,n):
            if my_set[nums[i]] == 1:
                return nums[i]
        
        

        