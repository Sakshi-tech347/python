 
def CountDigit(No):
    Digit = 0
    Count = 0

    while(No != 0):
        Digit = No % 10
        Count = Count + 1
        No = No // 10

    return Count
    
        
def main():
  
    Value = 0
    print("Enter Number ")
    Value = int(input())

    Ret = CountDigit(Value)
    print(f"Count of Digit is : {Ret}")

    
if __name__ == "__main__":
    main()
