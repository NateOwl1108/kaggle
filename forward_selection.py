print('begin')
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
import sys
import warnings
warnings.filterwarnings("ignore")

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

permanant_columns = ['Survived']
permanant_acuracy = 0
while True:
    improved =  False
    keep_feature = None
    for feature in df.columns:
        if feature in permanant_columns:
            continue
        # permanant + [feature]
        new_df = df[permanant_columns + [feature]]
        train_tests = split_train_test(new_df)
        predictions = get_predictions(train_tests[0],train_tests[1])
        accuracy = get_accuracy(predictions['test predictions'], list(train_tests[1]['Survived']))
        
        if accuracy > permanant_acuracy:
            keep_feature = feature
            permanant_acuracy = accuracy
            improved = True
    
    if improved == False:
        break
    permanant_columns.append(keep_feature)

best_df = df[permanant_columns]
train_tests = split_train_test(best_df)
predictions = get_predictions(train_tests[0],train_tests[1])
test = get_accuracy(predictions['test predictions'], list(train_tests[1]['Survived']))
train = get_accuracy(predictions['train predictions'], list(train_tests[0]['Survived']))

print(permanant_columns)
print('test accuracy : ', test)
print('train accuracy : ', train)
