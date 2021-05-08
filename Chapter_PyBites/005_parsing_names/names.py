NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']


def dedup_and_title_case_names(names):
    """Should return a list of names, each name appears only once"""
    return list(set(name.title() for name in names))


def sort_by_surname_desc(names):
    """Returns names list sorted desc by surname"""
    names = dedup_and_title_case_names(names)
    surname= [name.split()[-1] for name in names]
    return sorted(surname, reverse=True)
    #return sorted(names,key=lambda n: n.split()[-1], reverse=True)


def shortest_first_name(names):
    """Returns the shortest first name (str).
       You can assume there is only one shortest name.
    """
    names = dedup_and_title_case_names(names)
    firstname = [name.split()[0] for name in names]
    #return min(firstname, key=len)
    return sorted(firstname,key=lambda n: n.split()[0])[0]
    #return sorted(names,key=lambda n: n.split()[0] ,  key=len) I cannot do this bc it complains about duplicated keys