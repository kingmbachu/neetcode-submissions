import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        mapFreq = {}
        heap = []
        output = []

        for number in nums:
            if number not in mapFreq:
                mapFreq[number] = 1
            else:
                mapFreq[number] += 1
            
        for number, count in mapFreq.items():
            heapq.heappush(heap, (count, number))

            if len(heap) > k:
                heapq.heappop(heap)

        while heap:
            number = heapq.heappop(heap)[1]
            output.append(number)

        return output

        