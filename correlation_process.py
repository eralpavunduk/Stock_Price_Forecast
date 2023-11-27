# This function gives the correlation of data
def correlation_of_data(data):
    numeric_columns = data.drop(columns=['Date'])
    correlation_matrix = numeric_columns.corr()

    return print(correlation_matrix)

