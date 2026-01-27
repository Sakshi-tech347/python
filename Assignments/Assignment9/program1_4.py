# Function to Calculate cube of Number

def Cube(Value1):
      Sqr = Value1 * Value1 *Value1
      return Sqr

def main():
    No1 = int(input("Enter a Number"))
    Ret =Cube(No1)
    print(f"Cube of {No1} is : {Ret}")
     
        
    
if __name__ == "__main__":
    main()
