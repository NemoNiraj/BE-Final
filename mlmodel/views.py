from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib import messages,auth

from contacts.models import Contact
from django.contrib.auth.models import User

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
import numpy as np



def predict_view(request):
	return render(request, 'mlmodel/predict.html')


def result(request):
	#return render(request, 'mlmodel/predict.html')
	dataset = pd.read_csv(r"C:\Users\Lenovo\Desktop\next\Django-Real-Estate-Management-Webapp-main\kc_house_data.csv")
	dataset = dataset.drop(['id','date','lat','long'],axis=1)
	X = dataset.iloc[:, 1:].values
	y = dataset.iloc[:, 0].values

	X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=0)
	rf_regressor = RandomForestRegressor(n_estimators=17, random_state=0)
	rf_regressor.fit(X_train, y_train)
	rf_regressor.score(X_test, y_test)
	#rf_pred = rf_regressor.predict(X_test)
	#rf_score = rf_regressor.score(X_test, y_test)
	#expl_rf = explained_variance_score(rf_pred, y_test)
	#
	# var1 = float(request.POST.get('one'))
	# var2 = float(request.POST.get('two'))
	# var3 = float(request.POST.get('thri'))
	# var4 = float(request.POST.get('four'))
	# var5 = float(request.POST.get('five'))

	# var1 = 34324.433
	# var2 = 543.44
	# var3 = 454354543.655
	# var4 = 4353534.65
	# var5 = 345435.56

	var1 = float(request.POST.get('one'))
	var2 = float(request.POST.get('two'))
	var3 = float(request.POST.get('thri'))
	var4 = float(request.POST.get('four'))
	var5 = float(request.POST.get('five'))
	var6 = float(request.POST.get('n6'))
	var7 = float(request.POST.get('n7'))
	var8 = float(request.POST.get('n8'))
	var9 = float(request.POST.get('n9'))
	var10 = float(request.POST.get('n10'))
	var11 = float(request.POST.get('n11'))
	var12 = float(request.POST.get('n12'))
	var13 = float(request.POST.get('n13'))
	var14 = float(request.POST.get('n14'))
	var15 = float(request.POST.get('n15'))
	var16 = float(request.POST.get('n16'))





	pred = rf_regressor.predict(np.array([var1,var2,var3,var4,var5,var6,var7,var8,var9,var10,var11,var12,var13,var14,var15,var16]).reshape(1,-1))
	pred = round(pred[0])

	price = '  Predicted price is : $ '+str(pred)

	return render(request, 'mlmodel/predict.html',{"result2":price})




def dashborad(request):
	user_contact = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)
	return render(request,'accounts/dashborad.html',{'contacts' : user_contact})
