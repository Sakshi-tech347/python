
def SumofFactors(No):
    Sum = 0
    for i in range(1,int(No/2)+1):
        if(No % i == 0):
            Sum = i + Sum
    return Sum
        
          
def main():

    Value = int(input("Enter Number:"))

    Ret =SumofFactors(Value)

    print(f"Summation  is  : {Ret}")
     
if __name__ == "__main__":
    main()
