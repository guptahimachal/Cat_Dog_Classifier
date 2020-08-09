import time
start = time.time()
classifier3.fit(training_set,
               epochs = 40,
               steps_per_epoch = 400,
               validation_data= test_set,
               validation_steps = 100,
               callbacks=[PlotLossesKeras(),
               CSVLogger( TRAINING_LOGS_FILE, append=True,separator=";" )] 
              )

end = time.time()
classifier3_time = end - start
print(classifier3_time)


accuracy
	validation       	 (min:    0.494, max:    0.885, cur:    0.862)
	training         	 (min:    0.499, max:    0.892, cur:    0.888)
Loss
	validation       	 (min:    0.136, max:    1.396, cur:    0.497)
	training         	 (min:    0.271, max:    0.694, cur:    0.281)
3052.0956897735596



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

Model: "sequential_3"
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
conv2d_10 (Conv2D)           (None, 62, 62, 64)        1792      
_________________________________________________________________
conv2d_11 (Conv2D)           (None, 60, 60, 128)       73856     
_________________________________________________________________
conv2d_12 (Conv2D)           (None, 58, 58, 256)       295168    
_________________________________________________________________
max_pooling2d_6 (MaxPooling2 (None, 29, 29, 256)       0         
_________________________________________________________________
conv2d_13 (Conv2D)           (None, 27, 27, 256)       590080    
_________________________________________________________________
max_pooling2d_7 (MaxPooling2 (None, 13, 13, 256)       0         
_________________________________________________________________
conv2d_14 (Conv2D)           (None, 11, 11, 512)       1180160   
_________________________________________________________________
max_pooling2d_8 (MaxPooling2 (None, 5, 5, 512)         0         
_________________________________________________________________
flatten_3 (Flatten)          (None, 12800)             0         
_________________________________________________________________
dense_5 (Dense)              (None, 256)               3277056   
_________________________________________________________________
dropout_3 (Dropout)          (None, 256)               0         
_________________________________________________________________
dense_6 (Dense)              (None, 1)                 257       
=================================================================
Total params: 5,418,369
Trainable params: 5,418,369
Non-trainable params: 0



