import time
import pandas as pd
import numpy as np
import pdb

# measure time elapsed
start_time = time.time()

# create dataframe to store initial data
df = pd.DataFrame([], columns=['Year', 'Ref made'])

# read our file
filename = "C:\Users\pgrig\Desktop\neuro\data.txt"
fh = open(filename, "r", encoding='utf-8')


pdb.set_trace()  # breakpoint 1


# Search our data and store the values we need!

# initial position in file
start_pos = fh.tell()

# initialize reference counter
ref_counter = 0

# counter for our rows
title_counter = 0

# Run through the entire file
line = fh.readline()

line = line.strip('\ufeff\n')  # remove starting special characters
while line:

    # Every title
    if line.find("#t") != -1:
        line = line.strip('#t')

        # increase rows counter
        title_counter += 1
        
        # print progress
        if title_counter % 50000 == 0:
            print('\t\t\t\t\t\t50.000 done...!!')

        # Don't finish the file
        # if title_counter == 500:
        #     break

        # create new entry to 'df' (add year to 'df')
        df = df.append({'Year': line}, ignore_index=True)

        # initialize the reference made column
        df.iloc[title_counter - 1, 1] = ''

        # print('Year:', line)  # debug

    elif line.find("#%") != -1:
        line = line.strip('#%')

        # increase reference counter
        ref_counter += 1

        # add reference to 'df'
        df.iloc[title_counter - 1, 1] += line
        df.iloc[title_counter - 1, 1] += ','

        # print('Reference:', line)  # debug

    # Move to next line
    line = fh.readline()

# close file
fh.close()

# measure time
elapsed_time = time.time() - start_time
print('Elapsed time parsing our data from the file:', elapsed_time)

# Remove '\n' from columns
cols_to_check = ['Year', 'Ref made']
df[cols_to_check] = df[cols_to_check].replace({'\n': ''}, regex=True)
df.index.name = 'ID'

# save df as csv file
df.to_csv('df_final.csv', sep=',', index=True, header=True)


pdb.set_trace()  # breakpoint 2.1


# read df from csv file
df_final = pd.read_csv("C:/Users/pgrig/Desktop/neuro/df_final.csv", sep=',')

# make ID column index name
df_final.index.name = 'ID'
df_final = df_final.drop(['ID'], axis = 1)

# replace all nan values with '0'
cols_to_check = df_final.columns
df_final[cols_to_check] = df_final[cols_to_check].replace({np.nan: 0}, regex=True)


pdb.set_trace()  # breakpoint 2.2


# prepare for creation of 'timeline' dataframe

# store unique years that appear in dataframe df
time = df_final.Year
time = np.unique(time)
time = list(time)

# Create our "timeline" dataframe to store Years and references
timeline = pd.DataFrame(0, index=np.arange(629814), columns=time )

# Create column for total references taken
timeline["tot_ref"] = int(0)

# keep column to indicate the year that the paper was published
year_col = df_final["Year"]

# Remove nan values from timeline
cols_to_check = timeline.columns
timeline[cols_to_check] = timeline[cols_to_check].replace({np.nan: 0}, regex=True)


# search for non-empty cells in Ref made column in df
for i in range(0, 629814):   
    if df_final.iloc[i, 1]:
        # references made
        value = df_final.iloc[i, 1]

        # number of references made
        number = value.count(",")

        # convert string -> array
        value = value.split(',')
        del (value[number])

        # print (value,number)#debug

        # increase references taken counter in 'timeline' based on the references made in 'df'
        for j in range(0, number):
            # increase year counter
            year = df_final.iloc[i, 0]
            timeline.loc[int(value[j]), year] += 1

            # increase total counter
            timeline.loc[int(value[j]), 'tot_ref'] += 1

# drop columns '-1', '1900' and '2018' because they are obviously some kind of a mistake
timeline = timeline.drop([-1], axis = 1)
timeline = timeline.drop([1900], axis = 1)
timeline = timeline.drop([2018], axis = 1)


# save years of publication to csv file
year_col.to_csv('year_publ.csv', sep=',', index=True, header=True)

# save timeline as csv file
timeline.to_csv('timeline.csv', sep=',', index=True, header=True)


pdb.set_trace()  # breakpoint 3.1


# read df from csv file
year_col = pd.read_csv("C:/Users/pgrig/Desktop/neuro/year_publ.csv", sep=',')

# make ID column index name
year_col.index.name = 'ID'
year_col = year_col.drop(['ID'], axis = 1)

# read df from csv file
timeline = pd.read_csv("C:/Users/pgrig/Desktop/neuro/timeline.csv", sep=',')

# make ID column index name
timeline.index.name = 'ID'
timeline = timeline.drop(timeline.columns[0], axis = 1)


pdb.set_trace()  # breakpoint 3.2


# save timeline as csv file
timeline.to_csv('timeline_final.csv', sep=',', index=True, header=True)



# 629814 citations
