class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        def generate(i,target,li):

            if target <0 :
                return

            if i==len(nums):
                if target == 0:
                    result.append(li.copy())
                return
            
            li.append(nums[i])
            generate(i,target-nums[i],li)
            li.pop()
            
            generate(i+1,target,li)

        result=[]
        li=[]
        generate(0,target,li)
        return result

            


            



                
        