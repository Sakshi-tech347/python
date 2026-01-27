import math

class Circle:
    PI = 3.14

    def __init__(self,A):
         self.Radius = A
         self.Area =0.0
         self.Circumference = 0.0
         
         print("Object gets created succefully")

    def Accept(self,A):
        self.Radius = A

    def CalculateArea(self):
        self.Area =Circle.PI * self.Radius *self.Radius

    def CalculateCircleCircumference(self):
        self.Circumference = 2* Circle.PI * self.Radius

    def Display(self):
        
        self.CalculateArea()
        self.CalculateCircleCircumference()

        print(f"Radius :{self.Radius}")
        print(f"Area :{self.Area}")
        print(f"Circumference:{self.Circumference}")
        

dobj1 =Circle(3)
dobj1.Display()

dobj2 =Circle(4)
dobj2.Display()
