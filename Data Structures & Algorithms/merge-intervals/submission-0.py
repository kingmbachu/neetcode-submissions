class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        # R: The question is asking us to return a list of arrays intervals that do not overlap with each other and merge all overlapping intervals.
        # E: i) Are we assuming the list is sorted?
        # A: 
        # c:

    

        intervals.sort(key = lambda i : i[0]) # we sort by using lambda and passing i which will take the the first element of each inner list. so we are sorting based on each inner list i[0]
        output = [intervals[0]] #we want to start our output with the very first interval. so its either you merge, or you dont overlap(be added as a new interval)

        for start, end in intervals[1:]: #We want to start iterating through intervals from index 1 till the end. The need for start and end is to unpack so eg: start = i[0], end = i[1]
            lastEnd = output[-1][1] # lastEnd allows to store the output evereytime we check the condition below. output[-1] gives us the the last list, while output[1] allows us to access the last interval in the the last interval list. so basically accessing the elemnt at the end of the interval

            if start <= lastEnd:   # This statement is to check if the start of of the interval is less than the lastEnd figure we are looking at, if its true then we will get the max between the lastEnd and the end. We do this to merge the numbers.
                output[-1][1] = max(lastEnd, end) 
            else:
                output.append([start,end])  #If it is not, then we just add the interval into the list
        return output     
        
            

                