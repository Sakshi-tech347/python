
def BinaryEquivalent(Value):
     
        BinEqui =[]
        

        while(Value > 0):
            binary =Value %2 
            BinEqui.append(str(binary))
            Value //= 2
    
        BinEqui.reverse()
        return"".join(BinEqui)

def main():
    No1 = int(input("Enter A Number"))


    Ret =BinaryEquivalent(No1)
    print(Ret)
  

if __name__ == "__main__":
    main()
