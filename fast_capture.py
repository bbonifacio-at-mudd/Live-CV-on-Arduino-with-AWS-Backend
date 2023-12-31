import numpy as np
import serial
from PIL import Image
import matplotlib.pyplot as plt

def serial_readline(obj):
    data = obj.readline()
    return data.decode("utf-8").strip()

def read_bulk_data(ser, total_bytes):
    return ser.read(total_bytes)

port = 'COM4'
baudrate = 115200

# Initialize serial port
ser = serial.Serial()
ser.port = port
ser.baudrate = baudrate

ser.open()
ser.reset_input_buffer()

while True:
    data_str = serial_readline(ser)

    if data_str == "<image>":
        w, h = int(serial_readline(ser)), int(serial_readline(ser))
        total_pixels = w * h * 3

        print("Reading frame:", w, h)
        # Read bulk data
        bulk_data = read_bulk_data(ser, total_pixels)

        # Convert the bulk data to a NumPy array and reshape it
        image = np.frombuffer(bulk_data, dtype=np.uint8).reshape((h, w, 3))

        if serial_readline(ser) == "</image>":
            print("Captured frame")
            plt.imshow(image)
            plt.show()
        else:
            print("Error capture image")
