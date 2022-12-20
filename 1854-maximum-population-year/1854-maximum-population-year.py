class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        mapYrOutlook = defaultdict(int)
        listYr=set()
        for birthYr, deathYr in logs:
            mapYrOutlook[birthYr]+=1
            mapYrOutlook[deathYr]-=1
            listYr.add(birthYr)
            listYr.add(deathYr)
            
        listYr=sorted(list(listYr))
        
        currentPopulation=0
        maxPopulation=0
        maxPopulationYr=None
        for yr in listYr:
            currentPopulation+=mapYrOutlook[yr]
            if currentPopulation > maxPopulation:
                maxPopulationYr=yr
                maxPopulation=currentPopulation
        return maxPopulationYr