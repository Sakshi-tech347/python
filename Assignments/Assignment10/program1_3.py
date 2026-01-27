 #print Factorial of Number

def Factorial(Value1):
    Fact = 1
    for i in range(1,Value1+1):
        Fact = i * Fact
    return Fact


def main():
    No1 = int(input("Enter A Number"))

    Ret = Factorial(No1)
    print(f"Factorial of Number is {Ret}")



if __name__ == "__main__":
    main()
