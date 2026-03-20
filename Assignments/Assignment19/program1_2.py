
#def Multiply(No1 , No2):
#   Ans = 0
#   Ans = No1 * No2 
#   return Ans 

Multiply = lambda No1,No2 : No1 *No2

def main():
    Value1 =0
    Value2 =0
    Ret =0

    print("Enter First Number")
    Value1 = int(input())

    print("Enter Second Number")
    Value2 = int(input())

    Ret = Multiply(Value1,Value2)
    print("Multiplication is ",Ret)


if __name__ == "__main__":
    main()
