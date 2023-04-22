import board
import neopixel
import adafruit_fancyled.adafruit_fancyled as fancy
import os

class PixieChroma:
    def __init__(self, pin, num_pixies, brightness=1.0):
        self.pixels = neopixel.NeoPixel(pin, num_pixies*70, auto_write=False, brightness=brightness)
        self.print_color = fancy.CRGB(20, 255, 0)
        self.print_offset = 0
        
        self.font_file = open("/lib/pixie_chroma/font.bin", "rb")
        self.font_data = self.font_file.read()
        
        self.XY_MAP = (    
            (0,  1,  2,  3,  4 ),
            (5,  6,  7,  8,  9 ),
            (10, 11, 12, 13, 14),
            (15, 16, 17, 18, 19),
            (20, 21, 22, 23, 24),
            (25, 26, 27, 28, 29),
            (30, 31, 32, 33, 34),
        )
         
    def print(self,input_string):
        input_string = str(input_string)
        
        length = len(input_string)
        
        temp_col = (
            255 * self.print_color[0],
            255 * self.print_color[1],
            255 * self.print_color[2],
        )
        
        for i in range(length):
            char = input_string[i];
            int_val = ord(char)-32
            
            start_col = 5*int_val
            end_col = start_col + 5
            cols = self.font_data[start_col : end_col]
                
            for x in range(5):
                rows = self.COL_TO_ROWS( cols[x] )
                
                XY_ORIG = self.XY_TO_1D(self.print_offset+x, 0)
                
                if rows[0] > 0:
                    self.pixels[ XY_ORIG + 0  ] = (temp_col[0]*rows[0], temp_col[1]*rows[0], temp_col[2]*rows[0]);
                if rows[1] > 0:
                    self.pixels[ XY_ORIG + 5  ] = (temp_col[0]*rows[1], temp_col[1]*rows[1], temp_col[2]*rows[1]);
                if rows[2] > 0:
                    self.pixels[ XY_ORIG + 10 ] = (temp_col[0]*rows[2], temp_col[1]*rows[2], temp_col[2]*rows[2]);
                if rows[3] > 0:
                    self.pixels[ XY_ORIG + 15 ] = (temp_col[0]*rows[3], temp_col[1]*rows[3], temp_col[2]*rows[3]);
                if rows[4] > 0:
                    self.pixels[ XY_ORIG + 20 ] = (temp_col[0]*rows[4], temp_col[1]*rows[4], temp_col[2]*rows[4]);
                if rows[5] > 0:
                    self.pixels[ XY_ORIG + 25 ] = (temp_col[0]*rows[5], temp_col[1]*rows[5], temp_col[2]*rows[5]);
                if rows[6] > 0:
                    self.pixels[ XY_ORIG + 30 ] = (temp_col[0]*rows[6], temp_col[1]*rows[6], temp_col[2]*rows[6]);
                
            self.print_offset += 5;

    def show(self):
        self.pixels.show()
            
    def clear(self):
        self.pixels.fill((0,0,0))
        self.print_offset = 0
        
    def set_brightness(self, bright_val):
        self.pixels.brightness = bright_val*bright_val
        
    def set_col_rgb(self, r, g, b):
        self.print_color = fancy.CRGB(r,g,b)
    
    def set_col_hsv(self, h, s, v):
        self.print_color = fancy.CRGB(fancy.CHSV(h,s,v))
    
    def set_cursor(self, position):
        self.print_offset = position*5
            
    # INTERNAL FUNCTIONS -----------------------------------------------

    def XY_TO_1D(self, x, y):
        index_shift = 0
        
        while x >= 5:
            x -= 5
            index_shift += 35
    
        index = self.XY_MAP[y][x] + index_shift;

        return index


    def COL_TO_ROWS(self, col):
        return [
            (col >> 0) & 1,
            (col >> 1) & 1,
            (col >> 2) & 1,
            (col >> 3) & 1,
            (col >> 4) & 1,
            (col >> 5) & 1,
            (col >> 6) & 1
        ]