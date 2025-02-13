# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 00:58:58 2025

@author: Matias
"""

import pandas as pd

df = pd.read_excel(r"C:\Users\Matias\Desktop\Uni\trabajosU\BigData\tablaOrganizada.xlsx")

df["Fecha de Alquiler"] = df["Fecha de Alquiler"].dt.strftime("%Y-%m-%d")
df["Fecha de Entrega"] = df["Fecha de Entrega"].dt.strftime("%Y-%m-%d")

df = df.dropna(subset=df.columns[1:], how="all")

df.to_excel("dbLimpia.xlsx", index=False, engine="openpyxl")

print("Archivo limpio guardado como 'dbLimpia.xlsx'")
