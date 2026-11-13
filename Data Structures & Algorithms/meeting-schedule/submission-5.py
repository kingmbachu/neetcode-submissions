"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # R: The question states that there are meeting intervals, and we want to check if the start_1,end_1 clash or do not clash with the remamining of the intervals. In order for it to be a valid interval, the start of the second interval should be greater than the end of the first interval. if it is greater, that means we return True, else we return False if it less than.
# E: i) What would happen if there were no end date? ii)
# A: My approach to this problem is to first sort it in ascending order so that the start of the first interval would be less than the start of the second interval and the end of the first interval would be less than the start of the second interval.
# C: 

        intervals.sort(key = lambda i : i.start)


        for i in range(1, len(intervals)):
            i1 = intervals[i - 1]
            i2 = intervals[i]

            if i2.start < i1.end:
                return False
            
        return True

