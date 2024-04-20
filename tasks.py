# Among Us Auto Task
# JTEE3D 2024

import os
import subprocess
import sys
import psutil
import keyboard
import pyautogui
import pygetwindow
import pyscreeze
import time
import math

# Set delay between pyautogui actions
pyautogui.PAUSE = 0.01

# Clear the console
os.system('cls')

def keyboard_hotkey():
    # Get the current cursor position
    cursor_x, cursor_y = pyautogui.position()
        
    # Calculate the cursor position relative to the center
    relative_x = cursor_x - center_x
    relative_y = cursor_y - center_y
    #print(f"Cursor position relative to center: ({relative_x}, {relative_y})")
        
    pixel_colour = pyscreeze.pixel(cursor_x, cursor_y)

    #print(f"(({relative_x}, {relative_y}),", pixel_colour, ")")
    
    # Wait for task animation
    time.sleep(0.5)    
    
    for i in range(0, len(pixel_array), 2):
        function = pixel_array[i]
        conditions = pixel_array[i + 1]
        conditions_met = True
        
        for coord, colour in conditions:  
            if not check_pixel_colour(coord, colour, center_x, center_y):
                conditions_met = False
                break 
        if conditions_met:
            function()

# Check if Among Us.exe is running
def is_among_us_running():
    for proc in psutil.process_iter(['name']):
        if proc.info['name'] == 'Among Us.exe':
            return True
    return False

def check_pixel_colour(coord, colour, center_x, center_y, tolerance=0):
    # Calculate the absolute coordinates based on the relative coordinates and center of the window
    absolute_x = center_x + coord[0]
    absolute_y = center_y + coord[1]
    
    # Get the pixel colour at the calculated absolute coordinates
    pixel_colour = pyscreeze.pixel(absolute_x, absolute_y)
    
    # Check if the pixel colour is within the tolerance range of the given colour
    if all(abs(pixel_colour[i] - colour[i]) <= tolerance for i in range(3)):
        return True
    else:
        return False

def in_map():
    print("In map")
    
def next_to_task():
    print("Next to task")
    
def admin_swipe_card():
    print("Admin: Swipe Card")
    pyautogui.moveTo(center_x - 190, center_y + 281, duration=0)
    pyautogui.click()
    time.sleep(0.5)
    pyautogui.moveTo(center_x - 403, center_y - 103, duration=0)
    pyautogui.mouseDown();
    pyautogui.move(900, 0, 1.5)
    time.sleep(0.1)
    pyautogui.mouseUp();
    
def divert_power():
    print("Electrical: Divert Power")
    
    if check_pixel_colour((-308, 242), (255, 98, 0), center_x, center_y):
        pyautogui.moveTo(center_x - 309, center_y + 242, duration=0) 
        pyautogui.mouseDown();
        pyautogui.move(0, -150, 0.2)
        pyautogui.mouseUp();
    
    if check_pixel_colour((-213, 242), (255, 98, 0), center_x, center_y):
        pyautogui.moveTo(center_x - 213 , center_y + 242, duration=0) 
        pyautogui.mouseDown();
        pyautogui.move(0, -150, 0.2)
        pyautogui.mouseUp();
        
    if check_pixel_colour((-116, 242), (255, 98, 0), center_x, center_y):
        pyautogui.moveTo(center_x - 116 , center_y + 242, duration=0) 
        pyautogui.mouseDown();
        pyautogui.move(0, -150, 0.2)
        pyautogui.mouseUp();
        
    if check_pixel_colour((-17, 242), (255, 98, 0), center_x, center_y):
        pyautogui.moveTo(center_x - 17  , center_y + 242, duration=0) 
        pyautogui.mouseDown();
        pyautogui.move(0, -150, 0.2)
        pyautogui.mouseUp();
        
    if check_pixel_colour((79, 242), (255, 98, 0), center_x, center_y):
        pyautogui.moveTo(center_x + 79 , center_y + 242, duration=0) 
        pyautogui.mouseDown();
        pyautogui.move(0, -150, 0.2)
        pyautogui.mouseUp();
        
    if check_pixel_colour((172, 242), (255, 98, 0), center_x, center_y):
        pyautogui.moveTo(center_x + 172 , center_y + 242, duration=0) 
        pyautogui.mouseDown();
        pyautogui.move(0, -150, 0.2)
        pyautogui.mouseUp();
        
    if check_pixel_colour((269, 242), (255, 98, 0), center_x, center_y):
        pyautogui.moveTo(center_x + 269 , center_y + 242, duration=0) 
        pyautogui.mouseDown();
        pyautogui.move(0, -150, 0.2)
        pyautogui.mouseUp(); 
        
    if check_pixel_colour((368, 242), (255, 98, 0), center_x, center_y):
        pyautogui.moveTo(center_x + 368 , center_y + 242, duration=0) 
        pyautogui.mouseDown();
        pyautogui.move(0, -150, 0.2)
        pyautogui.mouseUp();  
    
