import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.model_selection import KFold

def LinearRegression(A, b):
	reg = linear_model.LinearRegression().fit(A, b)
	return reg.coef_, reg.intercept_

def CrossValidation(A, b, kfold):
	kf = KFold(n_splits=kfold)
	error_list = []
	for train_index, test_index in kf.split(A):
		A_train, A_test = A[train_index], A[test_index]
		b_train, b_test = b[train_index], b[test_index]
		x, bias = LinearRegression(A_train, b_train)
		error_list.append(np.mean(np.absolute(b_test - (np.dot(A_test, x) + bias))))
	return np.mean(error_list)

def chooseBestProperty(A, b):
	result = []
	for i in range(A.shape[1]):
		cv_properties = CrossValidation(A[:, i:i + 1], b, 10)
		result.append(cv_properties)
	return result, np.argmin(result)

def myModel(A, b, error_list, header_len):
	sorted_error = np.argsort(error_list)
	full_error = CrossValidation(A, b, 10)

	error_list = []
	cv_error_list = []
	property_list = []

	for i in range(2, header_len - 1):
		properties_to_pick = sorted_error[:i]
		A_build = A[:, properties_to_pick]
		error = CrossValidation(A_build, b, 10)
		cv_error_list.append(error)
		error_list.append(np.absolute(full_error - error))
		property_list.append(properties_to_pick)	
	return cv_error_list, property_list, np.argmin(error_list)

#import data
df = pd.read_csv('wine.csv', sep=';')
#parse data to numpy
header = df.columns
data = df.iloc[:, : -1].to_numpy()
rate = df.iloc[:, -1].to_numpy()

#based on all data
x_a, bias_a = LinearRegression(data, rate)
error_a = CrossValidation(data, rate, 10)
print(f'Model: A{x_a} + {bias_a} = b')
print(f'CV error: {error_a}\n\n')

#best property
error_list, best_index = chooseBestProperty(data, rate)
x_b, bias_b = LinearRegression(data[:, best_index:best_index + 1], rate)
print(f'Best property: {header[best_index]}')
print(f'Model: A{x_b} + {bias_b} = b')
print(f'CV error: {error_list[best_index]}\n\n')

#build my own model
cv_error_list, property_list, best_index_property = myModel(data, rate, error_list, len(header))
x_c, bias_c = LinearRegression(data[:, property_list[best_index_property]], rate)
print(f'Best properties: {list(header[property_list[best_index_property]])}')
print(f'Model: A{x_c} + {bias_c} = b')
print(f'CV error: {cv_error_list[best_index_property]}')