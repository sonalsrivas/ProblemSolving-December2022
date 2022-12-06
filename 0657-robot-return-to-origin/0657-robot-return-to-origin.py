class Solution:
    def judgeCircle(self, moves: str) -> bool:
        
        xCoord, yCoord = 0,0
        
        def Rmove(xCoord, yCoord):
            xCoord+=1
            return xCoord, yCoord
        def Lmove(xCoord, yCoord ):
            xCoord-=1
            return xCoord, yCoord
        def Umove(xCoord, yCoord):
            yCoord+=1
            return xCoord, yCoord
        def Dmove(xCoord, yCoord):
            yCoord-=1
            return xCoord, yCoord
        
        mapMoves={'U':Umove, 'D':Dmove, 'R':Rmove, 'L':Lmove}
        for move in moves:
            xCoord, yCoord = mapMoves[move](xCoord, yCoord)
        
        return xCoord==yCoord==0