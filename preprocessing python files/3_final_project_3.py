# import time
import pandas as pd
# import numpy as np
import pdb

# read df from csv file
year_col = pd.read_csv("C:/Users/pgrig/Desktop/neuro/year_publ.csv", sep=',')

# make ID column index name
year_col.index.name = 'new_ID'
year_col = year_col.drop(['ID'], axis = 1)

# read df from csv file
timeline = pd.read_csv("C:/Users/pgrig/Desktop/neuro/timeline.csv", sep=',')

# make ID column index name
timeline.index.name = 'new_ID'
timeline = timeline.rename(columns = {'Unnamed: 0':'ID'})


pdb.set_trace()  # breakpoint 3.1


# concatenate both dataframes
timeseries = pd.concat([timeline, year_col], axis=1, sort=False)

# save df to csv
timeseries.to_csv('timeseries.csv', sep=',', index=False, header=True)   


