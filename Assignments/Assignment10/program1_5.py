 #print Odd number Upto N

def Print_Odd(Value1):
    
    for i in range(1,Value1+1):
        if(i % 2 != 0):
            print(i)
    
def main():
    No1 = int(input("Enter A Number :"))

    Print_Odd(No1)
     
if __name__ == "__main__":
    main()
