def ChkNum(Val1):
    if(Val1 == 0):
        print("Zero")
        
    elif(Val1 > 0):
        print("Positive  number ")
        
    else:
        print("negative number ")


def main():
    No1 = int(input("Enter a Number :"))

    Ret =ChkNum(No1 )

    

if __name__ == "__main__":
    main()