def data_task():
    print("Upload/Download Data Task")

    pyautogui.moveTo(center_x - 8, center_y + 110, duration=0)
    pyautogui.click()
    
def clean_vent():
    print("Clean Vent")

    pyautogui.moveTo(center_x, center_y, duration=0)
    pyautogui.click()
    time.sleep(0.2)
    
    top_left_x = -384
    top_left_y = -347
    bottom_right_x = 371
    bottom_right_y = 316
    rows = 10
    columns = 10
    
    width = bottom_right_x - top_left_x
    height = bottom_right_y - top_left_y
    row_gap = height / (rows - 1)
    col_gap = width / (columns - 1)
    
    for row in range(rows):
        for col in range(columns):
            target_x = top_left_x + col * col_gap
            target_y = top_left_y + row * row_gap
            pyautogui.moveTo(center_x + target_x, center_y + target_y, duration=0)
            pyautogui.click()
    

def wires():
    print("Wires")
    
    colours_to_check = [((38, 38, 255), "blue"), ((255, 0, 255), "magenta"), ((255, 235, 4), "yellow"), ((255, 0, 0), "red")]
    positions_to_check = [(-400, -268), (-400, -80), (-400, 104), (-400, 295)]

    for position in positions_to_check:
        for colour, colour_name in colours_to_check:
            if check_pixel_colour(position, colour, center_x, center_y):
                for offset_y in [-268, -81, 105, 289]:
                    if check_pixel_colour((361, offset_y), colour, center_x, center_y):
                        pyautogui.moveTo(center_x + position[0], center_y + position[1], duration=0)
                        pyautogui.mouseDown()
                        pyautogui.moveTo(center_x + 361, center_y + offset_y, 0.2)
                        time.sleep(0.2)
                        pyautogui.mouseUp()
                        break
                break

def start_reactor():
    print("Reactor: Start Reactor")

def clean_o2():
    print("O2: Clean O2 Filter")
    
def unlock_manifolds():
    print("Reactor: Unlock Manifolds")

def inspect_sample():
    print("MedBay: Inspect Sample")
    pyautogui.moveTo(center_x + 304, center_y + 395, duration=0)
    time.sleep(0.1)
    pyautogui.click()
    
    if check_pixel_colour((-227, 48), (246, 134, 134), center_x, center_y):
        pyautogui.moveTo(center_x -227, center_y + 306, duration=0)
        time.sleep(0.1)
        pyautogui.click()
    
    if check_pixel_colour((-111, 48), (246, 134, 134), center_x, center_y):
        pyautogui.moveTo(center_x -111, center_y + 306, duration=0)
        time.sleep(0.1)
        pyautogui.click()

    if check_pixel_colour((0, 48), (246, 134, 134), center_x, center_y):
        pyautogui.moveTo(center_x, center_y + 306, duration=0)
        time.sleep(0.1)
        pyautogui.click()
        
    if check_pixel_colour((117, 48), (246, 134, 134), center_x, center_y):
        pyautogui.moveTo(center_x + 117, center_y + 306, duration=0)
        time.sleep(0.1)
        pyautogui.click()
    
    if check_pixel_colour((227, 48), (246, 134, 134), center_x, center_y):
        pyautogui.moveTo(center_x + 227, center_y + 306, duration=0)
        time.sleep(0.1)
        pyautogui.click()


