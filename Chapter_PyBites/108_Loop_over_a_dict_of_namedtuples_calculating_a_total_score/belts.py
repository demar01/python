
from collections import namedtuple

BeltStats = namedtuple('BeltStats', 'score ninjas')

ninja_belts = {'yellow': BeltStats(50, 11),
               'orange': BeltStats(100, 7),
               'green': BeltStats(175, 1),
               'blue': BeltStats(250, 5)}


# ninja_belts['orange'][0]
# ninja_belts['yellow'].score
# ninja_belts['yellow'].ninjas

#Lessons: we want to loop over the values of the dictionary. To access each of the entries of the dictionary (which themselves are named tuples) access the dict. values an then the values of the named tuples with a .x
#See this nice post about named tuples where they use a namedtuple Point wiht X and Y https://stackoverflow.com/questions/2970608/what-are-named-tuples-in-python#:~:text=12%20Answers&text=Named%20tuples%20are%20basically%20easy,except%20that%20they%20are%20immutable.
def get_total_points(belts=ninja_belts):
    return (belt.score*belt.ninjas for belt in belts.values())
#this will create a generator

def get_total_points(belts=ninja_belts):
    return sum(belt.score*belt.ninjas for belt in belts.values())

#this will yield a number