 

def Addition(Value1,Value2):
    Ans = 0
    Ans = Value1 + Value2
    return Ans

def Substraction(Value1,Value2):
    Ans = 0
    Ans = Value1 - Value2
    return Ans

def Multiplication(Value1,Value2):
    Ans = 0
    Ans = Value1 * Value2
    return Ans

def Division(Value1,Value2):
    Ans = 0
    Ans = Value1 / Value2
    return Ans


def main():
    No1 = int(input("Enter A First Number"))
    No2 = int(input("Enter A First Number"))


    Ret = (Addition(No1,No2))
    print(f"Additon is { Ret}")

    Ret = (Multiplication(No1,No2))
    print(f"Multiplication is { Ret}")

    Ret = (Substraction(No1,No2))
    print(f"Substraction is { Ret}")

    Ret = (Division(No1,No2))
    print(f"Division is { Ret}")



if __name__ == "__main__":
    main()
