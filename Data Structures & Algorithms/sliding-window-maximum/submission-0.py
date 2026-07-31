class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        
        max_win=[]

        for right in range(len(nums)-k+1) :

            w=nums[right:right+k]

            max_win.append(max(w))
            

        return max_win

            

        