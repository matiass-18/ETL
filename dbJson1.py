# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 00:31:13 2025

@author: Matias
"""

import pandas as pd

df = pd.read_excel(r"your_route")

df["Fecha de Alquiler"] = df["Fecha de Alquiler"].dt.strftime("%Y-%m-%d")
df["Fecha de Entrega"] = df["Fecha de Entrega"].dt.strftime("%Y-%m-%d")

df.to_json("dbJson1.json", orient="records", indent=4, force_ascii=False)

print("Conversión completada: dbJson.json1")
