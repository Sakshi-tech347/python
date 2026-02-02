
from functools import reduce

min = lambda Val1 , Val2 : Val1 if Val1 < Val2 else Val2

def main():
     Data = [int(n) for n in input("Enter Data :").split() ]
     print(f"Actual data is : {Data}")

     
     rData = reduce(min,Data)
     print(f"minimun element is : {rData}")
     
if __name__ == "__main__":
    main()     