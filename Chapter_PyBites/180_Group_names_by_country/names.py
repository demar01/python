from collections import defaultdict

data = """last_name,first_name,country_code
Watsham,Husain,ID
Harrold,Alphonso,BR
Apdell,Margo,CN
Tomblings,Deerdre,RU
Wasielewski,Sula,ID
Jeffry,Rudolph,TD
Brenston,Luke,SE
Parrett,Ines,CN
Braunle,Kermit,PL
Halbard,Davie,CN"""

def group_names_by_country(data: str = data) -> defaultdict:
    countries = defaultdict(list)
    for line in data.splitlines():
        name, surname, country = line.split(",")
        countries[country].append(f"{surname} {name}")
    return countries

#group_names_by_country(data)

# dep = [('Sales', 'John Doe'),
#        ('Sales', 'Martin Smith'),
#        ('Accounting', 'Jane Doe'),
#        ('Marketing', 'Elizabeth Smith'),
#        ('Marketing', 'Adam Doe')]

# from collections import defaultdict

# dep_dd = defaultdict(list)
# for department, employee in dep:
#     dep_dd[department].append(employee)

# set(dir(defaultdict)) - set(dir(dict))