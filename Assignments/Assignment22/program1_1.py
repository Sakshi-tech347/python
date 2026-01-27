class Demo:
    Value = 1

   
    def __init__(self,A,B):
        self.no1= A
        self.no2= B
        
    def fun(self):
        print("Inside fun")
        print(self.no1)
        print(self.no2)

    def gun(self):
        print("Inside gun")

        print(self.no1)
        print(self.no2)

dobj1 = Demo(11,21)
dobj2 = Demo(51,101)

dobj1.fun()
dobj2.fun()

dobj1.gun()
dobj2.gun()


