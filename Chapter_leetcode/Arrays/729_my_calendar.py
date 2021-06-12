class MyCalendar(object):

    def __init__(self):
        self.cal = [(0,0),(10**9,10**9)]

    def book(self, start, end):
        #binary search
        l, r= 0, len(self.cal)
        while l<r:
            mid=(l+r)//2
            if end == self.cal[mid][0]: #we compare the startpoint here
                l = mid
                break
            elif end > self.cal[mid][0]: #if endpoint is greater than start, then we move ahead 
                l = mid + 1
            else:
                r = mid #the startime that comes right before 
        #l index point that we what to find
        if start < self.cal[l-1][1]: return False
        self.cal.insert(l,(start,end))    
            

        # l index     
        return True