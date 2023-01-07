import streamlit as st
import requests
import numpy as np
import json

st.title('Taxifare Pricer in NY')

pickup_datetime = st.text_input(label='Pickup Date')
pickup_longitude = st.text_input(label='Pickup Longitude')
pickup_latitude = st.text_input(label='Pickup Latitude')
dropoff_longitude = st.text_input(label='Dropoff Longitude')
dropoff_latitude = st.text_input(label='Dropoff Latitude')
passenger_count = st.text_input(label='Number of passengers')

params = {'pickup_datetime':pickup_datetime,
          'pickup_longitude':pickup_longitude,
          'pickup_latitude':pickup_latitude,
          'dropoff_longitude':dropoff_longitude,
          'dropoff_latitude':dropoff_latitude,
          'passenger_count':passenger_count}
fare_price = requests.get('https://taxifare.lewagon.ai/predict',params=params)
fare_price = np.round(json.loads(fare_price.text)['fare'],2)
st.write('The fare estimated price is : ', fare_price,'$')
