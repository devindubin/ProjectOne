import pandas as pd
import requests
from lxml import html

file_path_GDP = 'Resources/US_GDP_1960_2019.csv'
file_path_GNP = 'Resources/US_GNP_1960_2019.csv'
GDP = pd.read_csv(file_path_GDP)
GNP = requests.get("https://fred.stlouisfed.org/series/GNPA")
tree = html.fromstring(GNP.content)
print(tree)
#print(GDP.columns)
#print(GDP['LOCATION'].value_counts())
