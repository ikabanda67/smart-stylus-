# i am using this file to try to perform the realtime detction of handwritten gestures.
import serial as ser
from sklearn.ensemble import RandomForestClassifier
from joblib import load
from glob import glob 
import time
# real time testing 
pathtofolders = r'C:\Users\Lenovo\OneDrive\Desktop\motion\ML'


# load model, instantiate arduino communication
model = load(f"{pathtofolders}_trained_model.joblib")
com = 'COM5'
baud = 230400
mcu = ser.Serial(com,baud)

classes = {idx: name for idx, name in list(enumerate(glob(f'{pathtofolders}/*.csv')))}
print(classes)
print('starting connection')
count=0

while True:
    if mcu.in_waiting:    
        print(f'Detected {count}')
        string = mcu.readline()
        readings = [float(reading) for reading in string.decode('utf').strip().split(',')[:-1]]
        time.sleep(0.5)
        # predict number and print
        prediction = model.predict([readings])[0]
        prediction2 = model.predict([readings])[0]
        if prediction and prediction2:
            print(f'Number detected: {classes[int(prediction)]}')
        count= count + 1
    pass


