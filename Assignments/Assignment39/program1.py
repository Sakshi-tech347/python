from sklearn.tree import DecisionTreeClassifier ,plot_tree
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier


#load data set
DataSetPath ="student_performance_ml.csv"
df = pd.read_csv(DataSetPath)
print(df)
 
#split data X,Y for train test
feartur_col = [
    "StudyHours",
    "Attendance",
    "PreviousScore",
    "AssignmentsCompleted",
    "SleepHours"
]

X = df[feartur_col]
Y = df["FinalResult"]

print ("X shape ",X.shape)
print ("Y shape ",Y.shape)


X_train,X_test,Y_train,Y_test = train_test_split(
    X,Y,test_size = 2,random_state = 42

)
print("Data spliting done ")

print("X",X.shape)
print("Y",Y.shape)

print("X_train",X_train.shape)
print("X_test",X_test.shape)

print("Y_train",Y_train.shape)
print("Y_test",Y_test.shape)

#Build model
print("Build the model")
model = DecisionTreeClassifier(
   
    max_depth= 3,
    random_state = 42
)

print (" model created Succefully ",model)

#train model
model.fit(X_train,Y_train)
print("Model trainning completed ")








 
