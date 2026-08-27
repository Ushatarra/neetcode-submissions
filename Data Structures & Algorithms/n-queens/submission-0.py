class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        cols=set()
        pos_daig=set()
        neg_daig=set()
        result=[]
        board=[['.']* n for i in range(n)]

        def generate(row):

            if row == n:
                copy=["".join(i) for i in board]
                result.append(copy)
                return 
            
            for c in range(n):

                if c in cols or (row+c) in pos_daig or (row-c) in neg_daig:
                    continue
                
                cols.add(c)
                pos_daig.add((row+c))
                neg_daig.add((row-c))
                board[row][c]="Q"
                generate(row+1)
                cols.remove(c)
                pos_daig.remove((row+c))
                neg_daig.remove((row-c))
                board[row][c]="."

        generate(0)
        return result
        