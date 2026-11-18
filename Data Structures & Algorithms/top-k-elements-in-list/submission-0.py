class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {nums[0]: 1}
        for i in range(1,len(nums)):
            if nums[i] in counter:
                 counter[nums[i]]+=1
            else:
                counter[nums[i]]= 1
        sor_counter = sorted(counter, key = lambda num: counter[num], reverse= True)
        return sor_counter[:k]
        
            
            
        