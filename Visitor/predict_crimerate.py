import sys
import pickle
import numpy as np


# Linear Regression
file2 = open('../model2.pkl', 'rb') 
m1 = pickle.load(file2)
file2.close()


# Decision Tree Regressor
file3 = open('../model3.pkl', 'rb') 
m2 = pickle.load(file3)
file3.close()

# Support Vector Regressor
file4 = open('../model4.pkl', 'rb') 
m3 = pickle.load(file4)
file4.close()

# Lasso Regressor
file5 = open('../model5.pkl', 'rb') 
m4 = pickle.load(file5)
file5.close()

gender = sys.argv[1] # 0: M , 1:F, 2:T, 3:None # FROM USER
density = sys.argv[2] # FROM LOCALITY DB
age = sys.argv[3] # FROM LOCALITY DB
income = sys.argv[4] # FROM LOCALITY DB
policestationcount = sys.argv[5] # FROM LOCALITY DB
petrolingvans = sys.argv[6] # FROM LOCALITY DB
moralitylevel = sys.argv[7] # FROM LOCALITY DB

userdata = [[gender, density, age, income , policestationcount, petrolingvans, moralitylevel]]

res1 = m1.predict(userdata)
res2 = m2.predict(userdata)
res3 = m3.predict(userdata)
res4 = m4.predict(userdata)


if(res1 < 0):
    res1 = 0

if(res2 < 0):
    res2 = 0

if(res3 < 0):
    res3 = 0

if(res4 < 0):
    res4 = 0

finalcrimerate = (res1 + res2 + res3 + res4) / 4

print(finalcrimerate)
