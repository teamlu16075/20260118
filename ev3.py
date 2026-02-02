#!/usr/bin/env pybricks-micropython
"""EV3 helpers: imports, device instances and behavior functions.

This module centralizes hardware imports and creates the EV3 objects
so `main.py` can simply import them.
"""

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# Create hardware objects
ev3 = EV3Brick()
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
left_light = ColorSensor(Port.S2)
right_light = ColorSensor(Port.S3)
# touch = TouchSensor(Port.S4)


def move_basic(left_speed, right_speed):
    """Drive using module-level motor objects.

    left_speed and right_speed are duty-cycle percentages.
    """
    left_motor.dc(left_speed)
    right_motor.dc(right_speed)


def two_light_goline(type_val,left_val, right_val, time_limit=1000, angle_limit=2000):
    """Follow line using module-level light sensors and motors.

    This loops indefinitely; consider adding a stop condition in `main.py`.
    """
    while True:
        if left_light.reflection() > left_val:
            if right_light.reflection() > right_val:
                move_basic(60, 60)
            else:
                move_basic(60, 20)
        else:
            if right_light.reflection() > right_val:
                move_basic(20, 60)
            else:
                move_basic(60, 60)
                if type_val==5:
                    break
