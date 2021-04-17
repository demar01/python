import doctest

"""First lambda example"""

ids = ['id1', 'id2', 'id30', 'id3', 'id22', 'id100']

def int_sort(generic_id):
    sorted_ids =sorted(ids, key=lambda x: int(x[2:])) # Integer sort
    return(sorted_ids)
print(int_sort(ids))

"""Second lambda example"""

my_list = [1, 5, 4, 6, 8, 11, 3, 12]
new_list = list(filter(lambda x: (x%2 == 0) , my_list)) #filter out only the even items from a list
print(new_list)

"""Third lambda example"""

full_name = lambda first, last: f'Full name: {first.title()} {last.title()}'
print(full_name("Pepa", "Perez"))

"""First list comprehension example"""

[x.capitalize() for x in ['cat', 'dog', 'cow']]

"""Second list comprehension example"""
print([x for x in range(11) if x%2 == 0])

"""Tirds list comprehension example"""
pairs = [(1, 'a'), (2, 'b'), (3, 'c')]
print(sum(x for x, _ in pairs))

print(doctest.testmod())
