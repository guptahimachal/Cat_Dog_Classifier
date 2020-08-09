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

_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
conv2d (Conv2D)              (None, 126, 126, 64)      1792      
_________________________________________________________________
conv2d_1 (Conv2D)            (None, 124, 124, 128)     73856     
_________________________________________________________________
conv2d_2 (Conv2D)            (None, 122, 122, 256)     295168    
_________________________________________________________________
max_pooling2d (MaxPooling2D) (None, 61, 61, 256)       0         
_________________________________________________________________
conv2d_3 (Conv2D)            (None, 59, 59, 256)       590080    
_________________________________________________________________
max_pooling2d_1 (MaxPooling2 (None, 29, 29, 256)       0         
_________________________________________________________________
conv2d_4 (Conv2D)            (None, 27, 27, 512)       1180160   
_________________________________________________________________
max_pooling2d_2 (MaxPooling2 (None, 13, 13, 512)       0         
_________________________________________________________________
flatten (Flatten)            (None, 86528)             0         
_________________________________________________________________
dense (Dense)                (None, 256)               22151424  
_________________________________________________________________
dropout (Dropout)            (None, 256)               0         
_________________________________________________________________
dense_1 (Dense)              (None, 1)                 257       
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



Accuracy
  training           (min:    0.498, max:    0.850, cur:    0.850)
  validation         (min:    0.501, max:    0.910, cur:    0.891)
Loss
  training           (min:    0.358, max:    0.694, cur:    0.363)
  validation         (min:    0.263, max:    0.696, cur:    0.292)
500/500 [==============================] - 150s 300ms/step - loss: 0.3630 - acc: 0.8495 - val_loss: 0.2922 - val_acc: 0.8911
3758.253257036209





