from datetime import datetime,timedelta

NOW=datetime.now()

class Promo:
    def __init__(self,name,expires):
        self.name= name
        self.expires= expires

    @property 
    # property decorator allows us to define a method that we can access it like an attribute. 
    def expired(self):
        return True if self.expires < NOW else False

past = datetime.today() - timedelta(days=365)
future = datetime.today() + timedelta(days=365)
mypromo_past=Promo('promocion_past',past)
mypromo_future=Promo('promocion_future',future)

# print(mypromo_past.name)
# print(mypromo_past.expired)

# print(mypromo_future.name)
# print(mypromo_future.expired)