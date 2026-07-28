class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        hash_map={}

        for i in nums:
            hash_map[i]=hash_map.get(i,0)+1
        
        for ele in hash_map:
            if hash_map[ele] > 1:
                return True
        
        return False


        



        