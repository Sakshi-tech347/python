def MinNumber(Brr,ele):
    Count = 0
    for no in Brr:
        if(no == ele):
            Count = Count + 1
            
    return Count        

def main():
    Size = 0
    Arr = []
    ele = 0
    print("Enter Number of Element :")
    Size = int(input())

    print("Enter Element to Search ")
    ele = int(input())

    print("Enter Element")
    Value =0
    for i in range(Size):
        Value = int(input())
        Arr.append(Value)
    
    print(Arr)

    Ret = MinNumber(Arr,ele)
    print(f"Frequency of {ele} is : {Ret}")


if __name__ == "__main__":
    main()
