
#  Enter Number of row:5
#  *       *       *       *       *
#  *       *       *       *
#  *       *       *
#  *       *
#  *
def Display_pattern(Row):
    
    for i in range(Row , 0 ,-1):
        
        for j in range(i):
                print("*",end="\t")
            
        print()

        
def main():
    Value1 = int(input("Enter Number of row:"))
    

    Display_pattern(Value1)

    
if __name__ == "__main__":
    main()
