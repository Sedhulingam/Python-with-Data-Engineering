import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score,mean_squared_error

data = pd.read_csv("C:/Users/XED1COB/Documents/Python with data Engineering Internship/Datasets/Ecommerce Customers.csv")

X = data[['Avg. Session Length','Time on App','Time on Website','Length of Membership']]
Y = data['Yearly Amount Spent']

x_train,x_test,y_train,y_test = train_test_split(X,Y,test_size=0.2,random_state=10)

model = LinearRegression()
model.fit(x_train,y_train)

y_pred = model.predict(x_test)

print("\nAccuracy: ",round(r2_score(y_test,y_pred)*100,2))

print("\nSlope Values of each X value/Coefficient\n",)
print("\n".join(map(str,model.coef_)))
print("\n")
print("C / Intercept Value: ",model.intercept_,"\n")


X1 = data[['Avg. Session Length','Time on App','Length of Membership']]
Y1 = data['Yearly Amount Spent']

x1_train,x1_test,y1_train,y1_test = train_test_split(X1,Y1,test_size=0.2,random_state=10)

model1 = LinearRegression()
model1.fit(x1_train,y1_train)

y1_pred = model1.predict(x1_test)

print("\nAccuracy: ",round(r2_score(y1_test,y1_pred)*100,2))
print("\nMSE: ",mean_squared_error(y1_test,y1_pred))
print("\nSlope Values of each X value/Coefficient\n",)
print("\n".join(map(str,model1.coef_)))
print("\n")
print("C / Intercept Value: ",model1.intercept_,"\n")