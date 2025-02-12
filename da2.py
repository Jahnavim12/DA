# -*- coding: utf-8 -*-
"""da2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1gRjFPfDtooabPs3VfAU6-UiDUBJ83WP2
"""

from bs4 import BeautifulSoup

import pandas as pd

import requests

density_response=requests.get("https://visaguide.world/asia/")

density_response.status_code

density_response.text

type(density_response.text)

densitysoup=BeautifulSoup(density_response.text,"html.parser")

densitytables=densitysoup.find_all("table")

len(densitytables)

densityheaders_tag=densitytables[1].find_all("th")
print(densityheaders_tag)

densityheaders=[i.text for i in densityheaders_tag]
print(densityheaders)

densityrows_tag=densitytables[1].find_all("td")
densityrows_tag

densityrows=[i.text for i in densityrows_tag]
densityrows

density_dict={}
n=0
for i in densityheaders:
  density_dict[i]=[densityrows[j] for j in range (n,len(densityrows),len(densityheaders))]
  n+=1
density_dict

density_df=pd.DataFrame(density_dict)
density_df

density_df.index=range(1,len(density_df)+1)
density_df

density_df.to_csv("density_data.csv")

density_df_sorted=density_df.sort_values(by="Population_density",ascending=False)
density_df_sorted.head()

import matplotlib.pyplot as plt
x=density_df["Country"][:20]
y=density_df["Population_density"][:20]
plt.xticks(rotation=90)
plt.bar(x,y)
plt.show()

density_df["Population (2021)"]=density_df["Population (2021)"].str.replace(",","").astype(int)

density_df["Area km2"]=density_df["Area km2"].str.replace(",","").astype(int)

density_df["Population_density"]=density_df["Population (2021)"]/density_df["Area km2"]

