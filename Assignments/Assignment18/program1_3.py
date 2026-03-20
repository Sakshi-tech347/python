def MinNumber(Brr):
    min = Brr[0]
    for no in Brr:
        if(min > no):
            min = no
    return min        

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

    Ret = MinNumber(Arr)
    print("Minimum number is : ",Ret)


if __name__ == "__main__":
    main()
