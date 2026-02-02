 # palindrom or not 

def Palindrom(Value1):
    
    revers = 0
    Number = Value1

    while Value1 > 0:
        temp =Value1 % 10

        revers = (revers* 10) + temp
        Value1 //= 10 

        
    return Number == revers



         
def main():
    No1 = int(input("Enter A Number :"))

    Ret =Palindrom(No1)
    if(Ret == True):
        print(f"{No1} is a Palindom")
    else:
        print(f"{No1} is Not Palindom")
        
     
if __name__ == "__main__":
    main()
