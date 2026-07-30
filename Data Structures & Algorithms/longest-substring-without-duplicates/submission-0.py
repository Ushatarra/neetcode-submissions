class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        length=0
        window=set()
        left,right=0,0

        while left < len(s) and right < len(s):
            
            while s[right] in window:
                window.remove(s[left])
                left+=1
            
            window.add(s[right])
            
            length=max(length,right-left+1)
            right+=1


        return length
                    



            
           
        