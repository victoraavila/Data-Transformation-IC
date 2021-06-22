from tabula import read_pdf
import pandas as pd

# 1. Reading desired tables from .pdf and saving them as Pandas Dataframe
pdf_name = "Componente Organizacional.pdf"
pages = [79, 80, 81, 82, 83, 84, 85]

df = read_pdf(pdf_name, pages = pages)
