def ChkNum(Val):
    Ans = Val % 2 == 0
    return Ans

def main():
    No = int(input("Enter a Number :"))
    Ret =ChkNum(No)

    if(Ret == True):
        print("Even number ")

    else:
        print("odd number ")


if __name__ == "__main__":
    main()
