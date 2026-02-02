
from functools import reduce


product = lambda Val1 , Val2:Val1 *Val2
 

def main():
     Data = list(map (int,input("Enter list of numbers : ").split()))
     print(f"Actual data is : {Data}")

     
     rData =reduce(product,Data)
     print(f"After reduced data is : {rData}")

     
if __name__ == "__main__":
    main() 