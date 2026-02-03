def Add(Val1 ,Val2):
    Ans = Val1 + Val2
    return Ans

def main():
    No1 = int(input("Enter 1st Number :"))
    No2 = int(input("Enter 2nd Number :"))

    Ret =Add(No1 ,No2)

    print("Addition is :",Ret)


if __name__ == "__main__":
    main()
