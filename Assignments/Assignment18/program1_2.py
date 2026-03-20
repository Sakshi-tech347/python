def MaxNumber(Brr):
    max = Brr[0]
    for no in Brr:
        if(max < no):
            max = no
    return max        

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

    Ret = MaxNumber(Arr)
    print("Maximum number is : ",Ret)


if __name__ == "__main__":
    main()
