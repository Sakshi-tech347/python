 #print Sum Upto N Number 

def Sum_Of_N(Value1):
    Sum = 0 
    for i in range(1,Value1+1):
        Sum = i + Sum
    return Sum


def main():
    No1 = int(input("Enter A Number"))

    Ret = Sum_Of_N(No1)
    print(f"Sum of First N Natural Number is {Ret}")



if __name__ == "__main__":
    main()