def clear_asteroids():
    print("Weapons: Clear Asteroids")
    
    # Crude - could do with a better way of detecting a pixel colour in a given area
    while check_pixel_colour((-505, -388), (238, 238, 238), center_x, center_y):
        pyautogui.moveTo(center_x + 280, center_y - 347, duration=0)
        time.sleep(0.05)
        pyautogui.click()
        time.sleep(0.05)
        pyautogui.moveTo(center_x + 280, center_y - 226, duration=0)
        time.sleep(0.05)
        pyautogui.click()
        time.sleep(0.05)
        pyautogui.moveTo(center_x + 280, center_y - 104, duration=0)
        time.sleep(0.05)
        pyautogui.click()
        time.sleep(0.05)
        pyautogui.moveTo(center_x + 280, center_y + 77, duration=0)
        time.sleep(0.05)
        pyautogui.click()
        time.sleep(0.05)
        pyautogui.moveTo(center_x + 280, center_y + 285, duration=0)
        time.sleep(0.05)
        pyautogui.click()
        time.sleep(0.05)
        pass

def stabalize_steering():
    print("Navigation: Stabalize Steering")
    pyautogui.moveTo(center_x, center_y, duration=0)
    pyautogui.click()
    
def divert_power_2():
    print("Divert Power - Part 2")
    pyautogui.moveTo(center_x, center_y, duration=0)
    pyautogui.click()
    
def chart_course():
    print("Navigation: Chart Course")

def prime_shields():
    print("Prime Shields")
    
    if check_pixel_colour((-142, -105), (202, 98, 116), center_x, center_y, 10):
        time.sleep(0.1)
        pyautogui.moveTo(center_x - 142, center_y - 105, duration=0)
        time.sleep(0.1)
        pyautogui.click()

        
    if check_pixel_colour((26, -180), (202, 98, 116), center_x, center_y, 10):
        time.sleep(0.1)
        pyautogui.moveTo(center_x + 26, center_y - 180, duration=0)
        time.sleep(0.1)
        pyautogui.click()
        
    if check_pixel_colour((180, -116), (202, 98, 116), center_x, center_y, 10):
        time.sleep(0.1)
        pyautogui.moveTo(center_x + 180, center_y - 116, duration=0)
        time.sleep(0.1)
        pyautogui.click()
        
    if check_pixel_colour((-176, 84), (202, 98, 116), center_x, center_y, 10):
        time.sleep(0.1)
        pyautogui.moveTo(center_x - 176, center_y + 84, duration=0)
        time.sleep(0.1)
        pyautogui.click()
        
    if check_pixel_colour((-38, 188), (202, 98, 116), center_x, center_y, 10):
        time.sleep(0.1)
        pyautogui.moveTo(center_x - 38, center_y + 188, duration=0)
        time.sleep(0.1)
        pyautogui.click()
        
    if check_pixel_colour((190, 67), (202, 98, 116), center_x, center_y, 10):
        time.sleep(0.1)
        pyautogui.moveTo(center_x + 190, center_y + 67, duration=0)
        time.sleep(0.1)
        pyautogui.click()
    
def refuel_station():
    print("Refuel Station")
    pyautogui.moveTo(center_x + 502, center_y + 334, duration=0)
    pyautogui.mouseDown();
    time.sleep(3.1)
    pyautogui.mouseUp();

def align_engine():
    print("Align Engine ")
    
    engine_x = 320
    engine_y = -400
    
    align_found = False
    
    # Maybe a better method that takes an snapshot of an area then finds the first instance of a pixel with given colour
    while not align_found:
        if check_pixel_colour((engine_x, engine_y), (202, 202, 216), center_x, center_y):
            pyautogui.moveTo(center_x + engine_x, center_y + engine_y, duration=0)
            pyautogui.mouseDown()
            pyautogui.moveTo(center_x + 279, center_y, 0.2)
            pyautogui.mouseUp()
            align_found = True
        
        engine_y += 5
    
def calibrate_distributor():
    print("Calibrate Distributor")

    step_1 = 0
    step_2 = 0
    step_3 = 0

    while step_1 == 0:
        if check_pixel_colour((272, -302), (255, 227, 0), center_x, center_y, 10):
            pyautogui.moveTo(center_x + 272, center_y - 231, duration=0)
            pyautogui.click()
            step_1 = 1
        time.sleep(0.05)
        pass
        
    while step_2 == 0:
        if check_pixel_colour((272, -47), (83, 98, 255), center_x, center_y, 10):
            pyautogui.moveTo(center_x + 272, center_y + 42, duration=0)
            pyautogui.click()
            step_2 = 1
        time.sleep(0.05)
        pass
        
    while step_3 == 0:
        if check_pixel_colour((272, 219), (111, 249, 255), center_x, center_y, 10):
            pyautogui.moveTo(center_x + 272, center_y + 300, duration=0)
            pyautogui.click()
            step_3 = 1
        time.sleep(0.05)
        pass

