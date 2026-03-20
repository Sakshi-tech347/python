
#def power(No1 ):
#   Ans = 0
#   Ans = 1 << No1 
#   return Ans 

Power = lambda No1 : 1 << No1

def main():
    Value1 =0
    Value2 =0
    Ret =0

    print("Enter First Number")
    Value1 = int(input())

     

    Ret = Power(Value1)
    print("power of 2 ",Ret)


if __name__ == "__main__":
    main()
