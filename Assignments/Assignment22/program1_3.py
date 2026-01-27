
import math
class Arithmatic:
    

    def __init__(self,A,B):
        self.Value1 =A
        self.Value2 = B
        print("Object gets created succesfully")
        
    def Accept(self , C,D):
        self.no1 = C
        self.no2 = D

    def Addition(self):
        Add = self.Value1+self.Value2
        print(f"Addition is : {Add}")

    def Substraction(self):
        Sub = self.Value1 - self.Value2

        print(f"Substraction is : {Sub}")

    def Multiplication(self):
        Sub = self.Value1 * self.Value2

        print(f"Multiplication is : {Sub}")

    def Division(self):
        #issue handle division by zero
        if( self.Value2== 0):
            
            print("Cannot divide by zero")
            
        else:
            Sub = self.Value1 / self.Value2

            print(f"Division is : {Sub}")

dobj1 = Arithmatic(2,3)
dobj1.Addition()
dobj1.Substraction()
dobj1.Multiplication()
dobj1.Division()



dobj2= Arithmatic(10,0)
dobj2.Addition()
dobj2.Substraction()
dobj2.Multiplication()
dobj2.Division()

dobj3= Arithmatic(0,10)
dobj3.Addition()
dobj3.Substraction()
dobj3.Multiplication()
dobj3.Division()
