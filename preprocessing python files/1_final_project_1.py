import time
import pandas as pd
# import numpy as np
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

