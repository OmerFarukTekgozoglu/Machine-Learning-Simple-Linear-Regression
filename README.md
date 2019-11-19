# Machine-Learning-Simple-Linear-Regression

## Linear Regression 

Linear Regression is the way to find a linear curve fitting to your data distribution in 2D-space. So this equation might be y = ax+b. In this equation y is score that dependent variable, x is score that the independent variable, b is a constant and a is the coefficient of the regression. 

For more please click on this link:  [LinearRegression](https://en.wikipedia.org/wiki/Linear_regression)

## Look at this
For example a linear regression curve:
![SalaryVsExperience](https://github.com/OmerFarukTekgozoglu/Machine-Learning-Simple-Linear-Regression/blob/master/photo/SalaryVsExperience.png?raw=true "Salary vs Experience on Train Set")

The data is actually comes from our .csv file. A simple linear regression finds the best fitted curve in order to achieve high accuracy.

**Note that:** simple linear regression can one of the best solution of the problem where the data distribute linearly. So, if the data distrubiton does not linearly seperable I recomended to don't use simple linear regression. There're other regression techniques to fits non-linear data distrubitions.

# Evaluating the Performance of the Regression Prediction
if you look at the codes, as you can see, there is a evaluating part of the regression and basically it's just evaluate our linear regression model on a subset of the train data as known as the validation / test set. Here, is the visual representation of the test set with our regression predict curve.

![LinearRegressionValidation](https://github.com/OmerFarukTekgozoglu/Machine-Learning-Simple-Linear-Regression/blob/master/photo/SalaryVsExperienceTestSet.png?raw=true "Salary vs Experience on Validation Set")
