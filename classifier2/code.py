classifier2  = Sequential()
classifier2.add(Convolution2D(32,3,3, input_shape=(64,64,3), activation = 'relu'))
classifier2.add(MaxPool2D(pool_size = (2,2)))

classifier2.add(Convolution2D(32,3,3,activation='relu'))
classifier2.add(MaxPool2D(pool_size = (2,2)))

classifier2.add(Flatten())
classifier2.add(Dense(units =128,activation = 'relu'))
classifier2.add( Dropout(0.4) )

classifier2.add(Dense(units = 1  ,activation = 'sigmoid'))

classifier2.compile(optimizer = 'RMSprop', loss = 'binary_crossentropy', metrics = ['accuracy'] )