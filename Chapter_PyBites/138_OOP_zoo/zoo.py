class Animal:
    counting= 1000 #to initiate countering from 1000 everytime a class animal is called. 
    animals =[] # to keep track of animals
    
    def __init__(self, name): #it will definitely have a name attribute
        self.name = name.capitalize()
        Animal.counting += 1 #counting increasing everytime an new initialization ofthe class animal is call
        self.counting = Animal.counting
        Animal.animals.append((self.counting, self.name))
    
    def __str__(self): 
        return f"{self.counting}. {self.name}"
        
    @classmethod
    def zoo(cls):
        for a in Animal.animals:
            yield f"{a[0]}. {a[1]}"




# no need to generate a callable object but rather make it __str__ which is way that is easy to read and outputs all the members of the class.
# read a bit more about pythonic way to do constructor overloading here https://stackoverflow.com/questions/12179271/meaning-of-classmethod-and-staticmethod-for-beginner and 
#https://stackoverflow.com/questions/682504/what-is-a-clean-pythonic-way-to-have-multiple-constructors-in-python
