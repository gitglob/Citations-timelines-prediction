# import time
import pandas as pd
import numpy as np
# import pdb


# read df from csv file.


timeseries = pd.read_csv("C:/Users/pgrig/Desktop/neuro/timeseries_30.csv", sep=',')
# [2456 rows x 28 columns]


# get a random smaller sample from our data
# timeseries = timeseries.sample(frac = 0.01, replace = False,  random_state=1)
# timeseries = timeseries.reset_index(drop=True)
# [5866 rows x 27 columns]

# final data preperation

# obtain timeline column titles
cols = timeseries.columns

# get indexes for years
unique_index = pd.Index(cols)

# make every paper start from the year it was released
for index, row in timeseries.iterrows():
    # print progress
    if (index + 1) % 500 == 0:
        print ('501 done..')
    
    # get year of publication
    year = str(timeseries.Year[index])
    
    # get lifespan of this paper until year 2009
    lifespan = 2010 - int(year)
    
    # column that this year appears
    col_index = unique_index.get_loc(year)
    
    # shift references taken left so that we begin with the first year after publication
    for i in range (lifespan):
        timeseries.iloc[index, i+1] = timeseries.iloc[index, col_index + i]   
        
    # make remaining columns 0 values
    for i in range (25 - lifespan):
        timeseries.iloc[index, -3 -i] = np.NaN
           
# change columns names from [1986... 2010] to consecutive integers [0,1,2,3...11]
new_cols = np.arange(25)
timeseries.rename(columns = dict(zip(timeseries.columns[1:-2], new_cols)), inplace=True)

# drop last 2 columns
timeseries = timeseries.drop(['ID','tot_ref','Year'], axis=1)

# save timeline as csv file
timeseries.to_csv('timeseries_final_form_30.csv', sep=',', index=False, header=True)