def empty_chute():
    print("Empty Chute")
    pyautogui.moveTo(center_x + 318, center_y -124, duration=0)
    pyautogui.mouseDown();
    pyautogui.move(0, 300, 0.2)
    time.sleep(1.5)
    pyautogui.mouseUp();

# Specify coordinates and colours to check, then run the task function if conditions are met    
pixel_array = [
    in_map,
    [
        ((-814, -421), (238, 238, 238)),
        ((-814, -396), (51, 51, 51))
    ],   
    next_to_task,
    [
        ((798, 397), (173, 185, 189)),
        ((828, 408), (189, 200, 206))
    ],
    admin_swipe_card,
    [
        ((-517, -397), (238, 238, 238)),
        ((-215, -388), (22, 74, 57))
    ],
    data_task,
    [
        ((361, -66), (242, 215, 169)),
        ((-266, -164), (221, 227, 233))
    ],
    clean_vent,
    [
        ((-373, -351), (148, 170, 173)),
        ((503, -83), (148, 170, 173))
    ],
    divert_power,
    [
        ((0, -353), (255, 255, 255)),
        ((-348, -12), (253, 255, 92))
    ],
    wires,
    [
        ((427, -338), (57, 62, 66)),
        ((424, -299), (51, 51, 51))
    ],
    start_reactor,
    [
        ((-354, -307), (203, 204, 203)),
        ((499, 307), (66, 65, 66))
    ],
    clean_o2,
    [
        ((-431, 436), (57, 57, 57)),
        ((-495, -403), (238, 238, 238))
    ],
    unlock_manifolds,
    [
        ((-523, -182), (238, 238, 238)),
        ((-357, -121), (142, 161, 208))
    ],
    inspect_sample,
    [
        ((-494, -430), (238, 238, 238)),
        ((391, -248), (121, 120, 126))
    ],
    clear_asteroids,
    [
        ((-508, -388), (238, 238, 238)),
        ((-373, 358), (255, 255, 255))
    ],
    stabalize_steering,
    [
        ((-367, -361), (197, 208, 219)),
        ((351, -368), (197, 208, 219))
    ],
    chart_course,
    [
        ((-627, -310), (238, 238, 238)),
        ((209, -314), (198, 208, 220))
    ],
    prime_shields,
    [
        ((-337, -390), (101, 102, 101)),
        ((-92, -400), (30, 73, 145))
    ],
    refuel_station, 
    [
        ((8, -232), (0, 0, 0)),
        ((-14, 80), (0, 0, 0))
    ],
    align_engine,
    [
        ((-313, 314), (12, 30, 12)),
        ((-368, -375), (12, 30, 12))
    ],
    empty_chute,
    [
        ((-499, -432), (238, 238, 238)),
        ((269, -442), (156, 169, 192))
    ],
    calibrate_distributor,
    [
        ((161, -313), (255, 227, 0)),
        ((158, 229), (111, 249, 255))
    ],
    divert_power_2,
    [
        ((-621, -262), (238, 238, 238)),
        ((18, -221), (105, 105, 105))
    ]
]

if is_among_us_running():
    #print("Among Us.exe is running!")
    
    # Get windows with the exact title "Among Us"
    among_us_windows = [window for window in pygetwindow.getWindowsWithTitle("") if window.title == "Among Us"]
    
    if among_us_windows:
        # Assuming you want to use the first window found
        among_us_window = among_us_windows[0]
        width = among_us_window.width
        height = among_us_window.height
        aspect_ratio = width / height if height != 0 else 0
        #print(f"Window width: {width}, height: {height}, aspect ratio: {aspect_ratio:.2f}")
        # Get the center coordinates of the window
        center_x = among_us_window.left + width // 2
        center_y = among_us_window.top + height // 2
        
    else:
        print("No window with the title 'Among Us' found.")
else:
    print("Among Us.exe is not running.")

keyboard.add_hotkey('space', keyboard_hotkey)
keyboard.wait()