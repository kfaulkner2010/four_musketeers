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

shift_counts = question_236_df['shift'].value_counts()

plt.figure(figsize=(8, 8))
plt.pie(shift_counts, labels=shift_counts.index, autopct='%1.1f%%', startangle=140, colors=['#ff9999','#66b3ff'])
plt.title('Distribution of Shifts')
plt.savefig("shift_distribution.png") 
plt.show()
