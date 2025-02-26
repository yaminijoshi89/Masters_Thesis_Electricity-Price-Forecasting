# Masters_Thesis: Comparative Study of ML/AI Models for short-term Electricity-Price-Forecasting in the German market

Model's used : 
- Autoregressive Integrated Moving Average (ARIMA)
- Seasonal Autoregressive Integrated Moving-Average (SARIMA)
- XGBoost (Extreme Gradient Boosting)
- Long Short-Term Memory (LSTM) networks
- Convolutional Neural Networks (CNNs)
- Prophet
- Generalized Additive Model (GAM)
- Interpretable Generalized Additive Neural Networks (IGANN)

Variables:
- Day-ahead price : ENTSO-E provides day-ahead transmission prices at hourly intervals.
- Load 
- Generation : Generation forecast for brown coal/lignite, gas, hard coal, biomass, oil, geothermal, hydro (pumped storage, run-of-river, and reservoir), Other, Other RES, waste, wind (offshore and onshore), and solar
- Weather : Cloud cover, sunshine duration, wind speed, and humidity.

Data Source: 
**The final merged and cleaned data is in /Datasets/Final_Modelling_data.csv**

**ENTSO-E (open-source)**

Setup:

1. Download and install the Python client for the ENTSO-E platform first.
   pip install entsoe-py
2. Register on the ENTSO-E transparency platform (click login at the top right of the page): https://transparency.entsoe.eu/dashboard/show
3. Request an API key by sending an email to transparency@entsoe.eu with “Restful API access” in the subject line. In the email body state your registered email address.
   You will receive an email when you have been provided with the API key. The key is then visible in your ENTSO-E account under “Web API Security Token”.

   Since our study is focused on German market, it is important to note :
   <img width="611" alt="image" src="https://github.com/user-attachments/assets/31fec171-3e0b-4275-b3e5-1af650a5c625">
   
   [source: https://github.com/EnergieID/entsoe-py/blob/master/README.md]

**DWD**
Following github provide detail steps to get data via *wetterdienst* library.
https://github.com/earthobservations/wetterdienst/blob/main/examples/notebooks/wetterdienst_notebook.ipynb
!pip install wetterdienst
!pip install dwdweather2
