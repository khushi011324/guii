import RPi.GPIO as GPIO
import tkinter as tk

# GPIO setup
GPIO.setmode(GPIO.BCM)
LED_PIN = 18  # LED connected to GPIO 18
GPIO.setup(LED_PIN, GPIO.OUT)

# Create PWM instance for LED
pwm_led = GPIO.PWM(LED_PIN, 100)  # 100Hz frequency
pwm_led.start(0)  # Start with 0% duty cycle (LED OFF)

# Function to change brightness
def change_brightness(value):
    duty_cycle = int(value)
    pwm_led.ChangeDutyCycle(duty_cycle)

# GUI setup
root = tk.Tk()
root.title("LED Brightness Control")

tk.Label(root, text="Adjust LED Brightness").pack()

# Create slider to control brightness
slider = tk.Scale(root, from_=0, to=100, orient="horizontal", command=change_brightness)
slider.pack()

# Function to clean up GPIO on exit
def close_app():
    pwm_led.stop()
    GPIO.cleanup()
    root.destroy()

root.protocol("WM_DELETE_WINDOW", close_app)
root.mainloop()
