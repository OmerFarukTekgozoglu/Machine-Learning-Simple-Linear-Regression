# -*- coding: utf-8 -*-

#Basic Linear Regression
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_csv('Salary_Data.csv')
X = dataset.iloc[:,:-1].values
y = dataset.iloc[:, 1].values

from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 0)

from sklearn.linear_model import LinearRegression
linear_reg = LinearRegression()
linear_reg.fit(X_train, y_train)

predict_y = linear_reg.predict(X_test)

#To see to accuracy rate
from sklearn import metrics
print("% " + str(metrics.r2_score(y_test, predict_y)*100))

#For basic visualization
plt.scatter(X_train, y_train, color = 'red')
plt.plot(X_train, linear_reg.predict(X_train), color = 'blue')
plt.title('Maaş vs Deneyim (Öğrenme seti ile)')
plt.ylabel('Maaş')
plt.xlabel('Deneyim')
plt.show()

plt.scatter(X_test, y_test, color = 'red')
plt.plot(X_train, linear_reg.predict(X_train), color = 'blue')
plt.title('Maaş vs Deneyim (Test seti ile)')
plt.ylabel('Maaş')
plt.xlabel('Deneyim')
plt.show()