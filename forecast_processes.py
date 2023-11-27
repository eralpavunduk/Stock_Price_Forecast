import pandas as pd
from statsmodels.tsa.statespace.sarimax import SARIMAX


# This function use SARIMAX algorithm for time series data
def sarimax_forecast(time_series_data):
    # Configuration of SARIMAX
    model = SARIMAX(time_series_data['value'], order=(1, 1, 1), seasonal_order=(1, 1, 1, 12))
    results = model.fit(disp=False)
    forecast_steps = 10
    forecast = results.get_forecast(steps=forecast_steps)
    pd.date_range(start=time_series_data['date'].max() + pd.DateOffset(1), periods=forecast_steps,
                  freq='D')

    print(f"SARI-MAX Forecast for the next {forecast_steps} days:")
    print(forecast.predicted_mean)


# This function executes the results of SARIMAX algorithm and gets closing values of next forecast_steps days
def sarimax_executor(data):
    data['Date'] = pd.to_datetime(data['Date'])
    data = data.sort_values(by='Date')

    time_series_data = data[['Date', 'Close']]
    time_series_data.columns = ['date', 'value']

    sarimax_forecast(time_series_data)
