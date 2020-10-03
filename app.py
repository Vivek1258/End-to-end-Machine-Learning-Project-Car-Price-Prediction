import streamlit as st 
import jsonify
import pickle
import numpy as np
import webbrowser
import sklearn
from sklearn.preprocessing import StandardScaler


#st.title("Car Price Prediction")
html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h1 style="color:white;text-align:center;">ML App: Car Price prediction </h1>
    </div>
    """

st.markdown(html_temp,unsafe_allow_html=True)
model = pickle.load(open('models/cars_random_forest_regression_model.pkl', 'rb'))

Year = int(st.number_input("Year of purchase"))
Present_Price=st.number_input("What is the Showroom Price?(In lakhs)")
Kms_Driven=int(st.number_input("How Many Kilometers Drived?"))
Kms_Driven2=np.log(Kms_Driven)
Owner=int(st.selectbox("How much owners previously had the car?" , [0,1,2]))
Fuel_Type_Petrol= st.selectbox("What Is the Fuel type?" , ['Petrol' , 'Diesel'])
if(Fuel_Type_Petrol=='Petrol'):
        Fuel_Type_Petrol=1
        Fuel_Type_Diesel=0
elif (Fuel_Type_Petrol=='Diesel') :
        Fuel_Type_Petrol=0
        Fuel_Type_Diesel=1
else :
        Fuel_Type_Petrol=0
        Fuel_Type_Diesel=0

Year=2020-Year
Seller_Type_Individual=st.selectbox("Are you A Dealer or Individual" , ['Individual' , 'Dealer'])
if(Seller_Type_Individual=='Individual'):
    Seller_Type_Individual=1
else:
    Seller_Type_Individual=0	
Transmission_Mannual=st.selectbox("Transmission type" , ['Mannual' , 'Automatic'])
if(Transmission_Mannual=='Mannual'):
    Transmission_Mannual=1
else:
    Transmission_Mannual=0


result = ""


if st.button("Predict"):
	prediction=model.predict([[Present_Price,
						   Kms_Driven2,
						   Owner,
						   Year,
						   Fuel_Type_Diesel,
						   Fuel_Type_Petrol,
						   Seller_Type_Individual,
						   Transmission_Mannual
						  ]])

	output = round(prediction[0] , 2)

	if output<0 :
		result = "Sorry you cannot sell this car"
	else:
		result = "You Can Sell The Car at {}".format(output)


st.write(result)




url = 'https://github.com/Vivek1258/Car-Price-Prediction-using-random_forest_regression'

if st.button('Check code on github'):
    webbrowser.open_new_tab(url)
