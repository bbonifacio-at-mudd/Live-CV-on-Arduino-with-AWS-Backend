# Welcome to the Live Computer Vision on Arduino with an AWS Backend Project! 

The title of this project succinctly explains what I did in this project, and I also provide a full System Diagram below to help explain. I completed this project during my winter break from December 2023 - January 2024 with the purpose of gaining more experience with live ML deployment and cloud engineering. 

 ![image](https://github.com/bbonifacio-at-mudd/Live-CV-on-Arduino-with-AWS-Backend/assets/114462423/76d28254-9cc4-4051-95af-ab892c1134a0)

In this project, I connected an OV7670 camera to an Arduino Nano 33 BLE Sense. Then, I created a cloud-based backend in AWS, with the primary components being S3 for data storage and Sagemaker for MLOps. Using this, I trained a MobileNetv2 model in Sagemaker, compressed its size to 0.6 MB using Tensorflow Lite, and then deployed it on the Arduino in order to capture and label images live. I used S3 to maintain model version control by storing my models on it.

The purpose of the model was to classify Saltine crackers imaged under it as either broken or whole, and you can see some examples of whole/broken Saltines below that were imaged with the camera: 

![image](https://github.com/bbonifacio-at-mudd/Live-CV-on-Arduino-with-AWS-Backend/assets/114462423/0943859e-f442-4ad6-ac93-a91ea201bfc6)


Below is a picture of my camera setup with a Saltine and also a hamster: 

![image](https://github.com/bbonifacio-at-mudd/Live-CV-on-Arduino-with-AWS-Backend/assets/114462423/8f981642-f6b9-4890-9e40-a7b4a1735e5a)

