import heapq
from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        negative_stones = [-stone for stone in stones]
        heapq.heapify(negative_stones)
        
      
        while len(negative_stones) > 1:
            first = -heapq.heappop(negative_stones)
            second = -heapq.heappop(negative_stones)
            
            if first > second:
                new_stone = first - second
               
                heapq.heappush(negative_stones, -new_stone)
        
        return -negative_stones[0] if negative_stones else 0
