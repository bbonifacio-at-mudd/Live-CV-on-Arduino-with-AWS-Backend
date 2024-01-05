import numpy as np
import serial
from PIL import Image
import matplotlib.pyplot as plt

import os
from datetime import datetime

# Directory to save images
save_dir = r"C:\Users\Brandon\Desktop\Projects\Live-CV-on-Arduino\crackers_raw\broken"
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

def serial_readline(obj):
    data = obj.readline()
    return data.decode("utf-8").strip()

port = 'COM4'  # This must be determined from the Arduino app
baudrate = 115200

# Initialize serial port
ser = serial.Serial()
ser.port = port
ser.baudrate = baudrate

ser.open()
ser.reset_input_buffer()

while True:
    data_str = serial_readline(ser)

    if str(data_str) == "<image>":
        w_str = serial_readline(ser)
        h_str = serial_readline(ser)
        w = int(w_str)
        h = int(h_str)
        c = int(3)
        image = np.empty((h, w, c), dtype=np.uint8)

        print("Reading frame:", w, h)
        for y in range(h):
            for x in range(w):
                for d in range(c):
                    data_str = serial_readline(ser)
                    image[y, x, d] = int(data_str)
        data_str = serial_readline(ser)
        if str(data_str) == "</image>":
            print("Captured frame")
            # Display the image using Matplotlib
            plt.imshow(image)
            plt.show()
            # Save the image
            pil_image = Image.fromarray(image)
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = os.path.join(save_dir, f"image_{timestamp}.png")
            pil_image.save(filename)
            print(f"Image saved as {filename}")
        else:
            print("Error capture image")
