import pandas as pd
import datetime
#########################################################################
#question 1
df = pd.read_csv('question 1,4,5.csv')
df = pd.DataFrame(df)
df.head()

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

df.head(20)






###################################################################
#question 4
def supplier_classification(supplier_country):
    if supplier_country == 'USA':
        return 'Domestic'
    else:
        return 'International'
df['International or Domestic'] = df['SUPPLIER_COUNTRY_CODE'].apply(supplier_classification)
df.head(20)




