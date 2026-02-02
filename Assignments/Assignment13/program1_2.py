 

def Area_Of_Circle(Value):
    Ans =  3.14 * Value *Value
    return Ans

 
def main():
    Radius = int(input("Enter A Radius"))


    Ret = (Area_Of_Circle(Radius))
    print(f"Area of Circle is:{ Ret}")

    

if __name__ == "__main__":
    main()
