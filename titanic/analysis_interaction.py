print('begin')
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
import sys

x = 'Sex * SibSp'
y = x.split(' * ')
print('split')
print(y)

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



key_features = ['Sex',"Pclass","Fare","Age","SibSp","SibSp>0","Parch>0","Embarked=C","Embarked=None","Embarked=Q","Embarked=S", "CabinType=A","CabinType=B","CabinType=C","CabinType=D","CabinType=E","CabinType=F","CabinType=G","CabinType=None","CabinType=T"] 


interaction_features = ['Sex * Pclass', 'Sex * Fare', 'Sex * Age', 'Sex * SibSp', 'Sex * SibSp>0', 'Sex * Parch>0', 'Sex * Embarked=C', 'Sex * Embarked=None', 'Sex * Embarked=Q', 'Sex * Embarked=S', 'Sex * CabinType=A', 'Sex * CabinType=B', 'Sex * CabinType=C', 'Sex * CabinType=D', 'Sex * CabinType=E', 'Sex * CabinType=F', 'Sex * CabinType=G', 'Sex * CabinType=None', 'Sex * CabinType=T', 'Pclass * Fare', 'Pclass * Age', 'Pclass * SibSp', 'Pclass * SibSp>0', 'Pclass * Parch>0', 'Pclass * Embarked=C', 'Pclass * Embarked=None', 'Pclass * Embarked=Q', 'Pclass * Embarked=S', 'Pclass * CabinType=A', 'Pclass * CabinType=B', 'Pclass * CabinType=C', 'Pclass * CabinType=D', 'Pclass * CabinType=E', 'Pclass * CabinType=F', 'Pclass * CabinType=G', 'Pclass * CabinType=None', 'Pclass * CabinType=T', 'Fare * Age', 'Fare * SibSp', 'Fare * SibSp>0', 'Fare * Parch>0', 'Fare * Embarked=C', 'Fare * Embarked=None', 'Fare * Embarked=Q', 'Fare * Embarked=S', 'Fare * CabinType=A', 'Fare * CabinType=B', 'Fare * CabinType=C', 'Fare * CabinType=D', 'Fare * CabinType=E', 'Fare * CabinType=F', 'Fare * CabinType=G', 'Fare * CabinType=None', 'Fare * CabinType=T', 'Age * SibSp', 'Age * SibSp>0', 'Age * Parch>0', 'Age * Embarked=C', 'Age * Embarked=None', 'Age * Embarked=Q', 'Age * Embarked=S', 'Age * CabinType=A', 'Age * CabinType=B', 'Age * CabinType=C', 'Age * CabinType=D', 'Age * CabinType=E', 'Age * CabinType=F', 'Age * CabinType=G', 'Age * CabinType=None', 'Age * CabinType=T', 'SibSp * SibSp>0', 'SibSp * Parch>0', 'SibSp * Embarked=C', 'SibSp * Embarked=None', 'SibSp * Embarked=Q', 'SibSp * Embarked=S', 'SibSp * CabinType=A', 'SibSp * CabinType=B', 'SibSp * CabinType=C', 'SibSp * CabinType=D', 'SibSp * CabinType=E', 'SibSp * CabinType=F', 'SibSp * CabinType=G', 'SibSp * CabinType=None', 'SibSp * CabinType=T', 'SibSp>0 * Parch>0', 'SibSp>0 * Embarked=C', 'SibSp>0 * Embarked=None', 'SibSp>0 * Embarked=Q', 'SibSp>0 * Embarked=S', 'SibSp>0 * CabinType=A', 'SibSp>0 * CabinType=B', 'SibSp>0 * CabinType=C', 'SibSp>0 * CabinType=D', 'SibSp>0 * CabinType=E', 'SibSp>0 * CabinType=F', 'SibSp>0 * CabinType=G', 'SibSp>0 * CabinType=None', 'SibSp>0 * CabinType=T', 'Parch>0 * Embarked=C', 'Parch>0 * Embarked=None', 'Parch>0 * Embarked=Q', 'Parch>0 * Embarked=S', 'Parch>0 * CabinType=A', 'Parch>0 * CabinType=B', 'Parch>0 * CabinType=C', 'Parch>0 * CabinType=D', 'Parch>0 * CabinType=E', 'Parch>0 * CabinType=F', 'Parch>0 * CabinType=G', 'Parch>0 * CabinType=None', 'Parch>0 * CabinType=T', 'Embarked=C * CabinType=A', 'Embarked=C * CabinType=B', 'Embarked=C * CabinType=C', 'Embarked=C * CabinType=D', 'Embarked=C * CabinType=E', 'Embarked=C * CabinType=F', 'Embarked=C * CabinType=G', 'Embarked=C * CabinType=None', 'Embarked=C * CabinType=T', 'Embarked=None * CabinType=A', 'Embarked=None * CabinType=B', 'Embarked=None * CabinType=C', 'Embarked=None * CabinType=D', 'Embarked=None * CabinType=E', 'Embarked=None * CabinType=F', 'Embarked=None * CabinType=G', 'Embarked=None * CabinType=None', 'Embarked=None * CabinType=T', 'Embarked=Q * CabinType=A', 'Embarked=Q * CabinType=B', 'Embarked=Q * CabinType=C', 'Embarked=Q * CabinType=D', 'Embarked=Q * CabinType=E', 'Embarked=Q * CabinType=F', 'Embarked=Q * CabinType=G', 'Embarked=Q * CabinType=None', 'Embarked=Q * CabinType=T', 'Embarked=S * CabinType=A', 'Embarked=S * CabinType=B', 'Embarked=S * CabinType=C', 'Embarked=S * CabinType=D', 'Embarked=S * CabinType=E', 'Embarked=S * CabinType=F', 'Embarked=S * CabinType=G', 'Embarked=S * CabinType=None', 'Embarked=S * CabinType=T']
columns_needed = ['Survived'] + key_features
all_features = columns_needed + interaction_features
df = df[columns_needed]

for column in interaction_features:
  if ' * ' in column:
    parts = column.split(' * ')    
    df[column] = df[parts[0]] * df[parts[1]]


df_train = df[:500]
df_test = df[500:]

arr_train = np.array(df_train)
arr_test = np.array(df_test)

Y_train = arr_train[:,0]
Y_test = arr_test[:,0]

X_train = arr_train[:,1:]
X_test = arr_test[:,1:]

regressor = LogisticRegression(max_iter=10000)

regressor.fit(X_train, Y_train)



coef_dict = {}
featured_columns = df.columns[1:]
featured_coefficients = regressor.coef_


for i in range(len(featured_columns)):
  column = featured_columns[i]

  coefficient = featured_coefficients[0][i]
  coef_dict[column] = coefficient


Y_test_predictions = regressor.predict(X_test)

Y_train_predictions = regressor.predict(X_train)

def conver_regressor_output_to_survival_value(output):
  if output <0.5:
    return 0
  else:
    return 1

y_test_predictions = [conver_regressor_output_to_survival_value(output) for output in Y_test_predictions]
y_train_predictions = [conver_regressor_output_to_survival_value(output) for output in Y_train_predictions]

def get_accuracy(predictions, actual):
  num_correct = 0 
  num_incorrect = 0
  for i in range(len(predictions)):
    if predictions[i] == actual[i]:
      num_correct += 1
    else:
      num_incorrect += 1
  return num_correct/(num_correct+num_incorrect)

print('features', all_features)
print('y test accuracy',get_accuracy(y_test_predictions, Y_test))
print('y train accuracy', get_accuracy(y_train_predictions, Y_train))
  


  

