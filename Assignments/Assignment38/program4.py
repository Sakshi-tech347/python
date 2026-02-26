import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt 




Border = "-"*40
##########################################################################
#   Step 1 : Load the Dataset
###########################################################################

DataSetPath = "student_performance_ml.csv"
df = pd.read_csv(DataSetPath)

print(df)

print("Class Distribution (FinalResult)")
print(df["FinalResult"].value_counts)

df['pass percentage'] = (df['FinalResult'] / (df["FinalResult"]==0).sum()) * 100
df['Fail percentage'] = (df['FinalResult'] / (df["FinalResult"]==1).sum()) * 100

print(df["pass percentage"])
print(df["Fail percentage"])

sns.countplot(x="FinalResult",data = df)
plt.title("Class Disribution ")
plt.show()


#not balemced 
# no of  passed students are more than fail students 

 
