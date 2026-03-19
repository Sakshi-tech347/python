def CheackPrime(No):
    if No <= 1:
        return False
    else:
        for i in range(2,No):
            if(No % i == 0):
                return False
        return True
        
def main():
    Value = int(input("Enter Number:"))
    Ret =CheackPrime(Value)

    if(Ret ==  True ):
        print("It is Prime Number ")
    else:
        print("It is NOT Prime Number ")

if __name__ == "__main__":
    main()
