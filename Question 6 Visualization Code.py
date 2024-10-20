import pandas as pd
from datetime import time
import matplotlib.pyplot as plt
import numpy as np
#############################################################################
# question 6
question_236_df = pd.read_csv("C:/Users/oury/Documents/GitHub/four_musketeers/Data/question 2,3,6.csv")
question_236_df[' TASK CREATE TIMESTAMP'] = pd.to_datetime(question_236_df[' TASK CREATE TIMESTAMP'])
question_236_df['hour'] = question_236_df[' TASK CREATE TIMESTAMP'].dt.hour
y_axis = question_236_df['hour'].value_counts()

# Sort the y_axis by the index (the hour values)
y_axis_sorted = y_axis.sort_index()

# Now you can get the sorted x-axis and y-axis
x_axis_sorted = y_axis_sorted.index
y_axis_sorted_values = y_axis_sorted.values

# Convert to lists if needed
x_axis_list = x_axis_sorted.tolist()
y_axis_list = y_axis_sorted_values.tolist()

# Now x_axis_list is sorted numerically and matches y_axis_list
# print("X-axis (sorted):", x_axis_list)
# print("Y-axis (sorted):", y_axis_list)

hours, = plt.plot(x_axis_list, y_axis_list, marker="o")
plt.title('Materials Shipped By Hour')
plt.xlabel('Hour')
plt.ylabel('Materials Shipped')
plt.xticks(x_axis_sorted)  
plt.grid()
plt.show()