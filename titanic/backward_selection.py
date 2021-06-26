print('begin')
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
import sys
from warnings import simplefilter
from sklearn.exceptions import ConvergenceWarning
simplefilter("ignore", category=ConvergenceWarning)

 #split data
def split_train_test(df):
    test_train = df[:500]
    test_test = df[500:]
    return (test_train, test_test)


def conver_regressor_output_to_survival_value(output):
    if output <0.5:
        return 0
    else:
        return 1

#regress train and test
def get_predictions(df_train, df_test):

    arr_train = np.array(df_train)
    arr_test = np.array(df_test)
    

    Y_train = arr_train[:,0]
    Y_test = arr_test[:,0]
    
    X_train = arr_train[:,1:]
    X_test = arr_test[:,1:]

    regressor = LogisticRegression(max_iter=10)
    
    regressor.fit(X_train, Y_train)
    
    Y_test_predictions = regressor.predict(X_test)
    
    Y_train_predictions = regressor.predict(X_train)

    y_test_predictions = [conver_regressor_output_to_survival_value(output) for output in Y_test_predictions]
    
    y_train_predictions = [conver_regressor_output_to_survival_value(output) for output in Y_train_predictions]

    predictions = {
        'test predictions': y_test_predictions,
        'train predictions':y_train_predictions
    }
    return predictions


def get_accuracy(predictions, actual):
    num_correct = 0 
    total = len(predictions)

    
    for i in range(len(predictions)):
        try:
            if predictions[i] == actual[i]:
                num_correct += 1
        except Exception as error:
            print('len predictions ', len(predictions))
            print('predictions ', predictions)
            print('len actual ', len(actual))
            print('actual ', actual['Survived'])
            print(error)
    return num_correct/(total)


df = pd.read_csv('processed_titanic_data.csv')

keep_columns = list(df.columns)
new_df = df[keep_columns]
train_tests = split_train_test(new_df)
predictions = get_predictions(train_tests[0],train_tests[1])
previous_accuracy = get_accuracy(predictions['test predictions'], list(train_tests[1]['Survived']))


print("start accuracy ",previous_accuracy)
for feature in df.columns:
  if feature == 'Survived':
    continue
  check_columns = list(keep_columns)
  feature_index = check_columns.index(feature)
  del check_columns[feature_index]

  new_df = df[check_columns]
  train_tests = split_train_test(new_df)
  predictions = get_predictions(train_tests[0],train_tests[1])
  accuracy = get_accuracy(predictions['test predictions'], list(train_tests[1]['Survived']))
    
  if accuracy > previous_accuracy:
    keep_columns = list(check_columns)
    previous_accuracy = accuracy


best_df = df[keep_columns]
train_tests = split_train_test(best_df)
predictions = get_predictions(train_tests[0],train_tests[1])
test = get_accuracy(predictions['test predictions'], list(train_tests[1]['Survived']))
train = get_accuracy(predictions['train predictions'], list(train_tests[0]['Survived']))

left_out = []
for column in df.columns:
  if column not in keep_columns:
    left_out.append(column)
print('left out ', left_out)
print('')

print(keep_columns)
print('')
print('test accuracy : ', test)
print('train accuracy : ', train)
