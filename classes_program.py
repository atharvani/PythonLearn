#working on classes

class PartyAnimal:
    #attributes
    x=0
    hostname=''
    #methods
    def __init__(self,pname):     #initializing the object
        self.hostname = pname
        print(self.hostname, " constructed")
    def party(self):
        self.x = self.x + 1
        print("Guests for",self.hostname, "So far ", self.x)
    def __del__(self):      #destructiong the object to free the memory
        print("I am destructed", self.x)

class Cricketfan(PartyAnimal):
    #attributes
    points = 6
    #methods
    def six(self):
        self.points = self.points + 6
        self.party()
        print(self.hostname,"points",self.points)

pa_s = PartyAnimal("Sally")  # create an instance(object) of the class
pa_s.party()
pa_m = PartyAnimal("mason")
pa_m.party()
pa_m.party()
PartyAnimal.party(pa_s)

pa_j = Cricketfan("Jim")
pa_j.party()
pa_j.six()

print("Type of object",type(pa_s))
#print("directory/ capabilities of object", dir(pa))
print("Type of attributes ", type(pa_m.x))
print("Type of methods", type(pa_m.party))
