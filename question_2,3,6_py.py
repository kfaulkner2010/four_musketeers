import pandas as pd
from datetime import time 
#######################################################################
#question 2
question_236_df = pd.read_csv("question 2,3,6.csv")
question_236_df= pd.DataFrame(question_236_df)
question_236_df.head(20)
question_236_df[' TASK CREATE TIMESTAMP'] = pd.to_datetime(question_236_df[' TASK CREATE TIMESTAMP'])

shiftstart= time(7,0)
shiftend= time(19,0)
def shift(task_timestamp):
    task_time = task_timestamp.time()  # Get the time part of the timestamp
    if shiftstart <= task_time <= shiftend:
        return 'dayshift'
    else:
        return 'nightshift'
    
question_236_df['shift']= question_236_df[' TASK CREATE TIMESTAMP'].apply(shift)
question_236_df["shift"].value_counts()



##########################################################################
#question 3
#same as question 2 except a different plot




##########################################################################
#question 6 
question_236_df['hour'] = question_236_df[' TASK CREATE TIMESTAMP'].dt.hour
question_236_df.head(20)
