class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        adjacency_list = {city:[] for city in range(1, n+1)}
        for city1, city2, dist in roads:
            adjacency_list[city1].append((city2, dist))
            adjacency_list[city2].append((city1, dist))

        def DFS(city, min_score, running_path):  # 4, 5, [1,2,3]     # 3, 6, [1,2]
            running_path.add(city) # [1, 2, 3, 4]
            #if not adjacency_list[city]:
            
            for neighbour_city, dist in adjacency_list[city]:
                min_score= min( min_score, dist )
                # min_score= min( min_score, dist )  # 5  # 1, 7
                if neighbour_city in running_path:
                    # 1 -> 2 -> 4, 4 will be added in set()
                    # 1 -> 4, 
                    continue
                
                min_score= min( min_score, DFS(neighbour_city, min_score, running_path) )
                

            return min_score

        min_possible_score = DFS(1, float("inf"), set([]))
        return min_possible_score