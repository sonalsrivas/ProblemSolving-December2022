import heapq
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k=k
        self.nums=nums
        self.minheap=sorted(nums, reverse=True)[:k]
        heapq.heapify(self.minheap)

    def add(self, val: int) -> int:    # val = 1
        top = 0
        if len(self.minheap) < self.k:
            heapq.heappush(self.minheap, val)
        elif val > self.minheap[top]:         # 1 > -1
            heapq.heappop(self.minheap)
            heapq.heappush(self.minheap, val)
        return self.minheap[top]