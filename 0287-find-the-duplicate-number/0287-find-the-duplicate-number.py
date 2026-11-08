class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        result = set()
        for num in nums:
            if num not in result:
                result.add(num)
            else:
                return num

            

        