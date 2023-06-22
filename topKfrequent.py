class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
       # Count the frequency of each element
        freq_map = {}
        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1

     # Create a min-heap with the k most frequent elements
        heap = []
        for num, freq in freq_map.items():
            if len(heap) < k:
                heapq.heappush(heap, (freq, num))
            else:
                heapq.heappushpop(heap, (freq, num))

     # Extract the top k frequent elements from the heap
        top_k = [item[1] for item in heap]

        # Return the top k frequent elements
        return top_k[::-1]  # Reverse the list to get descending order