class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hash_map={}

        for i in range(len(nums)):

            dif=target-nums[i]
            if dif not in hash_map:
                hash_map[nums[i]] = i
            
            else:
                return [hash_map[dif],i]



            



        