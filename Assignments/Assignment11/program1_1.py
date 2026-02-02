 #Check prime 

def ChkPrime(Value1):

    
        if(Value1 <= 1):
            return False
        else:
            for i in range(2,Value1):
                if(Value1 % i == 0):
                    return False
    
        return True
        
    
    
def main():
    No1 = int(input("Enter A Number :"))

    Ret =ChkPrime(No1)
    if(Ret == True):
        print(" Number is Prime ")
    else:
        print(" Number  is Not  Prime ")
        
     
if __name__ == "__main__":
    main()
