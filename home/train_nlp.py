import warnings
warnings.filterwarnings('ignore')

import os
import pandas as pd
import re
import string
import pickle

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score, precision_score, recall_score


data = pd.read_csv('train.csv') #https://www.kaggle.com/datasets/anu0012/hotel-review?select=train.csv

data.drop(columns=['User_ID', 'Browser_Used', 'Device_Used'], inplace=True)


def text_clean(text):
    text=text.lower()
    rext=re.sub('\[.*?\]','',text)
    text=re.sub('[%s]'%re.escape(string.punctuation),'',text)
    text=re.sub('\w*\d\w\*','',text)
    return text

def text_clean2(text):
    text=re.sub('\n','',text)
    return text

cleaned=lambda x:text_clean(x)

data['cleaned_desc']=pd.DataFrame(data.Description.apply(cleaned))

cleaned2=lambda x:text_clean2(x)

data['cleaned_new']=pd.DataFrame(data['cleaned_desc'].apply(cleaned2))


indep = data.cleaned_new
dep = data.Is_Response


X_train, X_test, Y_train, Y_test = train_test_split(indep, dep, test_size=0.1, random_state=225)

tvec = TfidfVectorizer()
clf2 = LogisticRegression(solver='lbfgs')

model = Pipeline([('vectorizer', tvec), ('classifier', clf2)])
model.fit(X_train, Y_train)


predictions = model.predict(X_test)
#confusion_matrix(predictions, Y_test)
print("Accuracy: ", accuracy_score(predictions, Y_test))

nlp = open('nlp.sav', 'wb') 
pickle.dump(model, nlp)
nlp.close()