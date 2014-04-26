#!/usr/bin/python

from Adafruit_I2C import Adafruit_I2C

class Adafruit_L3GD20(Adafruit_I2C):
    L3GD20_ADDRESS      = 0x6B
    L3GD20_POLL_TIMEOUT = 100
    L3GD20_ID           = 0b11010100

    GYRO_SENSITIVITY_250DPS  = 0.00875
    GYRO_SENSITIVITY_500DPS  = 0.00175
    GYRO_SENSITIVITY_2000DPS = 0.070

    GYRO_REGISTER_WHO_AM_I = 0x0F
    GYRO_REGISTER

    def __init__(self, busnum=-1, debug=False):
        self.gyro = Adafruit_I2C(self.
