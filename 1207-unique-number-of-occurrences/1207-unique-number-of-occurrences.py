class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        n = len(arr)
        
        my_set ={}
        for i in range(0,n):
            if arr[i] in my_set:
                my_set[arr[i]] += 1
            else:
                my_set[arr[i]] = 1
        return len(set(my_set.values())) == len(my_set)


        