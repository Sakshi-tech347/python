class BankAccount:
    ROI = 10.5

    def __init__(self,A,B) :
            self.Name = A
            self.Amount = B

    def Display(self):
        print(f"Name : {self.Name} ")
        print(f"Amount : {self.Amount} ")
        
    def Deposite(self,Amt):
        Add = Amt + self.Amount
        self.Amount = Add    
        print(f"total Amount is {self.Amount}")                            

    def Withdraw(self,Amt):
        if(Amt < self.Amount):

            Sub =  self.Amount -Amt
            self.Amount = Sub 
            print(f"total Amount is {self.Amount}")                            

        else:
            print("Not Suffecient Balence in youre Account ")
    
    def CalulateInterest(self):
        Interest = (self.Amount * BankAccount.ROI )/100
        print(f"Interest is : {Interest}")
        print("-"*40)

obj1 = BankAccount("Raju more",100)
obj1.Display()
obj1.Deposite(100)
obj1.Withdraw(300)
obj1.CalulateInterest()


obj2 = BankAccount("Amit patil",100)
obj2.Display()
obj2.Deposite(100)
obj2.Withdraw(300)
obj2.CalulateInterest()
