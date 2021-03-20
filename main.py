import pandas
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
data=pandas.read_csv("results.csv")
print(data.head())
plt.scatter(data['Hours'],data['Scores'])
plt.show()
model=LinearRegression()
model.fit(data[['Hours']],data[['Scores']])
Hours=float(input("Give the no of hours Student Study\n"))
print(model.predict([[Hours]]))