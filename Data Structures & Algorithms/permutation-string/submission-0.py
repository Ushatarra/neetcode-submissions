class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        for right in range(0,len(s2)-len(s1)+1):
            s=s2[right:right+len(s1)]
            s="".join(sorted(s))
            s1="".join(sorted(s1))
            if s==s1:
                return True
        return False

            





         
        