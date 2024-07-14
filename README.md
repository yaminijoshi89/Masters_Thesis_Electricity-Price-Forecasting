# Masters_Thesis: Comparative Study of ML/AI Models for day-ahead Electricity-Price-Forecasting in the German market
This repository is created to document my master's thesis-related datasets and code. 
Once completed, it will be made public for future use, improvements, and research. 

Model's used : 
- Autoregressive Integrated Moving Average (ARIMA)
- Seasonal Autoregressive Integrated Moving-Average (SARIMA)
- Generalized Autoregressive Conditional Heteroskedasticity (GARCH)
- XGBoost (Extreme Gradient Boosting)
- Long Short-Term Memory (LSTM) networks
- Convolutional Neural Networks (CNNs)
- Prophet
- DeepAR
- Wavelet-Transform-Based Models
- Generalized Additive Model (GAM)

Variables:
- Day-ahead price: ENTSO-E provides day-ahead transmission prices at 15-min, 30-min, and hourly intervals.
- Fuel Prices (Gas, coal): 
- Load 
- Installed Capacity per Production Type
- Generation: Generation forecast for wind and solar , Generation forecast for day-ahead
- Weather -> Temperature
- Calendar variables: Weekday, Weekend

Data Source: ENTSO-E (open-source)

Setup:

1. Download and install the Python client for the ENTSO-E platform first.
   pip install entsoe-py
2. Register on the ENTSO-E transparency platform (click login at the top right of the page): https://transparency.entsoe.eu/dashboard/show
3. Request an API key by sending an email to transparency@entsoe.eu with “Restful API access” in the subject line. In the email body state your registered email address.
   You will receive an email when you have been provided with the API key. The key is then visible in your ENTSO-E account under “Web API Security Token”.

   Since our study is focused on German market, it is important to note :
   <img width="611" alt="image" src="https://github.com/user-attachments/assets/31fec171-3e0b-4275-b3e5-1af650a5c625">
   source: https://github.com/EnergieID/entsoe-py/blob/master/README.md


