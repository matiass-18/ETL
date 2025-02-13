# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 00:16:30 2025

@author: Matias
"""

import pandas as pd

df = pd.read_excel(r"your_route")

df.to_json("dbJson.json", orient="records", indent=4, force_ascii=False)

print("Conversión completada: dbJson.json")


