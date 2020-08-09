from keras.optimizers import RMSprop
opt = tf.keras.optimizers.RMSprop(
    learning_rate=0.0001,
    rho=0.9,
    momentum=0.9,
    epsilon=1e-07,
    centered=False,
    name="RMSprop"
)


classifier3  = Sequential()
classifier3.add(Conv2D(64,(3,3), input_shape=(64,64,3), activation = 'relu'))
classifier3.add(Conv2D(128,(3,3),activation='relu'))

classifier3.add(Conv2D(256,(3,3),activation='relu'))
classifier3.add(MaxPool2D(pool_size = (2,2)))

classifier3.add(Conv2D(256,(3,3),activation='relu'))
classifier3.add(MaxPool2D(pool_size = (2,2)))


classifier3.add(Conv2D(512,(3,3),activation='relu'))
classifier3.add(MaxPool2D(pool_size = (2,2)))


classifier3.add(Flatten())
classifier3.add(Dense(units = 256,activation = 'relu'))
classifier3.add( Dropout(0.4) )



classifier3.add(Dense(units = 1  ,activation = 'sigmoid'))

classifier3.compile(optimizer = opt, loss = 'binary_crossentropy', metrics = ['accuracy'] )

classifier3.summary()



Model: "sequential_2"
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
conv2d_5 (Conv2D)            (None, 62, 62, 64)        1792      
_________________________________________________________________
conv2d_6 (Conv2D)            (None, 60, 60, 128)       73856     
_________________________________________________________________
conv2d_7 (Conv2D)            (None, 58, 58, 256)       295168    
_________________________________________________________________
max_pooling2d_3 (MaxPooling2 (None, 29, 29, 256)       0         
_________________________________________________________________
conv2d_8 (Conv2D)            (None, 27, 27, 256)       590080    
_________________________________________________________________
max_pooling2d_4 (MaxPooling2 (None, 13, 13, 256)       0         
_________________________________________________________________
conv2d_9 (Conv2D)            (None, 11, 11, 512)       1180160   
_________________________________________________________________
max_pooling2d_5 (MaxPooling2 (None, 5, 5, 512)         0         
_________________________________________________________________
flatten_2 (Flatten)          (None, 12800)             0         
_________________________________________________________________
dense_3 (Dense)              (None, 256)               3277056   
_________________________________________________________________
dropout_2 (Dropout)          (None, 256)               0         
_________________________________________________________________
dense_4 (Dense)              (None, 1)                 257       
=================================================================
Total params: 5,418,369
Trainable params: 5,418,369


import time
start = time.time()
classifier3.fit(training_set,
               epochs = 25,
               steps_per_epoch = 500,
               validation_data= test_set,
               validation_steps = 125,
               callbacks=[PlotLossesKeras(),
               CSVLogger( TRAINING_LOGS_FILE, append=True,separator=";" )] 
              )

end = time.time()
classifier3_time = end - start
print(classifier3_time)



accuracy
	validation       	 (min:    0.500, max:    0.891, cur:    0.891)
	training         	 (min:    0.507, max:    0.892, cur:    0.887)
Loss
	validation       	 (min:    0.111, max:    1.244, cur:    0.297)
	training         	 (min:    0.269, max:    0.695, cur:    0.283)
2475.5413312911987