chkOdd = lambda Val :(Val % 2 != 0)

def main():
     Data = [int(X) for  X in  input("Enter Data :").split()]
     print(f"Actual Data is : {Data}")

     fData = list(filter(chkOdd,Data))
     print(f"Odd Data : {fData}")

if __name__ == "__main__":
    main()