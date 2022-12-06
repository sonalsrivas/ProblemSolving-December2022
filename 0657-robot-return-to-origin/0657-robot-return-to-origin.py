class Solution:
    def judgeCircle(self, moves: str) -> bool:
        
        xCoord, yCoord = 0,0
        
        for move in moves:
            if move == 'R':
                xCoord+=1
            elif move == 'L':
                xCoord-=1
            elif move == 'U':
                yCoord+=1
            else:
                yCoord-=1
            
        
        return xCoord==yCoord==0