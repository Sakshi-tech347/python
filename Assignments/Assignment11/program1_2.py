 # Count digit in Given NUmber 

def Count_of_Digit(Value1):
    Count  = 0
    
    if Value1 == 0:
        Count = Count + 1
        return Count 
    
    while Value1 > 0:
        Value1 //=10 
        Count = Count + 1

    return Count
        
    
    
def main():
    No1 = int(input("Enter A Number :"))

    Ret =Count_of_Digit(No1)
    print(f"Count of Digit is : {Ret}")
        
     
if __name__ == "__main__":
    main()
