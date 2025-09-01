// Define the pins for the ultrasonic sensor
const int TRIG_PIN = A3; // Trigger pin
const int ECHO_PIN = A2; // Echo pin

void setup() {
  // Start the Serial communication
  Serial.begin(9600);
  
  // Set the TRIG_PIN as an OUTPUT
  pinMode(TRIG_PIN, OUTPUT);
  
  // Set the ECHO_PIN as an INPUT
  pinMode(ECHO_PIN, INPUT);
}

void loop() {
  // Variable to store the duration and distance
  long duration;
  float distance;

  // Clear the TRIG_PIN
  digitalWrite(TRIG_PIN, LOW);
  delayMicroseconds(2);

  // Set the TRIG_PIN HIGH for 10 microseconds
  digitalWrite(TRIG_PIN, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG_PIN, LOW);

  // Read the ECHO_PIN, duration of the pulse
  duration = pulseIn(ECHO_PIN, HIGH);

  // Calculate the distance (in cm)
  distance = duration * 0.034 / 2;

  // Print the distance to the Serial Monitor
  Serial.print("Distance: ");
  Serial.print(distance);
  Serial.println(" cm");

  // Wait for a short period before the next measurement
  delay(500);
}