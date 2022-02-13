class Something:
    def __init__(self, somepart, somepart3):
        self.somepart = somepart
        #self.somepart2 = somepart2
        print(somepart)
        #print(somepart2)
        self.somepart4 = "test2"

    def add_one(self):
        print("print..something")

    def add_two(self,x):
        return x + 1
        
    somepart3 = "test"

s = Something("first", "second")
print(s.add_two(2))

print(s.somepart3)
print(s.somepart4)
