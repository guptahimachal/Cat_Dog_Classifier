import time
start = time.time()
classifier3.fit(training_set,
               epochs = 25,
               steps_per_epoch = 5000,
               validation_data= test_set,
               validation_steps = 1250,
               callbacks=[PlotLossesKeras(),
               CSVLogger( TRAINING_LOGS_FILE, append=True,separator=";" )] 
              )

end = time.time()
classifier3_time = end - start
print(classifier3_time)