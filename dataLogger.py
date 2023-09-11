# creating a data logger to be able to store the values of the sensor readings into csv file format 
# for this we create a serial object and pipe the data directly into python 
import serial 
import csv
arduino_port = 'COM5'
baud = 230400
zero = r'C:\Users\Lenovo\OneDrive\Desktop\motion\ML\nine.csv'
one = r'C:\Users\Lenovo\OneDrive\Desktop\motion\accel\zero.csv'

ser = serial.Serial(arduino_port, baud)

print(f'Connected to Arduino port: {arduino_port}')
# file = open(fileName,'a')

print(f'Created file {zero}')
samples = 20
sensor_data = []
line = 0


while line < samples:
    # display the data to the terminal 
    # print(f'line: {line}')
    getData = ser.readline().decode("utf-8").strip()
    # the serial communication transmits the data in binary so we need to
    # to convert it into ascii by decoding 
    datastring = getData[0:][:-2]

    data = datastring.split(',')
    print(data)
    print(len(data))
    sensor_data.append(data)
    line = line + 1

with open(zero, 'w',encoding = 'utf=8',newline = '') as f:
    writer = csv.writer(f)
    writer.writerows(sensor_data)

print('Data collection Complete!')
# file.close()
ser.close()
print(f'Closed file {zero}')