"""Bite 15. Enumerate 2 sequences
"""
names = 'Julian Bob PyBites Dante Martin Rodolfo'.split()
countries = 'Australia Spain Global Argentina USA Mexico'.split()

def generator():
    for i, (name, country) in enumerate(zip(names,countries)):
        yield i, (name, country) #this will return ALL values

#for i in generator():
#    print(i)

def enumerate_name_countries():
        for i, (name, country) in generator():
           
            