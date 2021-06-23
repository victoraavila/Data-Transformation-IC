import pandas as pd
import re
import numpy as np

def divide_string_column_into_list_column(dataframe, rows_amount):
    for i in range(rows_amount + 1):
        dataframe.iloc[i][0] = re.split(r' ', str(dataframe.iloc[i][0]))

    for i in range(rows_amount + 1):
        for j in range(1):
            count = 0
            mylist = []
            for item in dataframe.iloc[i][j]:
                if count >= 1:
                    mylist.append(item)
                count += 1
            dataframe.iloc[i][j][1] = " ".join(mylist)

            if count > 2:
                for iter in range(count - 1, 1, -1):
                    dataframe.iloc[i][j].pop(iter)

    return dataframe

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