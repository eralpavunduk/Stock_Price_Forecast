from forecast_processes import sarimax_executor
from visualization_process import visualize
from correlation_process import correlation_of_data
from Helpers.readingdata import apple_data


def forecasting(data):
    try:
        our_forecast = sarimax_executor(data)
        return our_forecast
    except Exception as ex:
        return print(str(ex))


def data_correlation(data):
    try:
        our_correlation = correlation_of_data(data)
        return our_correlation
    except Exception as ex:
        return print(str(ex))


def visualizing_data(data):
    try:
        our_graph = visualize(data)
        return our_graph
    except Exception as ex:
        return print(str(ex))


forecasting(apple_data)
data_correlation(apple_data)
visualizing_data(apple_data)
