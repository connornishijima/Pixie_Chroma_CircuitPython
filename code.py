#---------------------------------------------#
#
#   Pixie Chroma CircuitPython Library Demo
#   by @lixielabs (4/21/23)
#
#   This demo shows how to configure a chain of
#   Pixie Chromas to self-test the average FPS
#   that the microcontroller is capable of. (It
#   displays the benchmark in two colors and the
#   results in purple.)
#
#   I've got 10+ years of experience in C/C++
#   firmware development, but I'm completely
#   new to the much higher-level CircuitPython
#   scene.
#
#   The pixie_chroma module uses some tricks
#   that feel really inefficient and strange
#   in order to access the 475-byte ASCII font
#   stored in font.bin, because I haven't
#   found a working method to store it all in
#   RAM. Any attempts to store it as a tuple
#   or array.array('B' [data]) still cause a
#   RuntimeError: pystack exhausted. Am I
#   crazy or does the RP2040 running
#   CircuitPython not have a lot of memory to
#   go around? I'm still used to C where even
#   an ATMEGA328 could store 2K bytes in memory.
#
#   My equivalent to PROGMEM that I'm using is
#   leaving the font.bin file open at all times
#   and running seek()/read() calls on it at
#   runtime to emulate the feel of an Arduino-
#   style C array stored in flash.
#
#   Also, this is only developed and tested on
#   a Raspberry Pi Pico thus far, you likely
#   need to change how your GPIO pin is set up
#   on other boards.
#
#---------------------------------------------#


import board
import time

import pixie_chroma # Code in /lib/pixie_chroma.py

DATA_PIN   = board.GP15 # GPIO pin to use
NUM_PIXIES = 3          # Number of Pixie PCBs
BRIGHTNESS = 0.05       # 0.0 - 1.0

pix = pixie_chroma.PixieChroma(DATA_PIN, NUM_PIXIES, BRIGHTNESS)

while True:
    t_end = time.monotonic_ns() + 10000000000 # 10 seconds from now

    num = 0 # Start count from 0

    # How many times can we print num's value in 10 seconds?
    while time.monotonic_ns() <= t_end:
        pix.clear() # Clear the display buffer
        
        pix.set_col_hsv(10,255,255)  # Set orange color
        pix.print(num)               # Print the value to the display buffer
        
        pix.set_cursor(3)            # Next print call starts from display at index 3

        pix.set_col_hsv(num,255,255) # Set cycling color
        pix.print(num)               # Print the value to the display buffer
        
        pix.show() # Send the display buffer to the LEDs
        num += 1   # Count up

    FPS = num / 10.0 # Divide by 10 seconds
    
    pix.set_col_hsv(180,255,255) # Go purple
    
    # Write the measured FPS to the displays
    pix.clear()
    pix.print(FPS)
    pix.show()
    
    # Wait 3 seconds before repeating forever
    time.sleep(3)