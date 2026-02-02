 # print of Digit digit (reverse) in Given NUmber 

def Sum_of_Digit(Value1):
    
    if Value1 == 0:
        Count = Count + 1
        return Count 
    
    while Value1 > 0:
        Digit = 0
        Digit =Value1 % 10 
        print(Digit)
        Value1 //=10 
         
def main():
    No1 = int(input("Enter A Number :"))

    Sum_of_Digit(No1)
        
     
if __name__ == "__main__":
    main()
