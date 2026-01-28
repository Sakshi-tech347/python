 
MaxOFThree= lambda Val1,Val2,Val3 : Val1 if (Val1 >= Val2 and Val1 >= Val3 ) else ( Val2 if Val2 >=Val3 else Val3)


def main():
    
        no1 = int(input("Enter First Number :"))
        no2 = int(input("Enter Second Number :"))
        no3 = int(input("Enter third Number :"))


        Ret =MaxOFThree(no1,no2,no3)
        print(f"Maximum   is : {Ret}")
               
if __name__ == "__main__":
    main()
