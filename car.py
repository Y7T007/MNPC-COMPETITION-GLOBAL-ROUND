class car :
    def __init__(self, name, color, speed):
        self.name = name
        self.color = color
        self.speed = speed

    def speedUp(self):
        self.speed += 10

    def speedDown(self):
        self.speed -= 10

    def showInfo(self):
        print('Name : ', self.name)
        print('Color : ', self.color)
        print('Speed : ', self.speed)