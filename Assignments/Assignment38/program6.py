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

print("Class Distribution (StudyHours)")
print(df["StudyHours"].value_counts)

sns.histplot(df["StudyHours"])
plt.show()

 
