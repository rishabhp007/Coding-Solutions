class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        n = len(nums)
        nums1 = set(nums)
        result = []
        for i in range(1, n+1):
            if i not in nums1:
                result.append(i)
        return result

            


        