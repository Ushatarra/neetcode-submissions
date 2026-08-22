class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        def generate(i,li):

            if i==len(nums):
                result.append(li.copy())
                return
            
            li.append(nums[i])
            generate(i+1,li)
            li.pop()

            generate(i+1,li)
        
        result=[]
        li=[]
        generate(0,li)
        return result


        