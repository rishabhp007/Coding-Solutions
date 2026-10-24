class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        n = len(nums)
        nums = [str(num) for num in nums]
        
        for i in range(n):
            for j in range(n-i-1):
                first = nums[j] + nums[j+1]
                second = nums[j+1] + nums[j]
                if first < second :
                    nums[j], nums[j+1] = nums[j+1], nums[j]
        result = "".join(nums)
        if result[0] == "0":
            return "0"

        return result


        