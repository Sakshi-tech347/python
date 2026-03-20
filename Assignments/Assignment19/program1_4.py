 

#############################################
#  userdefined filtr () Map () Reduce ()
#############################################
def FilterX(Task, Elements):
    Result = list()
    for no in Elements:
        Ret = Task(no)
        if(Ret == True):
            Result.append(no)
    
    return Result


def MapX(Task , Elements):
    Result = list()
    for no in Elements:
        Ret = Task(no)
        Result.append(Ret)
    
    return Result


def ReduceX(Task,Elements):
    Sum = 0

    for no in Elements:
        Sum = Task(Sum, no)

    return Sum
        


#############################################
#  Task
#############################################
def CheckEven(No):
    if(No % 2 == 0):
        return True

def Square(No):
    return No * No

def Add(No1 , No2):
    return No1 + No2




#############################################
#  main()
#############################################

def main():
    Size = 0
    Value = 0
    Data = []

    print("Enter number of elments ")
    Size = int(input())

    print("Enter elments")

    for i in range(Size):
        Value = int(input())
        Data.append(Value)


    print("Actual Data is ",Data)

    FData = list(FilterX(CheckEven,Data))
    print("Data After Filter : ",FData)


    MData = list(MapX(Square,FData))
    print("Data After Map",MData)

    RData = ReduceX(Add,MData)
    print("Data After Reduce ", RData)

if __name__ == "__main__":
    main()

#############################################
#  Output
#############################################



#Enter number of elments
#10
#Enter elments
#5
#2
#3
#4
#3
#4
#1
#2
#8
#Actual Data is  [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]
#Data After Filter :  [2, 4, 4, 2, 8, 10]
#Data After Map [4, 16, 16, 4, 64, 100]
#Data After Reduce  204
