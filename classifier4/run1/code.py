import tensorflow as tf
opt = tf.keras.optimizers.RMSprop(
    learning_rate=0.0001,
    rho=0.9,
    momentum=0.9,
    epsilon=1e-07,
    centered=False,
    name="RMSprop"
)

classifier4 = Sequential()

classifier4.add(Conv2D(32, (3, 3), padding = 'same' ,input_shape=(64,64,3) , activation='relu' ))
classifier4.add(Conv2D(32, (3, 3), padding = 'same' , activation='relu'))   
classifier4.add(MaxPool2D(pool_size=(2, 2) ))

classifier4.add(Conv2D(64, 3, 3, border_mode='same', activation='relu'))
classifier4.add(Conv2D(64, 3, 3, border_mode='same', activation='relu'))
classifier4.add(MaxPool2D(pool_size=(2, 2)))

classifier4.add(Conv2D(128, 3, 3, border_mode='same', activation='relu'))
classifier4.add(Conv2D(128, 3, 3, border_mode='same', activation='relu'))
classifier4.add(MaxPool2D(pool_size=(2, 2)))

classifier4.add(Conv2D(256, 3, 3, border_mode='same', activation='relu'))
classifier4.add(Conv2D(256, 3, 3, border_mode='same', activation='relu'))
classifier4.add(MaxPool2D(pool_size=(2, 2)))


classifier4.add(Flatten())

classifier4.add( Dense(units = 256,activation = 'relu'))
classifier4.add(Dropout(0.5))

classifier4.add( Dense(units = 256,activation = 'relu'))
classifier4.add(Dropout(0.5))

classifier4.add(Dense(1,activation = 'sigmoid' ))

classifier4.compile(optimizer = opt, loss = 'binary_crossentropy', metrics = ['accuracy'] )
classifier4.summary()

import time
start = time.time()
classifier4.fit(training_set,
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

