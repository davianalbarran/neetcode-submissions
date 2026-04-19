class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_tracker = {}

        for i in nums:
            if i in freq_tracker:
                freq_tracker[i] += 1
            else:
                freq_tracker[i] = 1
        
        sorted_dict = dict(reversed(sorted(freq_tracker.items(), key=lambda item: item[1])))

        return [key for key, val in sorted_dict.items()][:k]


