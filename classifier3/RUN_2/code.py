classifier3  = Sequential()
classifier3.add(Conv2D(64,(3,3), input_shape=(64,64,3), activation = 'relu'))
classifier3.add(Conv2D(128,(3,3),activation='relu'))

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
	validation       	 (min:    0.723, max:    0.866, cur:    0.853)
	training         	 (min:    0.627, max:    0.922, cur:    0.919)
Loss
	validation       	 (min:    0.161, max:    0.649, cur:    0.230)
	training         	 (min:    0.205, max:    0.639, cur:    0.208)
1655.6418342590332