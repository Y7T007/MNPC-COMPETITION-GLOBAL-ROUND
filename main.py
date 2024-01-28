class hello_world :
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def print_name(self):
        print("My name is "+self.name)
        


h1 = hello_world('ysr',60)
h1.print_name()
