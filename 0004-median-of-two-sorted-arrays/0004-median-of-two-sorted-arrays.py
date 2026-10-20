class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        i = 0
        j = 0
        merged_array = []
        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                merged_array.append(nums1[i])
                i += 1
            else:
                merged_array.append(nums2[j])
                j += 1
        
        merged_array.extend(nums1[i:])
        merged_array.extend(nums2[j:])

        l = len(merged_array)
        mid = l // 2

        if l % 2 == 1:
            return float(merged_array[mid])
        else :
            return (merged_array[mid-1] + merged_array[mid]) / 2