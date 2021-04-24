from itertools import zip_longest

names = 'Tim Bob Julian Carmen Sofia Mike Kim Andre'.split()
locations = 'DE ES AUS NL BR US'.split()
confirmed = [False, True, True, False, True]

# # the problem: zip truncates string to shotest available value and so some values are missing3
# set(zip(names, locations, confirmed))

# #the solution:
# set(zip_longest(names, locations, confirmed, fillvalue='-'))

def get_attendees():
    for participant in zip_longest(names, locations, confirmed, fillvalue='-'):
        print(participant)

#to make the output visible
if __name__ == '__main__':
    get_attendees()