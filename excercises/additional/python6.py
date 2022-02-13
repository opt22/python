#1 List all items in list along with the department number for the email.
#
data = [
{ "Google": ["google@one.com 123", "google@two.com 321", "google@three.com 451", "google@five.com 123" ]},
{ "Yahoo": ["test@test.com 123", "test@test.com 321", "test@test.com 451", "test@test.com 451" ]},
{ "IBM": ["test@test.com 888", "test@test.com 123", "test@test.com 888", "test@test.com 123" ]},
{ "GREGS": ["test@test.com 123", "test@test.com 888", "test@test.com 123", "test@test.com 123" ]},
{ "AUTO-SHOP": ["test@test.com 888", "test@test.com 555", "test@test.com 555", "test@test.com 123" ]},
{ "PAWN-SHOP": ["test@test.com 123", "test@test.com 123", "test@test.com 123", "test@test.com 123" ]},
{ "Nike": ["test@test.com 123", "test@test.com 123", "test@test.com 555", "test@test.com 123" ]},
{ "Franks": ["test@test.com 123", "test@test.com 888", "test@test.com 555", "test@test.com 123" ]},
{ "Tims": ["test@test.com 123", "test@test.com 123", "test@test.com 888", "test@test.com 123" ]},
{ "Apple": ["test@test.com 123", "test@test.com 555", "test@test.com 123", "test@test.com 123" ]},
{ "Sony": ["test@test.com 123", "test@test.com 123", "test@test.com 123", "test@test.com 123" ]},
{ "Disney": ["test@test.com 123", "test@test.com 888", "test@test.com 123", "test@test.com 123" ]},
{ "Popies": ["test@test.com 123", "test@test.com 123", "test@test.com 123", "test@test.com 123" ]},
{ "Sally": ["test@test.com 123", "test@test.com 555", "test@test.com 888", "test@test.com 123" ]},
{ "Henry": ["test@test.com 123", "test@test.com 555", "test@test.com 555", "test@test.com 555" ]},
{ "Dave's": ["test@test.com 123", "test@test.com 888", "test@test.com 555", "test@test.com 123" ]}
]

asdf = { "Google": ["google@one.com 123", "google@two.com 321", "google@three.com 451", "google@five.com 123" ]}

for i in data:
    vlist=(list((i.values()))[0])
    comp=(list((i.keys()))[0])
    for x in vlist:
        print(f"{comp} : {x}")

 #2. Create me a class called human, and give it at least 5 properties, and create one method, that lists all the properties of that human's instance. 
#
class Human:
    def __init__(self, height, weight, eyes, hair, feet):
        self.height = height
        self.weight = weight
        self.eyes = eyes
        self.hair = hair
        self.feet = feet

    def getprops(self):
        return self.height, self.weight, self.eyes, self.hair, self.feet

h = Human(3,40,"green","black","small")
print(h.getprops())

#3. What are some HTTP Verbs we can use? 
    #-GET
    #-POST
    #-PUT
    #-PATCH
    #-DELETE
    #-COPY
    #-HEAD
    #-OPTIONS
    #-LINK
    #-UNLINK
    #-PURGE
    #-LOCK
    #-UNLOCK
    #-PROPFIND
    #-VIEW

#4. What is flask? (edited) 
#    Flask is a python library that adds functionality to create an api that 
#    allows passing of data to and from a database.

