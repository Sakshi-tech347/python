 

def Print_Reverse(Value1):
     
     for i in range( Value1 ,0 , -1):
         print(i ,end ="\t")


def main():
    No1 = int(input("Enter A First Number"))
   
    Print_Reverse(No1)



if __name__ == "__main__":
    main()
