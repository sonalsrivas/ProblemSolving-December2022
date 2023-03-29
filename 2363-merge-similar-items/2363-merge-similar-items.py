class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        map_value_weight = defaultdict(int)
        for v,w in items1:
            map_value_weight[v]+=w
        for v,w in items2:
            map_value_weight[v]+=w
        
        return [[v,map_value_weight[v]] for v in sorted(map_value_weight.keys())]