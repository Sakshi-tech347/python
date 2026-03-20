def SumofListNum(Brr):
    Sum = 0
    for no in Brr:
        Sum = Sum + no
    return Sum



def main():
    Size = 0
    Arr = []
    print("Enter Number of element :")
    Size = int(input())
    
    print("Enter element :")
    Value = 0
    for i in range(Size):
        Value = int(input( ))
        Arr.append(Value)
    
    
    print("list is : ") 
    print(Arr)

    Ret =SumofListNum(Arr)
    print("Summation of all element is :" , Ret)



if __name__ == "__main__":
    main()
