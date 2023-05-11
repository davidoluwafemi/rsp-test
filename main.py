import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
servo_pin = 11  # Use the GPIO pin you connected the servo's signal (SIG) pin to

GPIO.setup(servo_pin, GPIO.OUT)
servo = GPIO.PWM(servo_pin, 50)  # 50 Hz frequency
servo.start(0)

def set_angle(angle):
    duty = angle / 18 + 2
    GPIO.output(servo_pin, True)
    servo.ChangeDutyCycle(duty)
    time.sleep(1)
    GPIO.output(servo_pin, False)
    servo.ChangeDutyCycle(0)


set_angle(90)  # Move servo to 90 degrees


servo.stop()
GPIO.cleanup()