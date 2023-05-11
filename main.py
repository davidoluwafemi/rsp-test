import RPi.GPIO as GPIO
import time

# Set GPIO numbering mode and configure GPIO pins
GPIO.setmode(GPIO.BCM)
STEP_PIN = 17
DIR_PIN = 27
SERVO_PIN = 18

GPIO.setup(STEP_PIN, GPIO.OUT)
GPIO.setup(DIR_PIN, GPIO.OUT)
GPIO.setup(SERVO_PIN, GPIO.OUT)

# Define servo control functions
def set_angle(angle):
    duty = angle / 18 + 2
    GPIO.output(SERVO_PIN, True)
    p = GPIO.PWM(SERVO_PIN, 50)
    p.start(0)
    p.ChangeDutyCycle(duty)
    time.sleep(0.5)
    GPIO.output(SERVO_PIN, False)
    p.stop()

# Define motor control functions
def move_motor(steps, direction):
    GPIO.output(DIR_PIN, direction)
    for _ in range(steps):
        GPIO.output(STEP_PIN, GPIO.HIGH)
        time.sleep(0.001)  # Adjust delay as per your motor requirements
        GPIO.output(STEP_PIN, GPIO.LOW)
        time.sleep(0.001)  # Adjust delay as per your motor requirements

# Usage examples
move_motor(200, GPIO.HIGH)  # Move motor 200 steps in one direction
set_angle(90)  # Set servo angle to 90 degrees

# Clean up GPIO pins
GPIO.cleanup()