import pandas as pd
import numpy as np

# read the input_test data
test_data = pd.read_csv(r"test_data\timeseries10.txt"
                        , sep=" ", header=None)

# number of columns
cols = test_data.shape[1]

# take the values from the test data
test = test_data.values

# take as input each row before NaN values
#non_nan_values = np.argwhere(~np.isnan(test[0,:]))
#test = test[0,:][non_nan_values]

# normalize the test data and keep NaN values
# the NaN value is the one we want to predict
#where_are_NaNs = np.isnan(test)
#test_scaled = (test - x_min)/(x_max - x_min)
#test_scaled[where_are_NaNs] = np.NaN
#test = test_scaled

# make it the proper form
test_x, test_y = split_sequence(test[0,:], n_steps)

# make it 3-D
# reshape from [samples, timesteps] into [samples, timesteps, features]
test_x = test_x.reshape((test_x.shape[0], n_steps, n_features))

# predict next year
predictions = model.predict(test_x, batch_size=None, verbose=1)

print ('Next year\'s prediction:', predictions[-1], '\n')

# print MSE for our test data except the value that we want to predict
loss = np.average((predictions[:-1] - test_y[:-1].reshape(predictions[:-1].shape[0],1))**2)
print ('Loss:', loss)

# inverse transform predictions, test
#predictions_inverse = ( predictions*(x_max-x_min) ) + x_min
predictions_round = np.round(predictions)
#test_inverse = ( test_y*(x_max-x_min) ) + x_min

# compare our predictions
plt.scatter(np.arange(len(predictions_round)), predictions_round, marker = '*', color = 'black', label = 'predictions')
plt.scatter(np.arange(len(test_y)), test_y, s=40, facecolors='none', edgecolors='red', label = 'true values')
plt.title('predictions vs real values')
plt.legend(loc='upper left')
plt.show() 


# print MSE for our test data
loss = np.average((predictions_round[:-1] - test_y[:-1].reshape(predictions_round[:-1].shape[0],1))**2)
print ('Loss:', loss, '\n')