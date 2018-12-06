# notes from Chapter 5

import pandas as pd
from pandas import Series, DataFrame
import numpy as np

# Series and DataFrame are the workhorse data structures

## Series

### A Series is a 1D array-like object with values and names (caled an index)

obj = pd.Series([4,7, -5, 3])

obj

obj.values #an array

obj.index # like range(4) 

### Can create your own index:

obj2 = pd.Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])

obj2

# can use index names for single or multiple selection

obj2['d']

obj2[['a', 'a', 'd', 'c']]

### and operations will keep the index

np.exp(obj2)

### these are very similar to a dict.  fixed-length, ordered dict.

'b' in obj2

'e' in obj2

### can convert dict to Series

sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}

obj3 = pd.Series(sdata)

obj3

sdata

### Series is nicer!

### Can pass an index when converting a dict to select what is kept:

states = ['California', 'Ohio', 'Oregon', 'Texas']

obj4 = pd.Series(sdata, index=states)

obj4

### looking for missing data

pd.isnull(obj4)

pd.notnull(obj4)

### or

obj4.isnull()

### cool alignment feature

obj3 + obj4

## DataFrames

2D

data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'],
        'year': [2000, 2001, 2002, 2001, 2002, 2003],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}
frame = pd.DataFrame(data)

frame

frame.head()

frame.head(2)

### specify the order

pd.DataFrame(data, columns=['year', 'state', 'pop'])


frame2 = pd.DataFrame(data, columns=['year', 'state', 'pop', 'debt'], index=['one', 'two', 'three', 'four', 'five', 'six'])

frame2

#if column with no data, then fills with Nas

frame2.columns

frame2['state']

frame2.state #only works in iPython context?  must be valid python variable name

# get a row:
frame2.loc['three']

# add a column.  if as a series, then indexes get matched.

val = pd.Series([-1.2, -1.5, -1.7], index=['two', 'four', 'five'])

frame2['debt'] = val

frame2


