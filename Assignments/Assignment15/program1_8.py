
from functools import reduce

Div = lambda Value: Value % 3 == 0 and Value %5 == 0

def main():
     Data = list(map (int,input("Enter list of numbers : ").split()))
     print(f"Actual data is : {Data}")

     
     fData= list(filter(Div,Data))
     print(f"Data After Filter  : {fData}")

     
if __name__ == "__main__":
    main()     