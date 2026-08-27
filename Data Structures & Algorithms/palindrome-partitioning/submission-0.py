class Solution:
    def partition(self, s: str) -> List[List[str]]:

        def generate(i):
            if i==len(s):
                result.append(ps.copy())
                return
            
            for j in range(i,len(s)):

                if palindrome(i,j):

                    ps.append(s[i:j+1])
                    generate(j+1)
                    ps.pop()

        
        def palindrome(i,j):

            while i <= j:
                if s[i]==s[j]:
                    i+=1
                    j-=1
                else:
                    return False
            return True
        
        ps=[]
        result=[]
        generate(0)
        return result

        
        