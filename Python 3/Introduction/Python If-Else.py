#!/bin/python3

import math
import os
import random
import re
import sys

# Created BY: Alpha

if __name__ == '__main__':
    n = int(input().strip())
    if n >= 1 and n <= 100:
        if n%2 != 0:
            print("Weird")
        elif n%2 == 0 and n in range(2,6):
            print("Not Weird")
        elif n%2 ==0 and n in range(6,21):
            print("Weird")
        else:
            print("Not Weird")
    else:
        print("Invalid Answer")