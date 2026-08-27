class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        digi_map={
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }

        def generate(start,li):

            if len(li) > len(digits):
                return 

            if len(li) == len(digits):
                result.append("".join(li))
                return
            
            for j in range(len(digi_map[digits[start]])):

                li.append(digi_map[digits[start]][j])
                generate(start+1,li)
                li.pop()
        
        if not digits:
            return[]
        result=[]
        li=[]
        generate(0,li)
        return result


            
        