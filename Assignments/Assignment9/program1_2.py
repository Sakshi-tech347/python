
def ChkGreater(Value1, Value2):
     if(Value1 > Value2 ):
        return True 
     else:
         return False

def main():
    No1 = int(input("Enter first Number"))
    No2 = int(input("Enter first Number"))


    Ret =ChkGreater(No1,No2)
    if Ret==True:
        print(f"{No1} is Greater than {No2}")
    else:
        print(f"{No2} is Greater than {No1}")
        
    
if __name__ == "__main__":
    main()
