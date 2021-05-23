def transpose(data):
    """Transpose a data structure
    1. dict
    data = {'2017-8': 19, '2017-9': 13}
    In:  transpose(data)
    Out: [('2017-8', '2017-9'), (19, 13)]
    2. list of (named)tuples
    data = [Member(name='Bob', since_days=60, karma_points=60,
                   bitecoin_earned=56),
            Member(name='Julian', since_days=221, karma_points=34,
                   bitecoin_earned=78)]
    In: transpose(data)
    Out: [('Bob', 'Julian'), (60, 221), (60, 34), (56, 78)]
    """
    if isinstance(data, dict):
        return [data.keys(), data.values()]
    return list(zip(*data)) #unpacking opertor

# data = {'2017-8': 19, '2017-9': 13}
# transpose(data)
# data = [Member(name='Bob', since_days=60, karma_points=60,bitecoin_earned=56)]
# transpose(data)

# pairs = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
# numbers, letters = zip(*pairs) #unpacking opertor
# #https://realpython.com/python-zip-function/