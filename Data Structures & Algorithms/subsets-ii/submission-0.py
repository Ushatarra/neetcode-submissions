class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        def generate(i,li):

            if i == len(nums):
                if tuple(li) not in used: 
                    used.add(tuple(li)) 
                    result.append(li.copy())
                return
            

            li.append(nums[i])
            generate(i+1,li)
            li.pop()

            generate(i+1,li)
        
        nums=sorted(nums)
        result=[]
        li=[]
        used=set()
        generate(0,li)
        return result

                
        