import RPi.GPIO as GPIO
import time

led = 18
push_button = 16

GPIO.setmode(GPIO.BOARD)
GPIO.setup(led, GPIO.OUT)
GPIO.setup(push_button, GPIO.IN)

for i in range(10):
    GPIO.output(led, GPIO.HIGH)
    time.sleep(0.2)
    GPIO.output(led, GPIO.LOW)
    time.sleep(0.2)
    print('push_button_status = ', GPIO.input(push_button))

GPIO.cleanup()