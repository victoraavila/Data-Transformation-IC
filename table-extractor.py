import os
from tabula import read_pdf
import pandas as pd
import numpy as np
import re
from zipfile import ZipFile

# 1. Reading desired tables from .pdf and saving them as Pandas Dataframes
pdf_path = os.path.join(os.path.abspath("src"), "Componente Organizacional.pdf")
pages = [79, 80, 81, 82, 83, 84, 85]

df = read_pdf(pdf_path, pages = pages)

# 2. Organizing Quadro 30
## Creating MultiIndex
header = [df[0].columns.values[0], df[0].columns.values[0]]
subheader = ["Código", "Descrição da Categoria"]
Q30_header = pd.MultiIndex.from_tuples(list(zip(header, subheader)))

## Dividing column with one string into column with list of strings 
for i in range(6):
        df[0].iloc[i][0] = re.split(r' ', str(df[0].iloc[i][0]))

for i in range(6):
    for j in range(1):
        count = 0
        mylist = []
        for item in df[0].iloc[i][j]:
            if count >= 1:
                mylist.append(item)
            count += 1
        df[0].iloc[i][j][1] = " ".join(mylist)

        if count > 2:
            for iter in range(count - 1, 1, -1):
                df[0].iloc[i][j].pop(iter)

df[0] = pd.DataFrame(df[0]["Tabela de Tipo do Demandante"].to_list(), columns = subheader)
print(df[0], "\n")

## Creating a new empty Dataframe to fill it with df[0] Dataframe
Q30 = pd.DataFrame(np.empty((5, 2), dtype = str), columns = Q30_header)
for i in range(5):
    for j in range(2):
        Q30.iloc[i][j] = df[0].iloc[i + 1][j]

print(Q30, "\n")

# 3. Saving Quadro 30 as a .csv file
Q30_filename = "quadro30"
Q30.to_csv(path_or_buf = Q30_filename + ".csv")

#ZipFile(Q30_filename + ".zip", "w").write(Q30_filename + ".csv")
