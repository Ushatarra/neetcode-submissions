class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # max_win=[]
        # for right in range(len(nums)-k+1) :
        #     w=nums[right:right+k]
        #     max_win.append(max(w))
        # return max_win


        max_win=[]
        w=nums[:k]
        large=max(w)
        max_win.append(large)

        for right in range(k,len(nums)):
            removed = w.pop(0)
            w.append(nums[right])


            if removed == large:
                large = max(w)
            elif nums[right] > large:
                large = nums[right]
            
            max_win.append(large)
        
        return max_win
            
            
            







            

            


            

        