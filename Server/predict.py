import pickle

import numpy as np 

model = pickle.load(open('Server/models/cars_random_forest_regression_model.pkl', 'rb'))




def getpred(Present_Price,
			Kms_Driven,
			Owner,
			Year,
			Fuel_Type_Diesel,
			Fuel_Type_Petrol,
			Seller_Type_Individual,
			Transmission_Mannual):

	Kms_Driven2=np.log(Kms_Driven)

	prediction = model.predict([[Present_Price,
							   Kms_Driven2,
							   Owner,
							   Year,
							   Fuel_Type_Diesel,
							   Fuel_Type_Petrol,
							   Seller_Type_Individual,
							   Transmission_Mannual]])

	return np.round(prediction[0] , 2)
