print('begin')
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
import sys


df = pd.read_csv('titanic/train.csv')

keep_cols =["Survived","Pclass","Sex","Age","SibSp","Parch","Fare","Cabin","Embarked"]

df = df[keep_cols]



def convert_sex_to_int(sex):
  if sex == "male":
    return 0
  if sex == "female":
    return 1

df['Sex'] = df['Sex'].apply(convert_sex_to_int)


age_nan = df['Age'].apply(lambda entry: np.isnan(entry))
age_not_nan = df['Age'].apply(lambda entry: not np.isnan(entry))

mean_age = df['Age'][age_not_nan].mean()
df['Age'][age_nan] = mean_age

def indicator_greater_than_zero(x):
  if x > 0:
    return 1
  else:
    return 0

df['SibSp>0'] = df['SibSp'].apply(indicator_greater_than_zero)


df['Parch>0'] = df['Parch'].apply(indicator_greater_than_zero)


df['Cabin'] = df['Cabin'].fillna('None')

def get_cabin_type(cabin):
  if cabin == 'None':
    return 'None'
  else:
    return cabin[0]


df['CabinType'] = df['Cabin'].apply(get_cabin_type)

print(df['CabinType'])

for cabintype in df['CabinType'].unique():
  dummy_variable_name = 'CabinType={}'.format(cabintype)
  dummy_variable_values = df['CabinType'].apply(lambda entry: int(entry == cabintype))
  #print(dummy_variable_name)
  df[dummy_variable_name] = dummy_variable_values

del df['CabinType']

df['Embarked'] =df['Embarked'].fillna('None')

for cabintype in df['Embarked'].unique():
  dummy_variable_name = 'Embarked={}'.format(cabintype)
  dummy_variable_values = df['Embarked'].apply(lambda entry: int(entry == cabintype))
  df[dummy_variable_name] = dummy_variable_values

del df['Embarked']



features_to_use = ['Sex',"Pclass","Fare","Age","SibSp","SibSp>0","Parch>0","Embarked=C","Embarked=None","Embarked=Q","Embarked=S", "CabinType=A","CabinType=B","CabinType=C","CabinType=D","CabinType=E","CabinType=F","CabinType=G","CabinType=None","CabinType=T"]
columns_needed = ['Survived'] + features_to_use


df = df[columns_needed]



df_train = df[:500]
df_test = df[500:]

arr_train = np.array(df_train)
arr_test = np.array(df_test)

Y_train = arr_train[:,0]
Y_test = arr_test[:,0]

X_train = arr_train[:,1:]
X_test = arr_test[:,1:]

print("before regressor")
regressor = LogisticRegression(max_iter=1000)

print('after creation')
regressor.fit(X_train, Y_train)
print('fit')
print(regressor.coef_)


coef_dict = {}
featured_columns = df.columns[1:]
featured_coefficients = regressor.coef_
print('featured_coefficients')
print(featured_coefficients)

for i in range(len(featured_columns)):
  column = featured_columns[i]

  coefficient = featured_coefficients[0][i]
  coef_dict[column] = coefficient

print('coef_dict')
print(coef_dict)

Y_test_predictions = regressor.predict(X_test)

Y_train_predictions = regressor.predict(X_train)

def conver_regressor_output_to_survival_value(output):
  if output <0.5:
    return 0
  else:
    return 1

y_test_predictions = [conver_regressor_output_to_survival_value(output) for output in Y_test_predictions]
y_train_predictions = [conver_regressor_output_to_survival_value(output) for output in Y_train_predictions]
print(y_test_predictions)
print(y_train_predictions)

def get_accuracy(predictions, actual):
  num_correct = 0 
  num_incorrect = 0
  for i in range(len(predictions)):
    if predictions[i] == actual[i]:
      num_correct += 1
    else:
      num_incorrect += 1
  return num_correct/(num_correct+num_incorrect)

print('features', features_to_use)
print('y test accuracy',get_accuracy(y_test_predictions, Y_test))
print('y train accuracy', get_accuracy(y_train_predictions, Y_train))
  


  

