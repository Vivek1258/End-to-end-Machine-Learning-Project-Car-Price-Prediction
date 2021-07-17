import pickle

import numpy as np 

from transforms import transformer

model = pickle.load(open('Server/models/cars_random_forest_regression_model.pkl', 'rb'))


tr = transformer(m_path = "train/meta_data")


def getpred(Present_Price,
			Kms_Driven,
			Owner,
			Year,
			Fuel_Type_Diesel,
			Fuel_Type_Petrol,
			Seller_Type_Individual,
			Transmission_Mannual):

	
	Present_Price = tr.norm_Present_Price(Present_Price)

	Kms_Driven = tr.norm_Kms_Driven(Kms_Driven)

	Year = tr.norm_Year(Year)

	prediction = model.predict([[Present_Price,
							   Kms_Driven2,
							   Owner,
							   Year,
							   Fuel_Type_Diesel,
							   Fuel_Type_Petrol,
							   Seller_Type_Individual,
							   Transmission_Mannual]])

	pred = tr.de_norm_Selling_Price(prediction[0])

	return np.round(pred , 2)
