"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) <= 1:
            return True
        
        intervals.sort(key=lambda x: (x.start, x.end))
        prev_end = intervals[0].end

        for interval in intervals[1:]:
            start, end = interval.start, interval.end

            if prev_end > start:
                return False
            
            prev_end = end
            
        return True
        