from fbprophet import Prophet
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("./data/example_wp_log_peyton_manning.csv")
print(df.head())

m = Prophet() # Defalut growth='linear'
m.fit(df) 

future = m.make_future_dataframe(periods=365)
print(future.tail())

forecast = m.predict(future) 
print(forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail())

fig1 = m.plot(forecast)
fig2 = m.plot_components(forecast)
plt.show()

