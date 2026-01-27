# Function to Check Divisibility

def DivisibleByThreeOrFive(Value1):
    if(Value1 % 3 == 0 and Value1 % 5 == 0):
        return True
    else:
        return False

def main():
    No1 = int(input("Enter a Number"))
    Ret =DivisibleByThreeOrFive(No1)
    if Ret == True:
        print(f"{No1} is Divisible by Three And Five")

    else:
        print(f"{No1} is  NOT Divisible by Three And Five")

        
    
if __name__ == "__main__":
    main()
