import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt 




Border = "-"*40
##########################################################################
#   Step 1 : Load the Dataset
###########################################################################

DataSetPath = "student_performance_ml.csv"
df = pd.read_csv(DataSetPath)

print (df)
 
#      observation question 

#   Higher StudyHours increse the chance of pass
#   & also Higher Attendance improve final result 
#   when student attend every lecture then the understand every topic which is help for exam
#   & thats why there chances of pass is increase
