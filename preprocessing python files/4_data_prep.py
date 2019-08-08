# import time
# import pdb
import pandas as pd
# import numpy as np

# read df from csv file
timeseries = pd.read_csv("C:/Users/pgrig/Desktop/neuro/timeseries.csv", sep=',')

# make ID column index name
timeseries.index.name = 'new_ID'


# pdb.set_trace()  # breakpoint


# obtain timeline column titles
cols = timeseries.columns[1:-2]
cols = cols.astype(int)

# Let's thinner our data by removing outliers

# Kick all the years <1986 
for col in cols:
    if (col < 1986):
        timeseries = timeseries.drop([str(col)], axis = 1)
        
# Kick all papers that were published after 2002
# before2002 = timeseries['Year'] <= 2002
# timeseries = timeseries[before2002] # [424668 rows x 27 columns]
  
# Also kick papers that were published before 1986      
after1986 = timeseries['Year'] >= 1986
timeseries = timeseries[after1986] # [381499 rows x 27 columns]

# Kick papers with 0 citations
nonzero = timeseries['tot_ref'] != 0
timeseries_nonzero = timeseries[nonzero] # [105011 rows x 27 columns]

#kick papers with <3 citations
gr_than_two = timeseries['tot_ref'] > 2 
timeseries_gr_than_two = timeseries[gr_than_two] # [39951 rows x 27 columns]

#kick papers with <6 citations
gr_than_five = timeseries['tot_ref'] > 5 
timeseries_gr_than_five = timeseries[gr_than_five] # [18559 rows x 27 columns]

#kick papers with <11 citations
gr_than_ten = timeseries['tot_ref'] > 10 
timeseries_gr_than_ten = timeseries[gr_than_ten] # [8726 rows x 27 columns]

#kick papers with <11 citations
gr_than_twenty = timeseries['tot_ref'] > 20 
timeseries_gr_than_twenty = timeseries[gr_than_twenty] # [8726 rows x 27 columns]

#kick papers with <11 citations
gr_than_thirty = timeseries['tot_ref'] > 30 
timeseries_gr_than_thirty = timeseries[gr_than_thirty] # [8726 rows x 27 columns]

# save timelines as csv file
timeseries.to_csv('timeseries_all.csv', sep=',', index=False, header=True)
timeseries_nonzero.to_csv('timeseries_0.csv', sep=',', index=False, header=True)
timeseries_gr_than_two.to_csv('timeseries_2.csv', sep=',', index=False, header=True)    
timeseries_gr_than_five.to_csv('timeseries_5.csv', sep=',', index=False, header=True)    
timeseries_gr_than_ten.to_csv('timeseries_10.csv', sep=',', index=False, header=True)    
timeseries_gr_than_twenty.to_csv('timeseries_20.csv', sep=',', index=False, header=True)    
timeseries_gr_than_thirty.to_csv('timeseries_30.csv', sep=',', index=False, header=True) 

# We kicked all the papers published before 1986
# Timeline range : 1986 - 2010
# We plan on working for paper lifespan = oo

# 629814 original citations