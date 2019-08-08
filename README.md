# Project for ECE-418 (Neural Networks) : Use Neual Networks with Keras to make predictions on citations' timelines


LSTM_split_sequences.py : the fi
test.py : 
  
What **dataset** did we have? 
* A huge raw, txt dataset from (https://aminer.org/citation - Citation-network V1) with papers published from 1950 and after. 
The information that we are interested in is the citations that each paper made. 

What was our **task**?
  1. Read and process our original data and transform them into a pandas dataframe.
  2. Transform the dataframe into a timeseries.
  3. Decide what type of Neural Network I will use, given the type of the problem (LSTM Neural Nets are popular for timeseries)
  4. Train the network, make predictions on new 'test data', and check its performance based on the 'Loss' metric. 
   
What **type of problem** was it?
* It was a timeseries prediction problem, with really heavy preprocessing, since our original data were massive and in
raw inefficient form. 
    
What **techniques** did we use?
  1. Preprocessing required everything I previously knew including reading from a file and "sequence splitting"
  2. Chosen architecture: LSTM neural network (the most famous for handling timeseries problems)
  3. Alternative: Also tried a CNN-LSTM and a LSTM-Encoder-Decoder network, but they underperformed.
  
  
  
Important to **note**:
* Our data were pretty massive, so we had to make some important decisions based on the limited computational power
of my computer (sampling our data, batch-training).
