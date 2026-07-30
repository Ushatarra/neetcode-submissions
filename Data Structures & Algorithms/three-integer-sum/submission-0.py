class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        result=[]
        seen=set()

        for i in range(len(nums)):
            hash_map=set()
            for j in range(i+1,len(nums)):

                add=-(nums[i]+nums[j])
                if add not in hash_map:
                    hash_map.add(nums[j])
                else:
                    triplet=tuple(sorted([nums[i],nums[j],add]))
                    
                    if triplet not in seen:
                        seen.add(triplet)
                        result.append(list(triplet))
                    hash_map.add(nums[j])
        
        return result
                

                

        