import pandas as pd
import pickle
import sys
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.svm import SVR
from sklearn import linear_model

# Reading dataset
df = pd.read_csv('sample_db.csv')

# Label Encoding for Gender column
mycol = df[["Victim_Gender"]]
for i in mycol:
    cleanup_nums = {i: {"M": 0, "F": 1, "T": 2, "N":3}}
    df = df.replace(cleanup_nums)

# Feeding parameters 
feed = df[['Victim_Gender', 'Population_Density', 'Average_Age', 'Average_Income', 
           'Police_Station_Count', 'Petroling_Vans', 'Morality_level', 'Crime_Rate',
           'Rating', 'Overall_Preferred_index']]

# # Drop target column
df_train_x = feed.drop('Overall_Preferred_index',axis = 1)

# Target variable column
df_train_y = feed['Overall_Preferred_index']

# Train-test Splitting
x_train, x_test, y_train, y_test = train_test_split(df_train_x, df_train_y, test_size=0.20, random_state=42)


# Model 1 - Linear Regression
m1 = LinearRegression()
m1.fit(x_train, y_train)

# print(res1)

# Model 2 -  Decision Tree Regressor
m2 = DecisionTreeRegressor()
m2.fit(x_train, y_train)

# print(res2)

# Model 3 - Support Vector Regressor
m3 = SVR()
m3.fit(x_train, y_train)

# print(res3)

# Model 4 - Lasso Regressor
m4 = linear_model.Lasso(alpha=0.1)
m4.fit(x_train, y_train)

# Linear Regression
file2 = open('model2.sav', 'wb') 
pickle.dump(m1, file2)
file2.close()

# Decision Tree Regressor
file3 = open('model3.sav', 'wb') 
pickle.dump(m2, file3)
file3.close()

# Support Vector Regressor
file4 = open('model4.sav', 'wb') 
pickle.dump(m3, file4)
file4.close()

# Lasso Regressor
file5 = open('model5.sav', 'wb') 
pickle.dump(m4, file5)
file5.close()

print("All Model Building Done!")

#import pickle
#pickle.dump(log_model,open("titanic_survival_ml_model.sav", "wb"))