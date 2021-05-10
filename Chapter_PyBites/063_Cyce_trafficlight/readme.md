# Bite 63. Use an infinite iterator to simulate a traffic light

## Description 

Complete traffic_light using itertools.cycle to return an infinite iterator to simulate a traffic light.

When called it should return a State namedtuple for each new state, here is how an islice looks:

from pprint import pprint as pp
pp(list(islice(traffic_light(), 10)))
This captures the first 10 iterated values of traffic_light into a list and pretty prints them:

[State(color='red', command='Stop', timeout=2),
 State(color='green', command='Go', timeout=2),
 State(color='amber', command='Caution', timeout=0.5),
 State(color='red', command='Stop', timeout=2),
 State(color='green', command='Go', timeout=2),
 State(color='amber', command='Caution', timeout=0.5),
 State(color='red', command='Stop', timeout=2),
 State(color='green', command='Go', timeout=2),
 State(color='amber', command='Caution', timeout=0.5),
 State(color='red', command='Stop', timeout=2)]
Good luck and have fun!