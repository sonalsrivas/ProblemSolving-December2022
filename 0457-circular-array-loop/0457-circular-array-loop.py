class Solution:
    
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n=len(nums)
        neighbour_list = [0]*n
        for i in range(n):
            neighbour_list[i] = normalize_index(nums[i] + i, n)
        for i in range(n):
            result = traverse_and_find_cycle(i, nums, neighbour_list, set([]), n)
            if result:
                return True
        return False
        
            
def traverse_and_find_cycle( node, nums, neighbour_list, visitor_set, n, track_seq_pos=0, track_seq_neg=0):
    if nums[node] >=0 :
        track_seq_pos+=1
    else:
        track_seq_neg+=1
    if not (track_seq_pos==0 or track_seq_neg==0):
        return False
    #print(track_seq_pos, track_seq_neg)
    if node in visitor_set:
        return True
    visitor_set.add(node)
    next_node = neighbour_list[node]
    if next_node == node:
        return False
    return traverse_and_find_cycle( next_node, nums, neighbour_list, visitor_set, n, track_seq_pos, track_seq_neg)
    
    
def normalize_index(x, array_length):
    return x % array_length
    