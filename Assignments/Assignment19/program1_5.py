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
    Max = Elements[0] 

    for no in Elements:
        Max = Task(Max , no)

    return Max
        

#############################################
#  Task
#############################################

def Prime(No):
    if(No <= 1 ):
        return False
    else :
        for i in range(2,No):
            if(No % i == 0):
                return False
    return True

def Multiply(No):
    return No * 2

def Max(No1 , No2):
    Result = 0

    if(No1 > No2 ):
        return No1
    else:
        return No2



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

    FData = list(FilterX(Prime,Data))
    print("Data After Filter : ",FData)


    MData = list(MapX(Multiply,FData))
    print("Data After Map",MData)

    RData = ReduceX(Max,MData)
    print("Data After Reduce ", RData)

if __name__ == "__main__":
    main()


#Enter number of elments
#8
#Enter elments
#2
#17
#11
#10
#70
#23
#31
#77
#Actual Data is  [2, 17, 11, 10, 70, 23, 31, 77]
#Data After Filter :  [2, 17, 11, 23, 31]
#Data After Map [4, 34, 22, 46, 62]
#Data After Reduce  62
