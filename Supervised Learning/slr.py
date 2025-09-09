import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error

from sklearn.model_selection import train_test_split

data1 = pd.read_csv("C:/Users/XED1COB/Documents/Python with data Engineering Internship/Datasets/Advertising.csv")

print("Print the first 5 data:\n",data1.head())

print("Total Rows: ",data1.shape[0])

print("Total columns: ",data1.columns)
print("Info: ",data1.info())

print("Correlation Matrix: ",data1.corr())
data2 = data1.corr()

# fig,axes = plt.subplots(1,2,figsize = (15,6))

# sns.pairplot(data = data1,ax=axes[0])
# plt.show()
# sns.heatmap(data1.corr(),cmap = "coolwarm",fmt=".2f",annot=True,ax=axes[1])


print("Print the first 5 data:\n",data1.head())

print("Total Rows: ",data1.shape[0])

print("Total columns: ",data1.columns)
print("Info: ",data1.info())

print("Correlation Matrix: ",data1.corr())
data2 = data1.corr()

x = data1[['TV','Radio','Newspaper']]
y = data1['Sales']

model = LinearRegression()

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3,random_state=10)

model.fit(x_train,y_train)

y_pred = model.predict(x_test)

print(r2_score(y_test,y_pred))
print(mean_absolute_error(y_test,y_pred))
print(mean_squared_error(y_test,y_pred))

sns.pairplot(data = data1)
plt.gcf().set_size_inches(8, 6)
plt.show()

sns.heatmap(data1.corr(),cmap = "coolwarm",fmt=".2f",annot=True)
plt.tight_layout()

plt.show()