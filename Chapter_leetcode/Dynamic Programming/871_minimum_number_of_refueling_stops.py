def minRefuelStops(target, startFuel, stations):
    pq = []  # A maxheap is simulated using negative values
    output = prev = 0
    fuel=startFuel
    for distance, gas in stations +[[target,0]]:
        fuel -= distance - prev #total distance from our last station
        while pq and fuel < 0:  # must refuel in past
            fuel += -heappop(pq)
            output += 1
        if fuel < 0: return -1
        heappush(pq, -gas)
        prev = distance
    return output


# Driver Code
if __name__ == '__main__':
   target = 100
   startFuel = 10
   stations = [[10,60],[20,30],[30,30],[60,40]]
     
 
    # function call that returns the
    # answer to the problem
print(minRefuelStops(target, startFuel, stations))


# https://leetcode.com/problems/minimum-number-of-refueling-stops/discuss/1268839/Python-Solution-using-max-heap