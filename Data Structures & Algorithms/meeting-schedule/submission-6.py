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

        intervals.sort(key = lambda i : i.start)    #We sorted the the intervals object. After doing that i created an in line function using lambda which acceses the start of i.


        for i in range(1, len(intervals)):      #I then created a loop which allowed me to start at the second interval and end at the end of the interval. The reason we start at the second is because we want to compare the second with the first.
            i1 = intervals[i - 1]       #I then made varibales i1 and i2. i1 hel the first interval (index 0) and i2 held the second interval wed be comparing.
            i2 = intervals[i]

            if i2.start < i1.end:       # I then checked to see if the start of i2 was less than the end of i1. which should return False
                return False
            
        return True

