#############################################
# userdefined filte() map() reduce()
##############################################

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
    Multiply = 1

    for no in Elements:
        Multiply = Task(Multiply , no)

    return Multiply
        
#############################################
# Task
##############################################
def rangeX(No):
    if No >= 70 and No <= 90:
        return True

def increment(No):
    return (No + 10)

def Product(A,B):
    return (A*B)

#############################################
#  main()
##############################################

def main():
    Data = []
    Value = 0
    Size =0
    print("enter number of element")
    Size = int(input())

    print("Enter Elements :")
    for i in range(Size):
        Value = int(input())
        Data.append(Value)

    print("Actual Data is : ",Data)

    FData = list(FilterX(rangeX,Data))
    print("Data After Filter :" , FData)

    MData = list(MapX(increment,FData))
    print("Data After Map :", MData )

    RData = ReduceX(Product,MData)
    print("Data After reduce :",RData)


    

if __name__ == "__main__":
    main()

#############################################
#output
##############################################

#enter number of element
#12
#Enter Elements :
#4
#34
#36
#76
#68
#24
#89
#23
#86
#90
#45
#70
#Actual Data is :  [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]
#Data After Filter : [76, 89, 86, 90, 70]
#Data After Map : [86, 99, 96, 100, 80]
#Data After reduce : 6538752000
    
