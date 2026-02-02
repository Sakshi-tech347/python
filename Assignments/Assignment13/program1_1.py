 
def Area_Of_Rect(Value1,Value2):
    Ans = 0
    Ans = Value1 * Value2
    return Ans


def main():
    Length = int(input("Enter A Length of rectangle"))
    Width = int(input("Enter A  Width of rectangle"))


    Ret = (Area_Of_Rect(Length,Width))
    print(f"Area of Rectangle is:{ Ret}")

    



if __name__ == "__main__":
    main()
