class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        hash_map={}

        for i in s:
            hash_map[i]=hash_map.get(i,0)+1
        
        for i in t:
            hash_map[i]=hash_map.get(i,0)-1
            if hash_map[i] <0:
                return False
        
        return True

        


        