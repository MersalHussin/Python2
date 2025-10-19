class cat:
    def __init__(self,name,color,type,age,doeswalk,doesrun,doesmeow):
        self.name = name
        self.color = color
        self.type = type
        self.age = age
        self.doesrun = doesrun
        self.doeswalk = doeswalk
        self.doesmeow = doesmeow
    
    def iswalking(self,speed):
        result = f"my name is: {self.name} and my type is {self.type} my age is {self.age}"
        if(self.doeswalk):
            print(f"{result} and can walk with {speed} step/s")
        else:
            print(f"{result} and can't moewing")
    
    def isrunning(self,speed):
        result = f"my name is: {self.name} and my type is {self.type} my age is {self.age}"
        if(self.doesrun):
            print(f"{result} and can running with {speed} step/s")
        else:
            print(f"{result} and can't running")
    
    def isMeowing(self):
        result = f"my name is: {self.name} and my type is {self.type} my age is {self.age}"
        if(self.doesmeow):
            print(f"{result} and can meowing")
        else:
            print(f"{result} and can't moewing")
    
