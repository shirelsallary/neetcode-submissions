"Naive solution -> nested loop, O(n^2)"
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {nums[0]: 0}
        for i in range(1, len(nums)):
            curr = target - nums[i]
            if curr in seen:
                return [seen[curr], i]
            seen[nums[i]] = i
        return []
            




        