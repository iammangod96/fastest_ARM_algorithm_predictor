import pandas as pd
from sklearn import tree, svm
from sklearn.neighbors import KNeighborsClassifier
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.gaussian_process.kernels import RBF
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neural_network import MLPClassifier
import numpy as np
from pandas.tools.plotting import parallel_coordinates, andrews_curves
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import pandas.tools.plotting as pdplt
from sklearn import preprocessing

data = pd.read_csv('./final/final_dataset.txt', sep=',', header=None)

input_data = data.loc[:, [i for i in range(7)]]
output = data.loc[:, [7, 8, 9]]

output_data = []

output = np.array(output)

for line in output:
	for i in range(3):
		#print('line: ' + str(line))
		if line[i] == 1:
			output_data.append(i)
#print(output_data)

x, x_test, y, y_test = train_test_split(input_data, output_data, test_size=0.2, train_size=0.8)


clf1 = tree.DecisionTreeClassifier()
clf2 = svm.SVC(gamma=2,C=1)
clf3 = KNeighborsClassifier(3)
clf4 = GaussianProcessClassifier(1.0*RBF(1.0),warm_start=True)
clf5 = AdaBoostClassifier()
clf1= clf1.fit(x, y)
clf2= clf2.fit(x, y)
clf3=clf3.fit(x, y)
clf4=clf4.fit(x, y)
clf5=clf5.fit(x, y)
y_pred1 = clf1.predict(x_test)
y_pred2 = clf2.predict(x_test)
y_pred3 = clf3.predict(x_test)
y_pred4 = clf4.predict(x_test)
y_pred5 = clf5.predict(x_test)
count1 = 0	
for x, y in zip(y_pred1, y_test):
	if x == y:
		count1 += 1
count2 = 0	
for x, y in zip(y_pred2, y_test):
	if x == y:
		count2 += 1
count3 = 0	
for x, y in zip(y_pred3, y_test):
	if x == y:
		count3 += 1
count4 = 0	
for x, y in zip(y_pred4, y_test):
	if x == y:
		count4 += 1
count5 = 0	
for x, y in zip(y_pred5, y_test):
	if x == y:
		count5 += 1
for i in range(len(y_pred1)):
	if y_pred1[i]==0:
		y_pred1[i]=-1
for i in range(len(y_pred2)):
	if y_pred2[i]==0:
		y_pred2[i]=-1
for i in range(len(y_pred3)):
	if y_pred3[i]==0:
		y_pred3[i]=-1
for i in range(len(y_pred4)):
	if y_pred4[i]==0:
		y_pred4[i]=-1
for i in range(len(y_pred5)):
	if y_pred5[i]==0:
		y_pred5[i]=-1
acc1=float(count1)/len(y_test)
acc2=float(count2)/len(y_test)
acc3=float(count3)/len(y_test)
acc4=float(count4)/len(y_test)
acc5=float(count5)/len(y_test)
accsum=acc1+acc2+acc3+acc4+acc5
count6=0
for x,y,z,w,v,o in zip(y_pred1, y_pred2, y_pred3, y_pred4, y_pred5, y_test):
	y_pred6=(acc1/accsum)*x+(acc2/accsum)*y+(acc3/accsum)*z+(acc4/accsum)*w+(acc5/accsum)*v
	if y_pred6<=0:
		y_pred6=0
	else:
		y_pred6=1
	if y_pred6==o:
		count6 +=1
acc6=float(count6)/len(y_test)
print('The accuracy of dt classifier is %0.3f' %acc1)
print('The accuracy of svm classifier is %0.3f' %acc2)
print('The accuracy of knn classifier is %0.3f' %acc3)
print('The accuracy of guassian process classifier is %0.3f' %acc4)
print('The accuracy of adaboost classifier is %0.3f' %acc5)
print('The accuracy of optimal bayesian classifier is %0.3f' %acc6)
'''x = input_data.values #returns a numpy array
min_max_scaler = preprocessing.MinMaxScaler()
x_scaled = min_max_scaler.fit_transform(x)
input_data = pd.DataFrame(x_scaled)


input_data = input_data.assign(target = pd.Series(output_data).values)
#print(input_data.head())

 Plot '''
'''plt.figure()
parallel_coordinates(input_data, 'target')
plt.show()'''
