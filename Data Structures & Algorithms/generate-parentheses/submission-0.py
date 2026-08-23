class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        stack=[]
        li=[]
        def back_track(opened,closed):
        
            if opened == n and closed == n:
                stack.append("".join(li))
                return
            
            
            if opened < n:
                li.append("(")
                back_track(opened+1,closed)
                li.pop()
            
            if closed < opened:
                li.append(")")
                back_track(opened,closed+1)
                li.pop()
            
        back_track(0,0)
        return stack
        