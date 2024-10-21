import pandas as pd
from datetime import time
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
########################################################################
#question 1

df = pd.read_csv('C:/Users/oury/Documents/GitHub/four_musketeers/Data/question 1,4,5.csv')
df = pd.DataFrame(df)
# df.head()

# Convert date columns to datetime
df['IN_YARD_RECEIPT_DATE'] = pd.to_datetime(df['IN_YARD_RECEIPT_DATE'], format='%m/%d/%Y', errors='coerce')
df['EXPECTED_RECEIPT_DATE'] = pd.to_datetime(df['EXPECTED_RECEIPT_DATE'], format='%m/%d/%Y', errors='coerce')
df.head()
# Convert time columns to timedelta
df['IN_YARD_RECEIPT_TIME'] = pd.to_timedelta(df['IN_YARD_RECEIPT_TIME'])
df['EXPECTED_RECEIPT_TIME'] = pd.to_timedelta(df['EXPECTED_RECEIPT_TIME'])

# Combine date and time into a single datetime column
df['IN_YARD_RECEIPT_DATE_TIME'] = df['IN_YARD_RECEIPT_DATE'] + df['IN_YARD_RECEIPT_TIME']
df['EXPECTED_RECEIPT_DATE_TIME'] = df['EXPECTED_RECEIPT_DATE'] + df['EXPECTED_RECEIPT_TIME']

# Calculate the difference in hours
df['time_difference_hours'] = (df['IN_YARD_RECEIPT_DATE_TIME'] - df['EXPECTED_RECEIPT_DATE_TIME']).dt.total_seconds() / 3600

df = df[[
 'EXPECTED_RECEIPT_DATE',
 'EXPECTED_RECEIPT_TIME',
 'IN_YARD_RECEIPT_DATE',
 'IN_YARD_RECEIPT_TIME',
  'IN_YARD_RECEIPT_DATE_TIME',
 'EXPECTED_RECEIPT_DATE_TIME',
 'time_difference_hours',
'ITEM_NUMBER',
 'RAN_NUMBER',
 'SUPPLIER_NUMBER',
 'SUPPLIER_CITY_NAME',
 'SUPPLIER_STATE_CODE',
 'SUPPLIER_COUNTRY_CODE',
 'TRANSIT_TIME_HOURS',
]]

df['TRANSIT_TIME_HOURS'].value_counts()

# Drop any rows with missing data for the regression
df_clean = df[['time_difference_hours', 'TRANSIT_TIME_HOURS']].dropna()

# Extract the x and y values
x = df['TRANSIT_TIME_HOURS']
y = df['time_difference_hours']

# Perform linear regression using scipy
slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)

# Create the regression line
regression_line = slope * x + intercept

# Plot the scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(x, y, label='Data points')

# Plot the regression line
plt.plot(x, regression_line, color='red', label=f'Regression line (slope={slope:.2f})')

# Add labels and title
plt.xlabel('Transit (miles)')
plt.ylabel('Time Difference (hours)')
plt.title('Linear Regression: Expected/Actual Delivery Time vs Transit Miles')

# Show legend
plt.legend()

# Display the plot
plt.show()