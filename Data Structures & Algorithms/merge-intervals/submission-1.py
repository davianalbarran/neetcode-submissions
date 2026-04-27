class Solution:    
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals
        
        intervals.sort()
        res = [intervals[0]]
        
        for i in range(1, len(intervals)):
            cur_interval = intervals[i]
            last_merged = res[-1]
            
            if cur_interval[0] <= last_merged[1]:
                last_merged[1] = max(last_merged[1], cur_interval[1])
            else:
                res.append(cur_interval)
        
        return res