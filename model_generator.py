#---DEPENDENCIES--------------------------------------------------------------+
import numpy as np
import matplotlib.pyplot as plt
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
from tensorflow import keras
from sklearn.model_selection import train_test_split
from PIL import Image

#---DATA----------------------------------------------------------------------+
dataset = input('Enter dataset: ')
dataset_path = f'datasets/{dataset}'

x_data=[]
y_data=[]
count=0
for j in os.listdir(dataset_path):
    print(j)
    for i in os.listdir(dataset_path + '/' +str(j)):
        img = Image.open(dataset_path + '/' +str(j) + '/' + i)
        arr = np.array(img)
        x_data.append(arr)
        y_data.append(j)

img_size = arr.shape[0]

x_data = np.array(x_data, dtype = 'float32')
y_data = np.array(y_data)  
y_data = y_data.reshape(y_data.shape[0], 1)

def one_hot(array):
    unique, inverse = np.unique(array, return_inverse=True)
    onehot = np.eye(unique.shape[0])[inverse]
    return onehot

y_data = one_hot(y_data)

x_data = x_data.reshape((x_data.shape[0],img_size,img_size, 1))
x_data = x_data / 20

x_train,x_test,y_train,y_test = train_test_split(x_data,y_data,test_size = 0.3)
#---MODEL---------------------------------------------------------------------+
print('>>> Do you want a new model or transfer learning to M1 ?')
model_type = input('>>> Enter (N/T) : ')

if model_type == 'N':
    
    # >>> Gesture Categorization Framework
    
    GCF = keras.Sequential()                # initializing Sequential API
    
    GCF.add(keras.layers.Conv2D(            # 3 channel convolutional layer
        filters = 16,
        kernel_size = 4,
        padding = 'same',
        activation = 'relu',
        input_shape = (img_size,img_size,1)))
    GCF.add(keras.layers.MaxPooling2D(      # max pooling
        pool_size = 2))
    GCF.add(keras.layers.Conv2D(            # convo. layer
        filters = 16,
        kernel_size = 2,
        padding = 'same',
        activation = 'relu',))
    # GCF.add(keras.layers.Conv2D(            # convo. layer
    #     filters = 16,
    #     kernel_size = 2,
    #     padding = 'same',
    #     activation = 'relu'))
    # GCF.add(keras.layers.MaxPooling2D(      # max pooling
    #     pool_size = 2))
    
    GCF.add(keras.layers.Flatten())         # dense MLP block
    GCF.add(keras.layers.Dense(             
        108,
        activation = 'relu'))
    GCF.add(keras.layers.Dense(
        64,
        activation = 'relu'))
    GCF.add(keras.layers.Dense(
        9,
        activation = 'softmax'))

#---TRAINING------------------------------------------------------------------+
    GCF.compile(                            # compilation
        loss = 'categorical_crossentropy',
        optimizer = 'adam',
        metrics = ['accuracy'])
    
    callback_protocol = keras.callbacks.EarlyStopping(
        monitor = 'val_loss',
        patience = 3)
    
    history = GCF.fit(
        x = x_train,
        y = y_train,
        batch_size = 10,
        validation_split = 0.2,
        callbacks = callback_protocol,
        epochs = 5)

else:
    GCF = keras.models.load_model(r'models/M1.h5')
    
    GCF.compile(                            # compilation
        loss = 'categorical_crossentropy',
        optimizer = 'adam',
        metrics = ['accuracy'])
    
    callback_protocol = keras.callbacks.EarlyStopping(
        monitor = 'val_loss',
        patience = 3)
    
    history = GCF.fit(
        x = x_train,
        y = y_train,
        batch_size = 10,
        validation_split = 0.2,
        callbacks = callback_protocol,
        epochs = 5)
    
#---EVALUATION----------------------------------------------------------------+
for i in history.history:
    plt.plot(history.history[i])
plt.legend(history.history.keys())
plt.xlabel('epoch')
plt.ylabel('value')
plt.title('evaluation over training')
plt.show()

print("Evaluate on test data")
results = GCF.evaluate(x_test, y_test, batch_size = 2)
print("test loss, test acc:", results)

#---SAVE----------------------------------------------------------------------+
if model_type == 'N':
    model_name = input('New model ; Enter name (M1 is a reserved name): ') + '.h5'
    GCF.save(f'models/{model_name}')
else:
    GCF.save(r'models/M1.h5')


