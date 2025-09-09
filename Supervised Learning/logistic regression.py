from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = pd.read_csv("C:/Users/XED1COB/Documents/Python with data Engineering Internship/Datasets/diabetes.csv")

x = data.iloc[:,:-1] #all rows all columns except the last column
y = data.iloc[:,-1] #all rows of the last column only
print(y.head()) # by default it prints the first five records of y

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2)

model = LogisticRegression()
model.fit(x_train,y_train)
y_pred = model.predict(x_test)

# Two sample inputs from the screenshot
sample_inputs = np.array([
    [6, 148, 72, 35, 0, 33.6, 0.627, 50],   # Expected: Diabetic (1)
    [1, 85, 66, 29, 0, 26.6, 0.351, 31]     # Expected: Not Diabetic (0)
])

sample_preds = model.predict(sample_inputs)

for i, pred in enumerate(sample_preds):
    print(f"Sample {i+1} → Predicted: {'Diabetic' if pred == 1 else 'Not Diabetic'}")

plt.figure(figsize=(8,6))
plt.scatter(x_test['Glucose'], x_test['BMI'], c=y_pred, alpha=0.7)
plt.xlabel("Glucose")
plt.ylabel("BMI")
plt.title("Diabetes Prediction (Test Set)")
plt.colorbar(label='Prediction (0: No Diabetes, 1: Diabetes)')
plt.grid(True)
plt.show()
plt.show()




