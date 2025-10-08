import serial
import time

ser = serial.Serial('com', 9600)

while True:
    ser.write(b'Hello, Arduino!')
    time.sleep(1)