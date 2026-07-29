class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        hash_set=set(nums)
        length=0
        max_len=0

        for num in nums:
            if num-1 not in hash_set:
                length=1
                current=num
                while current+1 in hash_set:
                    current+=1
                    length+=1
            
                max_len=max(max_len,length)
        
        return max_len
                


        
        
        