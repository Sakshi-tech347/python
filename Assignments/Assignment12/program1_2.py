 #print Factorial of Number

def Factorial(Value1):
    print("Factors Are: ")
    for i in range(1,Value1+1):
        if(Value1 % i == 0):
            print(i)


def main():
    No1 = int(input("Enter A Number"))

    Factorial(No1)



if __name__ == "__main__":
    main()
