class Solution:
    def minWindow(self, s: str, t: str) -> str:

        t_map={}
        w_map={}

        for i in t:
            t_map[i]=t_map.get(i,0)+1
        
        formed=0
        required=len(t_map)

        start=0
        min_len=float("inf")

        left=0
        for right in range(len(s)):

            ch=s[right]
            w_map[ch]=w_map.get(ch,0)+1

            if ch in t_map and t_map[ch]==w_map[ch]:
                formed+=1
            
            while formed == required:
                
                if right-left+1 < min_len:
                    min_len=right-left+1
                    start=left
                
                left_char=s[left]
                w_map[left_char] -=1

                if left_char in t_map and w_map[left_char] < t_map[left_char]:
                    formed-=1
                
                left+=1
        
        if min_len == float("inf"):
            return ""
        
        return s[start:start+min_len]
            


        







            

            
                



            

        
        