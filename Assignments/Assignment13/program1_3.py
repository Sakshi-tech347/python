 

def Chk_Perfect(Value):
    Sum = 0
    if(Value < 0):
        return False
    
    for i in range(1,Value +1):
        if(Value % i == 0):
            Sum = i + Sum
            if(Sum == Value):
                return True
    

def main():
    No1 = int(input("Enter A Number"))


    Ret = (Chk_Perfect(No1))
    if Ret == True:
        print("is a Perfect number ")

    else:
        print("is NOT Perfect number ")

if __name__ == "__main__":
    main()
