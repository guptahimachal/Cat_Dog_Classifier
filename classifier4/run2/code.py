import tensorflow as tf
opt = tf.keras.optimizers.RMSprop(
    learning_rate=0.0001,
    rho=0.9,
    momentum=0.9,
    epsilon=1e-07,
    centered=False,
    name="RMSprop"
)

from keras.layers import BatchNormalization
from keras.layers import ZeroPadding2D




# USE ALL THE LAYERS FROM tf.
# and see about RMSprop if still not work





def getModel():
  model4 = Sequential()
  model4.add(Conv2D(64,(3,3), input_shape=(128,128,3), activation = 'relu'))
  model4.add(Conv2D(128,(3,3),activation='relu'))
  
  model4.add(Conv2D(256,(3,3),activation='relu'))
  model4.add(MaxPool2D(pool_size = (2,2)))

  model4.add(Conv2D(256,(3,3),activation='relu'))
  model4.add(MaxPool2D(pool_size = (2,2)))

  model4.add(Conv2D(512,(3,3),activation='relu'))
  model4.add(MaxPool2D(pool_size = (2,2)))


  model4.add(Flatten())
  model4.add(Dense(units = 256,activation = 'relu'))
  model4.add( Dropout(0.4) )



  model4.add(Dense(units = 1  ,activation = 'sigmoid'))

  model4.compile(optimizer = opt, loss = 'binary_crossentropy', metrics = ['accuracy'] )

  
  return model4



Model: "sequential_1"
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
conv2d_1 (Conv2D)            (None, 126, 126, 64)      1792      
_________________________________________________________________
conv2d_2 (Conv2D)            (None, 124, 124, 128)     73856     
_________________________________________________________________
conv2d_3 (Conv2D)            (None, 122, 122, 256)     295168    
_________________________________________________________________
max_pooling2d_1 (MaxPooling2 (None, 61, 61, 256)       0         
_________________________________________________________________
conv2d_4 (Conv2D)            (None, 59, 59, 256)       590080    
_________________________________________________________________
max_pooling2d_2 (MaxPooling2 (None, 29, 29, 256)       0         
_________________________________________________________________
conv2d_5 (Conv2D)            (None, 27, 27, 512)       1180160   
_________________________________________________________________
max_pooling2d_3 (MaxPooling2 (None, 13, 13, 512)       0         
_________________________________________________________________
flatten_1 (Flatten)          (None, 86528)             0         
_________________________________________________________________
dense_1 (Dense)              (None, 256)               22151424  
_________________________________________________________________
dropout_1 (Dropout)          (None, 256)               0         
_________________________________________________________________
dense_2 (Dense)              (None, 1)                 257       
=================================================================
Total params: 24,292,737
Trainable params: 24,292,737
Non-trainable params: 0
_________________________________________________________________



# Train completely and try withmore dataset and
# changing batch sizes
import time
start = time.time()
model.fit(training_set,
                epochs = 25,
                steps_per_epoch = 500,
                validation_data= test_set,
                validation_steps = 125,
                callbacks=[PlotLossesKeras(),
                CSVLogger( TRAINING_LOGS_FILE, append=True,separator=";" )] 
              )

end = time.time()
classifier4_time = end - start
print(classifier4_time)


accuracy
	validation       	 (min:    0.562, max:    0.912, cur:    0.887)
	training         	 (min:    0.512, max:    0.863, cur:    0.849)
Loss
	validation       	 (min:    0.076, max:    0.831, cur:    0.125)
	training         	 (min:    0.341, max:    0.693, cur:    0.373)
7123.349752664566

