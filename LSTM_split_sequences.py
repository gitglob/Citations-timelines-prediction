import time
# import pdb
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers.core import Dense
from keras.layers import LSTM
from keras import optimizers
from sklearn.model_selection import train_test_split 

# Read data from csv
timeseries = pd.read_csv("C:/Users/pgrig/Desktop/neuro/timeseries_final_form_30.csv", sep=',') 
# [9364 rows x 11 columns]

np.random.seed(seed = 0)

# get a random smaller sample from our data
#timeseries = timeseries.sample(frac = 0.05, replace = False,  random_state=7)
#timeseries = timeseries.reset_index(drop=True)

# pass dataframe to a numpy array
x = timeseries.values 

# prepare our data for timeseries predictions

# split a univariate sequence into samples
def split_sequence(sequence, n_steps):
	X, y = list(), list()
	for i in range(len(sequence)):
		# find the end of this pattern
		end_ix = i + n_steps
		# check if we are beyond the sequence
		if end_ix > len(sequence)-1:
			break
		# gather input and output parts of the pattern
		seq_x, seq_y = sequence[i:end_ix], sequence[end_ix]
		X.append(seq_x)
		y.append(seq_y)
	return np.array(X), np.array(y)

# choose a number of time steps
n_steps = 3
n_features = 1

# needed to run without errors
j = 0

# split into samples for every row
for i in range(x.shape[0]):

    # take as input each row before NaN values
    non_nan_values = np.argwhere(~np.isnan(x[i,:]))
    t = x[i,:][non_nan_values]
    
    # if the row is too short (<5), ignore it
    if t.shape[0] < 5:
        j = j + 1
        continue
    else:
        
        temp_X, temp_y = split_sequence(t, n_steps)
        
        if (i - j)==0:
            X, y = temp_X, temp_y
        else:
            X = np.append(X, temp_X, axis = 0)
            y = np.append(y, temp_y, axis = 0)

##############################################################################################################################

# reshape from [samples, timesteps] into [samples, timesteps, features]
X = X.reshape((X.shape[0], n_steps, n_features))

# split to train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

# define parameters
batch_size = 100
max_epochs = 100

# LSTM model
model = Sequential()
# define network
# first hidden layer
model.add(LSTM(10, activation = 'relu', batch_input_shape=(None, n_steps, n_features),
               return_sequences=False, stateful=False))
# second hidden layer
#model.add(LSTM(10))
# output layer
model.add(Dense(1, activation = 'relu'))
# Define compiler and compile model
#opt = optimizers.SGD(lr=0.000004, momentum=0.0, decay=0.00, nesterov=False)
#opt = optimizers.RMSprop(lr=0.00004, rho=0.9, epsilon=None, decay=0.0)
opt = optimizers.Adam(lr=0.0004, beta_1=0.9, beta_2=0.999, epsilon=None, decay=0.0, amsgrad=False)
model.compile(optimizer=opt, loss='mean_squared_error', metrics=['acc'])
# check summary
model.summary()

# Here we train the network and keep the execution time
start = time.time()
history = model.fit(X_train, y_train ,batch_size = batch_size, epochs = max_epochs, verbose = 2, 
                    validation_data=(X_test, y_test))
end = time.time()
print ('\nTraining time:', (end - start), 'sec')

# extract the weights for every layer
for layer in model.layers:
    weights = layer.get_weights()
    
print ('Layer weights:', weights)

##############################################################################################################################
    
# check our Loss plot
plt.plot(history.history['loss'], color = 'blue', label = 'training loss')
plt.plot(history.history['val_loss'], color = 'red', label = 'validation loss')
plt.title('Loss')
plt.legend()
plt.show()  

print ('min training Loss:', np.min(history.history['loss']))

##############################################################################################################################

# Check loss on validation set
print ('\nLoss:', history.history['val_loss'][-1])

# make predictions on validation set
results = model.predict(X_test, batch_size=None, verbose=0)
results_round = np.round(results)

# calculate accuracy in prediction by hand
hits = results_round == y_test.reshape(y_test.shape[0],1)
counts = hits.sum()
acc = counts/len(hits)
print ('Accuracy:', 100*acc, '%')
print ('Attention! Accuracy means nothing in our case! Loss is what we care about. We don\'t expect to predict the exact values')

# compare our predictions
plt.scatter(np.arange(len(results_round)), results_round, marker = '*', color = 'black', label = 'predictions')
plt.scatter(np.arange(len(y_test)), y_test, s=40, facecolors='none', edgecolors='red', label = 'true values')
plt.title('predictions vs real values')
plt.legend(loc='upper left')
plt.show()  

