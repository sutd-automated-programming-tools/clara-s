"""
@author: methylDragon

                       .     .
                    .  |\-^-/|  .    
                   /| } O.=.O { |\  
                  /´ \ \_ ~ _/ / `\
                /´ |  \-/ ~ \-/  | `\
                |   |  /\\ //\  |   | 
                 \|\|\/-""-""-\/|/|/
                         ______/ /
                         '------'
           _   _        _  ___                         
 _ __  ___| |_| |_ _  _| ||   \ _ _ __ _ __ _ ___ _ _  
| '  \/ -_)  _| ' \ || | || |) | '_/ _` / _` / _ \ ' \ 
|_|_|_\___|\__|_||_\_, |_||___/|_| \__,_\__, \___/_||_|
                   |__/                 |___/          
-------------------------------------------------------
               github.com/methylDragon


2018 MIDTERMS!!!!!

"""

# MID-TERM EXAM: QUESTION 3

import math

def area_square(s):
    return s ** 2

def vol_frustum(top_area, bottom_area, height):
    return height / 3 * (top_area + bottom_area + math.sqrt(top_area * bottom_area))

def get_volume(s1, s2, height):
    top_area = area_square(s1)
    bottom_area = area_square(s2)
    
    return vol_frustum(top_area, bottom_area, height)