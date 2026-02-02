


 
 
CountWord_inString = lambda Val1 :  len(Val1) > 5  

def main():
     Data = input("Enter list of string : ").split()
     print(f"Actual data is : {Data}")

     
     fData =list(filter(CountWord_inString,Data))

     print(" String Which is gtr than 5 letter :",(fData))
      
if __name__ == "__main__":
    main() 