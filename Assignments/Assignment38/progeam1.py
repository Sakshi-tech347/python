import pandas as pd 




Border = "-"*40
##########################################################################
#   Step 1 : Load the Dataset
###########################################################################

print(Border)
print("Step1 : Load the DataSet")
print(Border)

DataSetPath = "student_performance_ml.csv"
df = pd.read_csv(DataSetPath)

print("DataSet get loaded succefully ")
print("Initial 5 entries from dataset  ")
print(df.head())

print("last 5 entries from dataset  ")
print(df.tail())

 

print("number of column : ",df.shape[1])
print("number of rows : ",df.shape[0])


print("list of column names :",list(df.columns))
print("Data type of column" )
print(df.dtypes)
