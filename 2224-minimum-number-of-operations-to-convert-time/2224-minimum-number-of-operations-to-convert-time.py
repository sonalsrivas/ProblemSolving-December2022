class Solution:
    def convertToMins(self,time):
        timeDiv =  re.findall(r"(\d\d):(\d\d)", time)
        hr, mn=map(int, timeDiv[0])
        return hr*60+mn
    def convertTime(self, current: str, correct: str) -> int:
        currentMins=self.convertToMins(current)
        correctMins=self.convertToMins(correct)
        
        noOfOperations=0
        iter_validMinIncrements=iter((60,15,5,1)) 
        operateWith = float('inf')
        while currentMins < correctMins:
            while currentMins+operateWith>correctMins:
                operateWith = next(iter_validMinIncrements)
            currentMins+=operateWith
            noOfOperations+=1
            
        return noOfOperations