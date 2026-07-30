class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        
        window=""
        max_freq=0
        replacements=0
        left=0
        right=0
        hash_map={}
        answer=0

        for right in range(len(s)):
            hash_map[s[right]]=hash_map.get(s[right],0)+1
            max_freq=max(max_freq,hash_map[s[right]])
            replacements=(right-left+1) - max_freq

            while replacements > k:
                hash_map[s[left]]-=1
                left+=1

                replacements=(right-left+1) - max_freq
            answer=max(answer,right-left+1)
        return answer

        




        