def Display_pattern(No):
     
    for i in range(No):
    
        for j in range(1,No+1):
            print(j,end="\t")
        print()

        
def main():
    Value = int(input("Enter Number:"))
    Display_pattern(Value)

     

if __name__ == "__main__":
    main()
