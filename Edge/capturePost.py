import numpy as np
import serial
from PIL import Image
import requests
import json
import base64
import os
from datetime import datetime

def serial_readline(ser_obj):
    return ser_obj.readline().decode("utf-8").strip()

def save_image(image_array, label):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"image_{timestamp}_{label}.png"
    Image.fromarray(image_array).save(filename)
    return filename

def upload_image(image_filename, label):
    api_invoke_url = #Removed the link for github upload :)

    # Ensure the file is a PNG
    if not image_filename.lower().endswith('.png'):
        raise ValueError("The file is not a PNG image.")

    metadata = {'name': os.path.basename(image_filename), 'label': label, 'Content-Type': 'image/png'}

    with open(image_filename, 'rb') as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')

    data = {
        'image_data': encoded_string,
        'metadata': metadata
    }

    response = requests.post(api_invoke_url, data=json.dumps(data))
    return response.text, response.status_code

# Arduino communication setup
port = 'COM4'  # This must be determined from the Arduino IDE
baudrate = 115200
ser = serial.Serial(port, baudrate)
ser.reset_input_buffer()

while True:
    data_str = serial_readline(ser)

    if data_str == "<image>":
        w = int(serial_readline(ser))
        h = int(serial_readline(ser))
        image = np.empty((h, w, 3), dtype=np.uint8)

        for y in range(h):
            for x in range(w):
                rgb_str = serial_readline(ser).split()
                image[y, x] = [int(val) for val in rgb_str]

        if serial_readline(ser) == "</image>":
            label_str = serial_readline(ser)
            if label_str.startswith("<label>"):
                label = label_str[len("<label>"):].strip()
                if serial_readline(ser) == "</label>":
                    # Save and upload the image
                    image_filename = save_image(image, label)
                    response_text, status_code = upload_image(image_filename, label)
                    print(f"Uploaded {image_filename}, Response: {response_text}, Status Code: {status_code}")
                else:
                    print("Error: Label end tag not found")
            else:
                print("Error: Label start tag not found")
        else:
            print("Error: Image end tag not found")
