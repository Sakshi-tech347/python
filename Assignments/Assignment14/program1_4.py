 
Minimum = lambda Value1,Value2 : (Value1 > Value2)


def main():
    
        no1 = int(input("Enter First Number :"))
        no2 = int(input("Enter Second Number :"))

        Ret =Minimum(no1,no2)
        if(Ret == True):
                print(f"{no1} is Minimum")
        else:
                print(f"{no2} is Miminum")
               
if __name__ == "__main__":
    main()
