#!/usr/bin/python

# Left motor 0
# Right motor 1 

from PCA9685 import PCA9685
import time

Dir = [
    'forward',
    'backward',
]

# forward := IN1 = 1 IN2 = 0 
# backward := IN1 = 0 IN2 = 1
# left := m0 forward + m1 backward
# right := m0 backward + m1 forward

pwm = PCA9685(0x40, debug=False)
pwm.setPWMFreq(50)

class MotorDriver():
    def __init__(self, speed=0):
        self.PWMA = 0
        self.AIN1 = 1
        self.AIN2 = 2
        self.PWMB = 5
        self.BIN1 = 3
        self.BIN2 = 4
        self.speed = speed
    
    def set_speed(self, new_speed):
        self.speed = new_speed

    def MotorRun(self, motor, index):
        if self.speed > 100:
            return
        if(motor == 0):
            pwm.setDutycycle(self.PWMA, self.speed)
            if(index == Dir[0]):
                pwm.setLevel(self.AIN1, 0)
                pwm.setLevel(self.AIN2, 1)
            else:
                pwm.setLevel(self.AIN1, 1)
                pwm.setLevel(self.AIN2, 0)
        else:
            pwm.setDutycycle(self.PWMB, self.speed)
            if(index == Dir[0]):
                pwm.setLevel(self.BIN1, 0)
                pwm.setLevel(self.BIN2, 1)
            else:
                pwm.setLevel(self.BIN1, 1)
                pwm.setLevel(self.BIN2, 0)

    def MotorStop(self, motor):
        if (motor == 0):
            pwm.setDutycycle(self.PWMA, 0)
        else:
            pwm.setDutycycle(self.PWMB, 0)


