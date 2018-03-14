import numpy as np
import pandas as pd
import random

"""
(INNER) JOIN: Returns records that have matching values in both tables
LEFT (OUTER) JOIN: Return all records from the left table, and the matched records from the right table
RIGHT (OUTER) JOIN: Return all records from the right table, and the matched records from the left table
FULL (OUTER) JOIN: Return all records when there is a match in either left or right table
"""

# generate the data
np.random.seed(10)  #Setting seed for reproducability
x = np.array([i*np.pi/180 for i in range(60,300,4)])
y = np.sin(x) + np.random.normal(0,0.15,len(x))
df1 = pd.DataFrame(np.column_stack([x,y]))
df2 = pd.DataFrame(np.column_stack([x,y]),columns=['x','y'])

# inner join
pd.merge(df1, df2, left_index=True, right_index=True)

# left join
df1.join(df2)

# outer join
pd.concat([df1, df2], axis=1)
