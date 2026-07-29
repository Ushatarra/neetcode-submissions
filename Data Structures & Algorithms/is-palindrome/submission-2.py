class Solution:
    def isPalindrome(self, s: str) -> bool:

        s="".join(ch for ch in s if ch.isalnum())
        s=s.lower()
        l,r=0,len(s)-1

        while l < r:
                if s[l] == s[r]:
                    l+=1
                    r-=1
                else:
                    return False
        return True

        # if len(s)%2==0:
        #     while l < r:
        #         if s[l] == s[r]:
        #             l+=1
        #             r-=1
        #         else:
        #             return False
        #     return True
        # else:
        #     while l!=r:
        #         if s[l] == s[r]:
        #             l+=1
        #             r-=1
        #         else:
        #             return False
        #     return True

            

        