import MarvellousNum

def SumofPrime(Crr):
    Sum = 0
    for no in Crr:
        Sum = Sum + no
    return Sum


def main():
    Size = 0
    Arr = []
   
    print("Enter Number of Element :")
    Size = int(input())

     

    print("Enter Element")
    Value =0
    for i in range(Size):
        Value = int(input())
        Arr.append(Value)
    
    print(Arr)

    
    Brr = MarvellousNum.CheckPrime(Arr)

    Ret = SumofPrime(Brr)
    print(f"Summation of prime number is :{Ret} ")


if __name__ == "__main__":
    main()
