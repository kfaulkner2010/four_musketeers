import pandas as pd
from datetime import time
import matplotlib.pyplot as plt

question_236_df = pd.read_csv("question 2,3,6.csv")

question_236_df[' TASK CREATE TIMESTAMP'] = pd.to_datetime(question_236_df[' TASK CREATE TIMESTAMP'])

shiftstart = time(7, 0)
shiftend = time(19, 0)

def shift(task_timestamp):
    task_time = task_timestamp.time() 
    if shiftstart <= task_time <= shiftend:
        return 'dayshift'
    else:
        return 'nightshift'

question_236_df['shift'] = question_236_df[' TASK CREATE TIMESTAMP'].apply(shift)

question_236_df['date'] = question_236_df[' TASK CREATE TIMESTAMP'].dt.date

question_236_df['ship_count'] = question_236_df[' TASK CODE'].str.contains('ship', case=False, na=False).astype(int)

shift_ship_counts = question_236_df.groupby(['date', 'shift'])['ship_count'].sum().unstack().fillna(0)

shift_ship_counts.plot(kind='line', figsize=(18, 6), color=['#FF5733', '#33C3FF']) 
plt.title('Material Shipped by Shift')
plt.xlabel('Date')
plt.ylabel('Quantity Shipped')
plt.legend(title='Shift')
plt.grid(True)
plt.savefig("material_by_shift.png")
plt.show()
