import RPi.GPIO as io
import pynput

from pynput import keyboard

io.setmode(io.BCM)

motor1_in1_pin = 17
motor1_in2_pin = 22
io.setup(motor1_in1_pin, io.OUT)
io.setup(motor1_in2_pin, io.OUT)
io.setup(12, io.OUT)
io.setup(13, io.OUT)
motor1 = io.PWM(12,100)
motor1.start(0)
motor1.ChangeDutyCycle(0)

motor2_in1_pin = 23
motor2_in2_pin = 24
io.setup(motor2_in1_pin, io.OUT)
io.setup(motor2_in2_pin, io.OUT)
motor2 = io.PWM(13,100)
motor2.start(0)
motor2.ChangeDutyCycle(0)

def motor1_forward():
    io.output(motor1_in1_pin, False)
    io.output(motor1_in2_pin, True)

def motor1_reverse():
    io.output(motor1_in1_pin, True)
    io.output(motor1_in2_pin, False)

def motor2_forward():
    io.output(motor2_in1_pin, True)
    io.output(motor2_in2_pin, False)

def motor2_reverse():
    io.output(motor2_in1_pin, False)
    io.output(motor2_in2_pin, True)
    
def stop_all_motors():
    io.output(motor1_in1_pin, False)
    io.output(motor1_in2_pin, False)
    io.output(motor2_in1_pin, False)
    io.output(motor2_in2_pin, False)


def on_press(key):
    try:
        if key.char == ('w'):
            motor1_forward()
            motor2_forward()
            motor1.ChangeDutyCycle(99)
            motor2.ChangeDutyCycle(99)

        elif key.char == ('s'):
            motor1_reverse()
            motor2_reverse()
            motor1.ChangeDutyCycle(99)
            motor2.ChangeDutyCycle(99)

        elif key.char == ('a'):
            motor2_forward()

        elif key.char == ('d'):
            motor1_forward()
            
        else:
            print('Please press a valid key or shut down with X/ESC key!')
            
    except AttributeError:
        print('Key {0} pressed'.format(key))
        print('Unexpected error! Shut down!')
        stop_all_motors()
        
def on_release(key):
    print('{0} released'.format(key))
    stop_all_motors()
    
    if key == keyboard.Key.esc or key.char == ('x'):
        return False

print("W: forward")
print("S:  reverse")
print("A:  left")
print("D:  right")
print("X/ESC:  shut down")

with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
        listener.join()

io.cleanup()
