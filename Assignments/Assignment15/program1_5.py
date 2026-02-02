
from functools import reduce

max = lambda Val1 , Val2 : Val1 if Val1 > Val2 else Val2

def main():
     Data = [int(n) for n in input("Enter Data :").split() ]
     print(f"Actual data is : {Data}")

     
     rData = reduce(max,Data)
     print(f"Maximum element is : {rData}")
     
if __name__ == "__main__":
    main()     