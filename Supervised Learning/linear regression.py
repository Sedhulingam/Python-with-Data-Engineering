import pandas as pd                 
import numpy  as np                 
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
'''
About the dataset:

    Most of the students face problem with their estimate SAT score. 
    This data may help them find their approximate SAT score based on their academic performance.
'''

data=pd.read_csv('C:/Users/XED1COB/Documents/Python with data Engineering Internship/Datasets/SAT to GPA.csv')
print("Top 5 Records") 
print(data.head())    
 
print("\nTotal No of (rows,columns)",data.shape)     
 
 
x=data[['GPA']]   # X is independant  variable
y=data[['SAT']]   # y is dependant variable
 
x_train, x_test , y_train , y_test=train_test_split(x,y,test_size=0.2, random_state=0)
 
from sklearn.linear_model import LinearRegression
 
model=LinearRegression()
 
model.fit(x_train,y_train)
 
#Prediction of Test and Training set result
 
y_test_pred=model.predict(x_test)
y_train_pred =model.predict(x_train)
print(model.score(x_test,y_test)*100)

#visualizing the Test set results  
plt.figure(figsize=(12,5))

# Training data plot
plt.subplot(1,2,1)
plt.scatter(x_train, y_train, color='blue', label='Actual')
plt.scatter(x_train, y_train_pred, color='red', label='Predicted')
plt.title('Training Data: Actual vs Predicted')
plt.xlabel('GPA')
plt.ylabel('SAT')
plt.legend()

# Testing data plot
plt.subplot(1,2,2)
plt.scatter(x_test, y_test, color='blue', label='Actual')
plt.scatter(x_test, y_test_pred, color='red', label='Predicted')
plt.title('Testing Data: Actual vs Predicted')
plt.xlabel('GPA')
plt.ylabel('SAT')

plt.legend()

plt.tight_layout()
plt.show()
 
 

 
 

 