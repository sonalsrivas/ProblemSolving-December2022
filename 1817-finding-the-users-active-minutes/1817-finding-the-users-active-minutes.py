class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        mapUserIDToTimeSet=defaultdict(set)
        for userID, time in logs:
            mapUserIDToTimeSet[userID].add(time)
        mapUserIDToTimelen={}
        for userID in mapUserIDToTimeSet:
            mapUserIDToTimelen[userID]=len(mapUserIDToTimeSet[userID])
        answer=[0]*k
        for userID, time in mapUserIDToTimelen.items():
            answer[time-1]+=1
        return answer