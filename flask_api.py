
import time
from flask import Flask, request 
from flask import Response, jsonify
#from flask_restplus import Api, Resource, fields
 
import json

from Server.predict import getpred

flask_app = Flask(__name__)

@flask_app.route("/getcp", methods=['GET'])
def predict_CP():

	data_dict = request.get_json()

	print(data_dict)

	print(type(data_dict))	

	pred = getpred(
			Present_Price = data_dict['Present_Price'],
			Kms_Driven = data_dict["Kms_Driven"],
			Owner =  data_dict["Owner"],
			Year= data_dict["Year"],
			Fuel_Type_Diesel = data_dict["Fuel_Type_Diesel"],
			Fuel_Type_Petrol = data_dict["Fuel_Type_Petrol"],
			Seller_Type_Individual = data_dict["Seller_Type_Individual"],
			Transmission_Mannual= data_dict["Transmission_Mannual"]
			)

	rt = {
	"prediction" : pred
	}

	return jsonify(rt)

if __name__ == "__main__":
    flask_app.run(debug=True)
