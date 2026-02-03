class Numbers:
    def __init__(self,A) :
        self.Value = A

    def ChekPrime(self):
        if(self.Value  <= 1):
            return False
        
        for i in range(2,self.Value):
            if self.Value % i == 0:
                return False
        
        return True
    
    def CheckPerfect(self):
        if (self.Value < 0):
            return False

        total=0
        for i in range (1 ,self.Value ):
            if(self.Value % i == 0):
                total = i + total
                if(total == self.Value):
                    return True
             
    
    def Factors(self):
        Total =0

        for i in range(1,self.Value +1):
            if(self.Value % i == 0):
                Total = i +Total 

                print(i,end= " ")
    
                
        return Total
        
    
    

def main():
    Value = int(input("Enter a number :"))

    obj1 =Numbers(Value)
    Ret =obj1.ChekPrime()
    print("Number is Prime :",Ret)

    Ret=obj1.CheckPerfect()
    print("Number is Perfect :",Ret)

    Ret = obj1.Factors()
    print(f"\nSum of Factors : {Ret}")


 

if __name__ =="__main__":
    main()



 


 
