class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def search(i,j,start):

            if start == len(word):
                return True
            
            if i<0 or j<0 or i >= len(board) or j >= len(board[0]) or (board[i][j]!=word[start]) or ((i,j) in path):
                return False
            
            path.add((i,j))
            result=(
                search(i,j+1,start+1)or
                search(i,j-1,start+1)or
                search(i+1,j,start+1)or
                search(i-1,j,start+1)

            )
            path.remove((i,j))
            return result
        
        path=set()
        for i in range(len(board)):
            for j in range(len(board[0])):

                if search(i,j,0):
                    return True
        return False




