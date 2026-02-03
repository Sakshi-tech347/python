def Divisible_by_Five(Val1):
    return Val1 % 5 == 0
     

def main():
    No1 = int(input("Enter a Number :"))

    Ret =Divisible_by_Five(No1 )

    print(Ret)
      

if __name__ == "__main__":
    main()
