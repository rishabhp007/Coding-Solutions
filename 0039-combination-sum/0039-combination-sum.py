class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        n = len(candidates)
        result = []
        storage = [([],0,0)]
        while storage:
            current_path, current_sum, start_index = storage.pop()
            if current_sum == target:
                result.append(current_path)
                continue
            if current_sum > target:
                continue
            for i in range(start_index, n):
                new_path = current_path + [candidates[i]]
                new_sum = current_sum + candidates[i]
                storage.append((new_path, new_sum, i))
        return result


        