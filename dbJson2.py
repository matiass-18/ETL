# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 01:15:57 2025

@author: Matias
"""

import pandas as pd

df = pd.read_excel(r"your_route")

df["Fecha de Alquiler"] = pd.to_datetime(df["Fecha de Alquiler"], errors="coerce")
df["Fecha de Entrega"] = pd.to_datetime(df["Fecha de Entrega"], errors="coerce")

df["Fecha de Alquiler"] = df["Fecha de Alquiler"].dt.strftime("%Y-%m-%d")
df["Fecha de Entrega"] = df["Fecha de Entrega"].dt.strftime("%Y-%m-%d")

df = df.fillna("sin información")

df.to_json("dbJson2.json", orient="records", indent=4, force_ascii=False)

print("Conversión completada: dbJson2.json")

