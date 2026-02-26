import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt 




Border = "-"*40
##########################################################################
#   Step 1 : Load the Dataset
###########################################################################

DataSetPath = "student_performance_ml.csv"
df = pd.read_csv(DataSetPath)

 

plt.figure(figsize = (7,5))

for sp in df["FinalResult"].unique():   
    temp= df[df["FinalResult"]== sp]
    plt.scatter(temp["AssignmentsCompleted"],temp["FinalResult"])

plt.title("AssignmentsCompleted vs FinalResult")
plt.xlabel("AssignmentsCompleted")
plt.ylabel("FinalResult")

plt.legend()
plt.grid(True)
plt.show()





 
#   in this visualization i observed 
#   when Assinment not completed then sudets fails more 
#   and pass the sudents whose assinment completes      
