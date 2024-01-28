from car import car


class hello_world :
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def print_name(self):
        print("My name is "+self.name)
        


h1 = hello_world('ysr',60)
h1.print_name()


c1=car('sonata','red',0)

c1.speedUp()
c1.speedUp()
c1.speedUp()
c1.showInfo()

c1.speedDown()
c1.showInfo()