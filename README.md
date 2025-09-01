# Line-Following Robot with GPS and Anomaly Detection(CNN modal)

This project is an autonomous line-following robot built on the Arduino platform, enhanced with a machine learning module for anomaly detection. The robot follows a black line, and when it stops, it sends its GPS coordinates via SMS. Additionally, it integrates with a custom Convolutional Neural Network (CNN) to detect if the robot has flipped over, which is treated as an anomaly.

## Features

- **Autonomous Line Following**: Uses two IR sensors to accurately track a black line.
- **GPS Location Tracking**: Integrates a NEO-6M GPS module to determine its geographical coordinates.
- **GSM Notifications**: Equipped with a SIM800L/900A GSM module to send SMS alerts.
- **Anomaly Detection**: Utilizes a custom-trained CNN to classify the robot's state as normal (`1`) or flipped (`0` - anomaly) from a video feed.
- **ESP32-CAM Integration**: Includes scripts to stream video from an ESP32-CAM for real-time monitoring and inference.
- **Data Preparation Utilities**: A suite of Python scripts is provided for image processing, data augmentation, and dataset creation.

---

## Part 1: Line-Following Robot

### Hardware Requirements (Robot)

| Component     | Description                                                                          |
| ------------- | ------------------------------------------------------------------------------------ |
| Arduino Board | e.g., Arduino Uno, Nano, or any compatible board                                     |
| Motor Driver  | L298N or a similar dual H-bridge motor driver                                        |
| Robot Chassis | A 2WD chassis with two DC motors and a caster wheel                                  |
| IR Sensors    | Two digital IR proximity sensors                                                     |
| GPS Module    | NEO-6M or compatible GPS receiver                                                    |
| GSM Module    | SIM800L, SIM900A, or similar with a valid SIM card                                   |
| Power Supply  | A suitable battery pack for the Arduino and motors (e.g., 7.4V Li-ion or 9V battery) |
| Jumper Wires  | For making connections                                                               |

### Software Requirements (Robot)

1. **[Arduino IDE](https://www.arduino.cc/en/software)**
2. **Required Libraries:**
   - `TinyGPS++`: For parsing data from the GPS module. You can install this from the Arduino IDE's Library Manager (`Sketch` > `Include Library` > `Manage Libraries...`).
   - `SoftwareSerial`: This library is included with the Arduino IDE by default.

### Wiring and Pinout (Robot)

| Component Pin          | Arduino Pin |
| ---------------------- | ----------- |
| **IR Sensors**   |             |
| Right IR Sensor OUT    | `A0`      |
| Left IR Sensor OUT     | `A1`      |
| **Motor Driver** |             |
| Right Motor Enable     | `10`      |
| Right Motor IN1        | `9`       |
| Right Motor IN2        | `8`       |
| Left Motor Enable      | `5`       |
| Left Motor IN1         | `7`       |
| Left Motor IN2         | `6`       |
| **GPS Module**   |             |
| GPS TX                 | `4`       |
| GPS RX                 | `3`       |
| **GSM Module**   |             |
| GSM TX                 | `11`      |
| GSM RX                 | `12`      |

*Note: Ensure all components share a common ground (GND).*

### Setup and Installation (Robot)

1. **Assemble the Hardware**: Connect all the components according to the wiring diagram above.
2. **Install Libraries**: Open the Arduino IDE and install the `TinyGPS++` library.
3. **Configure the Code**:
   - Open the `mainCodeForCar.ino` file in the Arduino IDE.
   - Modify the `PHONE_NUMBER` constant to the phone number where you want to receive SMS notifications.
4. **Upload the Sketch** to your Arduino board.

---

## Part 2: Anomaly Detection with CNN

The machine learning component uses a custom-trained Convolutional Neural Network (CNN) to perform binary classification. It processes a video feed from the robot to determine if it is in an anomalous state (e.g., flipped over).

### ML Components

- **`Custom-labelled-image-dataset/`**: The dataset containing images of the robot in normal and anomalous (flipped) states, used for training the CNN.
- **`Get_Image_From_ESP.py`**: A Python script to connect to an ESP32-CAM's video stream and display it. This feed is used as input for the model.
- **`Image_Extractor.py`**: A utility to extract frames from video files to help build a dataset.
- **Data Augmentation Scripts**:
  - `AddNoise.py`, `HistogramEQ.py`, `imageCrop.py`, `RotateAndSave.py`: Various scripts to process and augment images to improve model performance.

### Hardware Requirements (ML)

| Component | Description                                |
| --------- | ------------------------------------------ |
| Computer  | A PC or laptop to run the Python scripts   |
| ESP32-CAM | (Optional) For live video streaming        |
| Webcam    | (Optional) For testing with a local camera |

### Software Requirements (ML)

1. **Python 3.x**
2. **Required Libraries:**
   - OpenCV: `pip install opencv-python`
   - NumPy: `pip install numpy`
   - TensorFlow/Keras: `pip install tensorflow`

### Setup and Usage (ML)

1. **Set up the Environment**:

   - Ensure you have Python and the required libraries installed on your computer.
   - Place all files from the `ML-Modals-for-Anomally-detection` directory into a single folder.
2. **Run Live Anomaly Detection**:

   - To use the ESP32-CAM, upload a camera web server sketch to it and connect it to your Wi-Fi.
   - Open `Get_Image_From_ESP.py` and replace the `url` variable with the IP address of your ESP32-CAM.
   - Run the script to view the live feed. A separate script would be needed to load the trained CNN model and perform real-time classification on frames from this stream.
3. **Training the Custom CNN**:

   - **Collect Data**: Use `Image_Extractor.py` or a webcam to gather images of the robot in two states: normal (upright) and anomalous (flipped).
   - **Organize and Label**: Separate the images into `0` (anomaly) and `1` (normal) folders.
   - **Augment Data**: Use the provided scripts (`AddNoise.py`, `RotateAndSave.py`, etc.) to increase the size and diversity of your dataset.
   - **Train**: Use a framework like TensorFlow/Keras to build and train a CNN classifier on your custom dataset.

## Future Scope

The project was initially planned to incorporate a **YOLOv3 object detection model** for more complex anomaly detection tasks. The model weights (`yolov3.weights`) and configuration (`yolov3.cfg`) are included in the repository for future development. This would allow the robot to identify a wider range of objects and scenarios beyond its orientation, such as detecting obstacles or specific items in its path.

## Troubleshooting

- **Robot not moving correctly**: Check motor wiring, power supply, and IR sensor calibration.
- **No GPS data**: Ensure the GPS module has a clear view of the sky.
- **SMS not sending**: Verify the SIM card is active and the GSM module is registered to the network.
- **Python script errors**: Make sure all required libraries are installed and that the ESP32-CAM is on the same Wi-Fi network.
