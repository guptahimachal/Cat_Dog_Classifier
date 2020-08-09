Accuracy
	training         	 (min:    0.593, max:    0.888, cur:    0.884)
	validation       	 (min:    0.621, max:    0.890, cur:    0.881)
Loss
	training         	 (min:    0.281, max:    0.668, cur:    0.292)
	validation       	 (min:    0.306, max:    0.654, cur:    0.306)
500/500 [==============================] - 199s 399ms/step - loss: 0.2915 - acc: 0.8838 - val_loss: 0.3058 - val_acc: 0.8810
5000.180477619171






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





# 1 Epoch 3 minutes on TPU without conversio of input data to tf.data.Dataset
# Total 25 Epochs 5000.180477619171 seconds (double of that by GPU)

