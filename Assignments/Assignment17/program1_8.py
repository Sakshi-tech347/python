#   Enter Number of row:5

#   1
#   1       2
#   1       2       3
#   1       2       3       4
#   1       2       3       4       5
def Display_pattern(Row):
    
    for i in range(1,Row+2):
        
        for j in range(1,Row+1):
                if(i <= j):
                     print(" ",end="\t")
                     
                else:
                    print(j,end="\t")

            
        print()

        
def main():
    Value1 = int(input("Enter Number of row:"))
    

    Display_pattern(Value1)

    
if __name__ == "__main__":
    main()
