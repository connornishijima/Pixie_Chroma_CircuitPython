# Pixie Chroma for CircuitPython

This repository is an early work-in-progress of a CircuitPython port of my Pixie Chroma library for Arduino.

This isn't even set up in a way that you can traditionally install it yet, it's just the contents of my CIRCUITPY drive on an RP2040, which is the only microcontroller I've tried this with.

`code.py` is the user code, and the `lib/pixie_chroma.py` file contains the internals.

(***code.py*** also contains more notes about how things work!)

No support yet for shortcodes or anything but basic color, but the printing functions work super smoothly! I get 45 FPS on a 6-character display setup.