#include <TinyGPS++.h>
#include <SoftwareSerial.h>

// Pin Definitions
const int IR_SENSOR_RIGHT = A0;
const int IR_SENSOR_LEFT = A1;

// Motor Configuration
const int MOTOR_SPEED = 180;
const int enableRightMotor = 10;
const int rightMotorPin1 = 9;
const int rightMotorPin2 = 8;
const int enableLeftMotor = 5;
const int leftMotorPin1 = 7;
const int leftMotorPin2 = 6;

// GPS Module (using SoftwareSerial)
const int GPS_RX_PIN = 4;
const int GPS_TX_PIN = 3;
SoftwareSerial gpsSerial(GPS_RX_PIN, GPS_TX_PIN);
TinyGPSPlus gps;

// GSM Module (using SoftwareSerial)
const int GSM_RX_PIN = 11;
const int GSM_TX_PIN = 12;
SoftwareSerial gsmSerial(GSM_RX_PIN, GSM_TX_PIN);
const char* PHONE_NUMBER = "+918135801656";

// State variable to prevent sending multiple messages
bool messageSent = false;

// --- Function Prototypes ---
void updateSerial();
void rotateMotor(int rightMotorSpeed, int leftMotorSpeed);
void sendMessage(const String& message);
void stopAndSendLocation();
void followLine();
void updateGPS();
void displayGPSInfo();
void setupSerialComm();
void setupGPSModule();
void setupGSMModule();
void setupMotorsAndSensors();

// --- Main Setup ---
void setup() {
  setupSerialComm();
  setupGPSModule();
  setupGSMModule();
  setupMotorsAndSensors();
  Serial.println("Setup complete. Starting robot.");
}

// --- Main Loop ---
void loop() {
  updateGPS();
  followLine();
  displayGPSInfo(); // For debugging GPS data
}

// --- Setup Functions ---
void setupSerialComm() {
  Serial.begin(9600);
  Serial.println("Serial communication started.");
}

void setupGPSModule() {
  gpsSerial.begin(9600);
  Serial.println("GPS module initialized.");
}

void setupGSMModule() {
  gsmSerial.begin(9600);
  Serial.println("Initializing GSM module...");
  delay(1000);

  gsmSerial.println("AT");
  updateSerial();
  gsmSerial.println("AT+CMGF=1"); // Set SMS to text mode
  updateSerial();
  Serial.println("GSM module ready.");
}

void setupMotorsAndSensors() {
  pinMode(enableRightMotor, OUTPUT);
  pinMode(rightMotorPin1, OUTPUT);
  pinMode(rightMotorPin2, OUTPUT);
  pinMode(enableLeftMotor, OUTPUT);
  pinMode(leftMotorPin1, OUTPUT);
  pinMode(leftMotorPin2, OUTPUT);

  pinMode(IR_SENSOR_RIGHT, INPUT);
  pinMode(IR_SENSOR_LEFT, INPUT);

  // Increasing PWM frequency allows for smoother motor control at lower speeds.
  // Note: Pin 5 (Timer0) and Pin 10 (Timer1) are on different timers,
  // resulting in different PWM frequencies, but both are higher than default.
  TCCR0B = (TCCR0B & 0b11111000) | 0b00000010; // Set PWM frequency for pin 5 to ~7.8 kHz
  TCCR1B = (TCCR1B & 0b11111000) | 0b00000010; // Set PWM frequency for pin 10 to ~3.9 kHz
  
  Serial.println("Motors and sensors initialized.");
  rotateMotor(0, 0); // Start with motors stopped
}


// --- Core Logic ---
void updateGPS() {
  while (gpsSerial.available() > 0) {
    gps.encode(gpsSerial.read());
  }
}

void followLine() {
  int rightIRSensorValue = digitalRead(IR_SENSOR_RIGHT);
  int leftIRSensorValue = digitalRead(IR_SENSOR_LEFT);

  // Assuming HIGH means the sensor is on the black line
  if (rightIRSensorValue == LOW && leftIRSensorValue == LOW) {
    rotateMotor(MOTOR_SPEED, MOTOR_SPEED); // Go straight
    messageSent = false;
  } else if (rightIRSensorValue == HIGH && leftIRSensorValue == LOW) {
    rotateMotor(-MOTOR_SPEED, MOTOR_SPEED); // Turn right
    messageSent = false;
  } else if (rightIRSensorValue == LOW && leftIRSensorValue == HIGH) {
    rotateMotor(MOTOR_SPEED, -MOTOR_SPEED); // Turn left
    messageSent = false;
  } else {
    stopAndSendLocation(); // Both sensors on black: stop
  }
}

void stopAndSendLocation() {
  rotateMotor(0, 0);
  if (!messageSent) {
    String message = "Car stopped. ";
    if (gps.location.isValid()) {
      message += "GPS: " + String(gps.location.lat(), 6) + "," + String(gps.location.lng(), 6);
    } else {
      message += "GPS location not available.";
    }
    sendMessage(message);
    messageSent = true;
  }
}

// --- Helper Functions ---
void sendMessage(const String& message) {
  Serial.println("Sending SMS...");
  gsmSerial.print("AT+CMGS=\"");
  gsmSerial.print(PHONE_NUMBER);
  gsmSerial.println("\"");
  updateSerial();
  gsmSerial.print(message);
  updateSerial();
  gsmSerial.write(26); // ASCII for Ctrl+Z to send the message
}

void rotateMotor(int rightMotorSpeed, int leftMotorSpeed) {
  // Right Motor
  if (rightMotorSpeed < 0) {
    digitalWrite(rightMotorPin1, LOW);
    digitalWrite(rightMotorPin2, HIGH);
  } else if (rightMotorSpeed > 0) {
    digitalWrite(rightMotorPin1, HIGH);
    digitalWrite(rightMotorPin2, LOW);
  } else {
    digitalWrite(rightMotorPin1, LOW);
    digitalWrite(rightMotorPin2, LOW);
  }

  // Left Motor
  if (leftMotorSpeed < 0) {
    digitalWrite(leftMotorPin1, LOW);
    digitalWrite(leftMotorPin2, HIGH);
  } else if (leftMotorSpeed > 0) {
    digitalWrite(leftMotorPin1, HIGH);
    digitalWrite(leftMotorPin2, LOW);
  } else {
    digitalWrite(leftMotorPin1, LOW);
    digitalWrite(leftMotorPin2, LOW);
  }
  analogWrite(enableRightMotor, abs(rightMotorSpeed));
  analogWrite(enableLeftMotor, abs(leftMotorSpeed));
}

void displayGPSInfo() {
  if (gps.location.isUpdated()) {
    Serial.print("Lat: "); Serial.print(gps.location.lat(), 6);
    Serial.print(" | Lng: "); Serial.print(gps.location.lng(), 6);
    Serial.print(" | Sats: "); Serial.println(gps.satellites.value());
  }
}

void updateSerial() {
  delay(500);
  while (Serial.available()) {
    gsmSerial.write(Serial.read());
  }
  while (gsmSerial.available()) {
    Serial.write(gsmSerial.read());
  }
}