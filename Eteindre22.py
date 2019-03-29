import RPi.GPIO as GPIO
import ctypes

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(22, GPIO.OUT)
GPIO.output(22,False)