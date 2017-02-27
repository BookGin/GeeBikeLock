#!/usr/bin/env python3
import sys
import math
import os
while True:
    pipe = open('./backpipe', 'r')
    os.system('echo -n ' + str(pipe.read(1)) + ' > /dev/ttyACM0')
