from typing import List

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        arr = []
        nums.sort() 
        for i, num in enumerate(nums):  
            if num == target:  
                arr.append(i)  
        return arr 
