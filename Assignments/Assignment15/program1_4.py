from functools import reduce

Add = lambda val1,val2 :  val1 + val2

def main():

     Data = [int(x) for x in input("Enter Data :").split()]
     print(f"Actual Data is :{Data}")

     fData =(reduce(Add,Data))
     print(f"Addition of numbers is : {fData}")

      
     
if __name__ == "__main__":
    main()     