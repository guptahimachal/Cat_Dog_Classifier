classifier2  = Sequential()
classifier2.add(Convolution2D(32,3,3, input_shape=(64,64,3), activation = 'relu'))
classifier2.add(MaxPool2D(pool_size = (2,2)))

classifier2.add(Convolution2D(32,3,3,activation='relu'))
classifier2.add(MaxPool2D(pool_size = (2,2)))

classifier2.add(Flatten())
classifier2.add(Dense(units = 128,activation = 'relu'))
classifier2.add( Dropout(0.4) )


classifier2.add(Dense(units = 64,activation = 'relu'))
classifier2.add( Dropout(0.4) )

classifier2.add(Dense(units = 1  ,activation = 'sigmoid'))

classifier2.compile(optimizer = 'RMSprop', loss = 'binary_crossentropy', metrics = ['accuracy'] )



# Training
import time
start = time.time()
classifier2.fit(training_set,
                epochs = 25,
               steps_per_epoch = 2000,
               validation_data= test_set,
               validation_steps = 500,
               callbacks=[PlotLossesKeras(),
               CSVLogger( TRAINING_LOGS_FILE, append=True,separator=";" )] 
              )

end = time.time()
classifier2_time = end - start
print(classifier2_time)

# Time in seconds to train 7460.69514131546

Model: "sequential_2"
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
conv2d_3 (Conv2D)            (None, 62, 62, 32)        896       
_________________________________________________________________
max_pooling2d_2 (MaxPooling2 (None, 31, 31, 32)        0         
_________________________________________________________________
conv2d_4 (Conv2D)            (None, 29, 29, 32)        9248      
_________________________________________________________________
max_pooling2d_3 (MaxPooling2 (None, 14, 14, 32)        0         
_________________________________________________________________
flatten_2 (Flatten)          (None, 6272)              0         
_________________________________________________________________
dense_3 (Dense)              (None, 128)               802944    
_________________________________________________________________
dropout_2 (Dropout)          (None, 128)               0         
_________________________________________________________________
dense_4 (Dense)              (None, 64)                8256      
_________________________________________________________________
dropout_3 (Dropout)          (None, 64)                0         
_________________________________________________________________
dense_5 (Dense)              (None, 1)                 65        
=================================================================
Total params: 821,409
Trainable params: 821,409
Non-trainable params: 0
_________________________________________________________________
