 # Sum of Digit digit in Given NUmber 

def Sum_of_Digit(Value1):
    Sum = 0
    
    if Value1 == 0:
        Count = Count + 1
        return Count 
    
    while Value1 > 0:
        Digit = 0
        Digit =Value1 % 10 
        Sum = Sum +Digit
        Value1 //=10 
         
    return Sum
     
        
    
    
def main():
    No1 = int(input("Enter A Number :"))

    Ret =Sum_of_Digit(No1)
    print(f"Total Sum of Digit is :{Ret}")
        
     
if __name__ == "__main__":
    main()
