 
def SumofDigit(No):
    Digit = 0
    Sum = 0

    while(No != 0):
        Digit = No % 10
        Sum = Sum + Digit
        No = No // 10

    return Sum
    
        
def main():
  
    Value = 0
    print("Enter Number ")
    Value = int(input())

    Ret = SumofDigit(Value)
    print(f"Summation of Digit is : {Ret}")

    
if __name__ == "__main__":
    main()
