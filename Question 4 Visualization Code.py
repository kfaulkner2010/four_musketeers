import pandas as pd
from datetime import time
import matplotlib.pyplot as plt
import numpy as np

################################################
# Question 4



df = pd.read_csv("C:/Users/oury/Documents/GitHub/four_musketeers/Data/question 1,4,5.csv")


def supplier_classification(supplier_country):
    if supplier_country == 'USA':
        return 'Domestic'
    else:
        return 'International'
df['International or Domestic'] = df['SUPPLIER_COUNTRY_CODE'].apply(supplier_classification)
# df.head(20)

location = df['International or Domestic'].value_counts()




# plt.figure(figsize=(8, 8))
plt.pie(location, labels=location.index, autopct='%1.1f%%', startangle=90, colors=['#0000FF','#FFFF00'])
plt.title('Source of Material')
plt.show()