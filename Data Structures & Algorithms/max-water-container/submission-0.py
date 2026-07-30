class Solution:
    def maxArea(self, heights: List[int]) -> int:

        left=0
        right=len(heights)-1
        max_len=0

        while left < right:

            width=right-left
            height=0
            if heights[left] < heights[right]:

                height=heights[left]
                left+=1
            else:
                height=heights[right]
                right-=1

            area=width*height
            max_len=max(max_len,area)

        return max_len 


        