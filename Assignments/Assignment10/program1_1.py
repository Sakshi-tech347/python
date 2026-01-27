# print Table of A Number

def Table(Value1):
    for i in range(1,11):
        print(Value1*i)


def main():
    No1 = int(input("Enter a Number"))
    Table(No1)
    
    
if __name__ == "__main__":
    main()
