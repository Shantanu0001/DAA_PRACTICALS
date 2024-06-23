class Solution(object):
    def findNumbers(self, nums):
        count = 0
        
        for num in nums:
            digit_count = 0
            while num > 0:
                num //= 10
                digit_count += 1
            
            if digit_count % 2 == 0:
                count += 1
        
        return count

        