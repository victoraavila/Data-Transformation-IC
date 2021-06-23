import pandas as pd
import numpy as np

def drag_header_to_first_line(dataframe, rows_amount, columns_amount, header):
    
    aux = pd.DataFrame(np.empty((rows_amount, columns_amount), dtype = str),
                       columns = header)

    for i in range(rows_amount):
        for j in range(columns_amount):
            if (i == 0):
                aux.iloc[0][j] = dataframe.columns.values[j]
            else:
                aux.iloc[i][j] = dataframe.iloc[i-1][j]

    return aux