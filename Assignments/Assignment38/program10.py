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
plt.figure(figsize = (7,5))

for sp in df["FinalResult"].unique():
    temp = df[df["FinalResult"]== sp]
    plt.scatter(temp["FinalResult"],temp["SleepHours"],label = sp)


plt.title("SleepHours vs FinalResult")
plt.xlabel("SleepHours")
plt.xlabel("FinalResult")

plt.legend()
plt.grid(True)
plt.show()





 
#   in this visualization i observed 
#   doing sleep more  student pass
#   & doing sleep less student fail     
