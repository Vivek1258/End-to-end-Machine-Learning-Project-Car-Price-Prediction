
import json
import requests
  
# api-endpoint
URL = "http://127.0.0.1:5000/getcp"
  
def predict_price(Present_Price,
					Kms_Driven,
					Owner,
					Year,
					Fuel_Type_Diesel,
					Fuel_Type_Petrol,
					Seller_Type_Individual,
					Transmission_Mannual):

	# defining a params dict for the parameters to be sent to the API
	PARAMS = { "Present_Price": Present_Price , 
					"Kms_Driven" : Kms_Driven ,
					"Owner" : Owner ,
					"Year" : Year,
					"Fuel_Type_Diesel" : Fuel_Type_Diesel ,
					"Fuel_Type_Petrol" :  Fuel_Type_Petrol ,
					"Seller_Type_Individual" : Seller_Type_Individual ,
					"Transmission_Mannual" : Transmission_Mannual }

	# sending get request and saving the response as response object
	r = requests.get(url = URL, json = PARAMS) # json.dumps(
	  
	# extracting data in json format

	print(r.status_code)
	data = r.json()

	#print(data)

	return data['prediction']


		
	

  

  

