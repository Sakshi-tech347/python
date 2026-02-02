


 
 
Evn = lambda Val1 :  (Val1 % 2 ==0)  



      

def main():
     Data = list(map (int,input("Enter list of numbers : ").split()))
     print(f"Actual data is : {Data}")

     
     fData =list(filter(Evn,Data))

     print("Filter Count Even :",len(fData))
      
if __name__ == "__main__":
    main() 