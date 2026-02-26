import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt 




Border = "-"*40
##########################################################################
#   Step 1 : Load the Dataset
###########################################################################

DataSetPath = "student_performance_ml.csv"
df = pd.read_csv(DataSetPath)
 

sns.boxplot(df["Attendance"])
plt.show()





 
#  in this case   
#  60% Attendence is a  outliers 
#  95% Attendance is a  outliers
#  there are in  box range  70 to 90 percente attendance   
