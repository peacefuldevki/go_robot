import RPi.GPIO as gpio
import time
from RpiMotorLib import rpi_dc_lib


def init():
    gpio.setmode(gpio.BCM)
    gpio.setup(17, gpio.OUT) 
    gpio.setup(22, gpio.OUT) 
    gpio.setup(23, gpio.OUT)
    gpio.setup(24, gpio.OUT)
    gpio.setup(12, gpio.OUT)
    gpio.setup(13, gpio.OUT)



def forward(sec):
    init()
    pwm17 = gpio.PWM(12,100)
    pwm22 = gpio.PWM(13,100)
    t=40
    pwm17.start(t)
    pwm22.start(t)
    
    gpio.output(17, False)
    gpio.output(22, True)
    gpio.output(23, True)
    gpio.output(24, False)

    
    time.sleep(sec)
    pwm17.stop(t)
    pwm22.stop(t)
    gpio.cleanup()

def forward_faster(sec):
    init()
    pwm17 = gpio.PWM(12,100)
    pwm22 = gpio.PWM(13,100)
    t=75
    pwm17.start(t)
    pwm22.start(t)
    
    gpio.output(17, False)
    gpio.output(22, True)
    gpio.output(23, True)
    gpio.output(24, False)

    
    time.sleep(sec)
    pwm17.stop(t)
    pwm22.stop(t)
    gpio.cleanup()

def forward_fastest(sec):
    init()
    pwm17 = gpio.PWM(12,100)
    pwm22 = gpio.PWM(13,100)
    t=100
    pwm17.start(t)
    pwm22.start(t)
    
    gpio.output(17, False)
    gpio.output(22, True)
    gpio.output(23, True)
    gpio.output(24, False)

    
    time.sleep(sec)
    pwm17.stop(t)
    pwm22.stop(t)
    gpio.cleanup()
    
def reverse(sec):
    init()
    pwm17 = gpio.PWM(12,100)
    pwm22 = gpio.PWM(13,100)
    t=100
    pwm17.start(t)
    pwm22.start(t)
    
    gpio.output(17, True)
    gpio.output(22, False)
    gpio.output(23, False)
    gpio.output(24, True)
    time.sleep(sec)
    gpio.cleanup()
    

def left_turn(sec):
    init()
    
    pwm17 = gpio.PWM(12,100)
    pwm22 = gpio.PWM(13,100)
    t=100
    pwm17.start(t)
    pwm22.start(t)
    
    gpio.output(17, True)
    gpio.output(22, False)
    gpio.output(23, True)
    gpio.output(24, False)
    time.sleep(sec)
    gpio.cleanup()
    
def right_turn(sec):
    init()
    
    pwm17 = gpio.PWM(12,100)
    pwm22 = gpio.PWM(13,100)
    t=100
    pwm17.start(t)
    pwm22.start(t)
    
    gpio.output(17, False)
    gpio.output(22, True)
    gpio.output(23, False)
    gpio.output(24, True)
    time.sleep(sec)
    gpio.cleanup()  

    
print("Forward for 2 seconds")
forward(2)
#right_turn(1)

#print("Pause for 2 seconds")
#time.sleep(2)

#print("reverse for 2 seconds")
# reverse(2)

#print("Motor stopped")
#time.sleep(1)

