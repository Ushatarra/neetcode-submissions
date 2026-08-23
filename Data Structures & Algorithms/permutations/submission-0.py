class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def generate(li,p_map):

            if len(li) == len(nums):
                result.append(li.copy())
                return 
            
            for i in range(len(nums)):
                if p_map[nums[i]] == 0:
                    li.append(nums[i])
                    p_map[nums[i]]=1
                    generate(li,p_map)
                    top=li.pop()
                    p_map[top] = 0

        result=[]
        li=[]
        p_map={}
        for i in nums:
            p_map[i]=0
        generate(li,p_map)
        return result
