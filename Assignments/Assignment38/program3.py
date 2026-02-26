import pandas as pd 




Border = "-"*40
##########################################################################
#   Step 1 : Load the Dataset
###########################################################################

DataSetPath = "student_performance_ml.csv"
df = pd.read_csv(DataSetPath)

print(df)

print("Average of StudyHours",df["StudyHours"].mean())
print("Average of Attendance",df["Attendance"].mean())
print("Maximum of Attendance",df["PreviousScore"].max())
print("Minimum of SleepHours",df["SleepHours"].min())
