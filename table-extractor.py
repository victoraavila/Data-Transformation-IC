import os
from tabula import read_pdf
import pandas as pd
import numpy as np
import re
import auxiliar_functions as af
import csv_zipper as cz

# 0. Setting Pandas printing options
pd.options.display.max_colwidth = 100
pd.options.display.max_rows = 140

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

## Dividing column with list of two strings into two columns
df[0] = pd.DataFrame(df[0]["Tabela de Tipo do Demandante"].to_list(), columns = subheader)

## Creating a new empty Dataframe to fill it with df[0] Dataframe
Q30 = pd.DataFrame(np.empty((5, 2), dtype = str), columns = Q30_header)
for i in range(5):
    for j in range(2):
        Q30.iloc[i][j] = df[0].iloc[i + 1][j]

print(Q30, "\n")

# 3. Saving Quadro 30 as a .csv file
Q30_filename = "quadro30"
Q30.to_csv(path_or_buf = Q30_filename + ".csv")

# 4. Organizing Quadro 31
## Creating MultiIndex
header = [df[1].columns.values[1], df[1].columns.values[1]]
Q31_header = pd.MultiIndex.from_tuples(list(zip(header, subheader)))

## Creating auxiliar matrix for df[2]
df[2] = af.drag_header_to_first_line(df[2], 27, 2, Q31_header)

## Creating auxiliar matrix for df[3]
df[3] = af.drag_header_to_first_line(df[3], 27, 2, Q31_header)

## Creating auxiliar matrix for df[4]
df[4] = af.drag_header_to_first_line(df[4], 26, 2, Q31_header)

## Creating auxiliar matrix for df[5]
df[5] = af.drag_header_to_first_line(df[5], 25, 2, Q31_header)

## Creating auxiliar matrix for df[6]
df[6] = af.drag_header_to_first_line(df[6], 23, 2, Q31_header)

## Creating a new empty Dataframe and filling it with df[1:6] Dataframes
Q31 = pd.DataFrame(np.empty((131, 2), dtype = str), columns = Q31_header)
for i in range(131):
    for j in range(2):
        if (i <= 2):
            Q31.iloc[i][j] = df[1].iloc[i + 1][j]
        
        elif (3 <= i) and (i <= 29):
            Q31.iloc[i][j] = df[2].iloc[i - 3][j]

        elif (30 <= i) and (i <= 56):
            Q31.iloc[i][j] = df[3].iloc[i - 30][j]

        elif (57 <= i) and (i <= 82):
            Q31.iloc[i][j] = df[4].iloc[i - 57][j]

        elif (83 <= i) and (i <= 107):
            Q31.iloc[i][j] = df[5].iloc[i - 83][j]

        elif (108 <= i) and (i <= 130):
            Q31.iloc[i][j] = df[6].iloc[i - 108][j]

## Replacing '\r' chars
for i in range(131):
    if ("\r" in Q31.iloc[i][1]):
        Q31.iloc[i][1] = Q31.iloc[i][1].replace("\r", " ")

print(Q31, "\n")

# 5. Saving Quadro 31 as a .csv file
Q31_filename = "quadro31"
Q31.to_csv(path_or_buf = Q31_filename + ".csv")

# 6. Organizing Quadro 32
## Creating MultiIndex
header = [df[7].columns.values[0], df[7].columns.values[0]]
subheader = ["Código", "Descrição da Categoria"]
Q32_header = pd.MultiIndex.from_tuples(list(zip(header, subheader)))

## Dividing column with one string into column with list of strings 
for i in range(4):
        df[7].iloc[i][0] = re.split(r' ', str(df[7].iloc[i][0]))

for i in range(4):
    for j in range(1):
        count = 0
        mylist = []
        for item in df[7].iloc[i][j]:
            if count >= 1:
                mylist.append(item)
            count += 1
        df[7].iloc[i][j][1] = " ".join(mylist)

        if count > 2:
            for iter in range(count - 1, 1, -1):
                df[7].iloc[i][j].pop(iter)

## Dividing column with list of two strings into two columns
df[7] = pd.DataFrame(df[7]["Tabela de Tipo de Solicitação"].to_list(), columns = subheader)

## Creating a new empty Dataframe to fill it with df[0] Dataframe
Q32 = pd.DataFrame(np.empty((3, 2), dtype = str), columns = Q32_header)
for i in range(3):
    for j in range(2):
        Q32.iloc[i][j] = df[7].iloc[i + 1][j]

print(Q32, "\n")

# 7. Saving Quadro 32 as a .csv file
Q32_filename = "quadro32"
Q32.to_csv(path_or_buf = Q32_filename + ".csv")

# 8. Zipping all .csv files
cz.zip_this_folder(path = os.path.abspath(os.getcwd()))
