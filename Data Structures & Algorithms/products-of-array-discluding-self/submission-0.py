class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        answer=[]
        left_product=[]
        right_product=[]
        product=1

        for i in range(len(nums)):
            if i!=0:
                product*=nums[i-1]
            else:
                product*=1
            left_product.append(product)
        product=1
        for j in range(len(nums)-1,-1,-1):
            if j != len(nums)-1:
                product*=nums[j+1]
            else:
                product*=1
            right_product.append(product)
        
        right_product=right_product[::-1]
        for i in range(len(nums)):
            answer.append(right_product[i]*left_product[i])
        return answer

                
