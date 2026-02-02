 

def Display_Grade(Value):
    match Value:
        
        case _ if Value >= 75 :
                return "Distinction"
            
        case _ if Value >= 60 :
                return "First Class"
            
        case _ if Value >= 50:
                return "Second Class"
            
        case _ if Value < 50 :
                return "Fail"
            
        case _:
            return "Invalid input"


def main():
    Marks = (int(input("Enter Marks")))

    Ret =Display_Grade(Marks)
    print(Ret)
     

     

    



if __name__ == "__main__":
    main()
