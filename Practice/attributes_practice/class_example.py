class animal():
    def __init__(self):
        print("animal created")

    def report(self):
        print("animal")

    def eat(self):
        print("eating")
    
    def sounds(self):
        print("makes noises")

#
class dog(animal):
    def __init__(self):
        animal.__init__(self)
        print("dog created")
    
    def sounds(self):
        animal.__init__(self)
        print("woof")

d = dog()
#print(d.eat())
print(d.sounds())


    


