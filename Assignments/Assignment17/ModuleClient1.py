# Q1:

import Arithmatic1
print("Inside Client :",__name__)

Result = 0

No1 =int(input(" Enter first number"))
No2 =int(input(" Enter second number"))

Result =Arithmatic1.add(No1,No2)
print(f"Addition is {Result}")

Result =Arithmatic1.Sub(No1,No2)
print(f"Substraction is {Result}")

Result =Arithmatic1.Mult(No1,No2)
print(f"Multiplication is {Result}")

Result =Arithmatic1.Div(No1,No2)
print(f"Division is {Result}")
