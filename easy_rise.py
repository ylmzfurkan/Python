# -*- coding: utf-8 -*-
"""
@author: Emilio Moretti
Copyright 2013 Emilio Moretti <emilio.morettiATgmailDOTcom>
This program is distributed under the terms of the GNU Lesser General Public License.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.
"""
import random
import time
from datetime import datetime, timedelta

import win32api
import win32gui

# The example starts here
from AutoHotPy import AutoHotPy  # we need to tell python that we are going to use the library


#TESTING
import cv2
import pytesseract
from PIL import ImageGrab
import os
import  numpy as np

import numpy as np
from InterceptionWrapper import InterceptionMouseState, InterceptionMouseStroke, InterceptionMouseFlag
from PIL import Image



# CONFIGURATION
HEALING_POT_KEY = 0  # Change accordingly
MANA_POT_KEY = 9  # Change accordingly
HEAL_PARTY_MEMBER_KEY = 2  # Change accordingly
start_time=0

# Available pages -> F1, F2, F3, F4, F5, F6, F7
ACTIVE_SKILL_PAGES = {
    #'F4': [1,2,3,4,5]  # Change accordingly
    'F1':[2]
}

# Be careful not to overlap any skills with your HEAL/MANA pot keys

# One skill page with F4 example is below
# ACTIVE_SKILL_PAGES = {
#     'F4': [3, 4, 5, 6]
# }

ENABLE_R_HITS = True  # Change it to True for basic attacks

# Do not change anything below this line
SELF_HP_X = 195
SELF_HP_Y = 46

SELF_MP_X = 180
SELF_MP_Y = 66

MONSTER_HP_X=960-30
MONSTER_HP_y=46

FIRST_PARTY_MEMBER_X = 1799
FIRST_PARTY_MEMBER_Y = 258
CURRENT_PARTY = []
PARTY_VALID_R = 159
PARTY_VALID_G = 57
PARTY_VALID_B = 39
PARTY_MEMBER_OFFSET_Y = 145

repeat_always = False
is_r_used=False

SELECTED_RUNTIME_CONFIGURATION = 0  # None
TIME_DELAY_BETWEEN_SKILLS = 0.1  # in seconds

HP_R = 0
HP_G = 0
HP_B = 0
MP_R = 0
MP_G = 0
MP_B = 0

number_template_dict = {
    0: "num_0.png",
    1: "num_1.png",
    2: "num_2.png",
    3: "num_3.png",
    4: "num_4.png",
    5: "num_5.png",
    6: "num_6.png",
    7: "num_7.png",
    8: "num_8.png",
    9: "num_9.png",

}
# END CONFIGURATION

# IMAGE PROCESSING


def nothing(x):
    pass

def enhance_contrast(image, clip_limit=2.0, tile_grid_size=(8, 8)):
    # Convert to LAB color space
    lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(lab)

    # Apply CLAHE (Contrast Limited Adaptive Histogram Equalization)
    clahe = cv2.createCLAHE(clipLimit=clip_limit, tileGridSize=tile_grid_size)
    l = clahe.apply(l)

    # Merge channels and convert back to BGR color space
    enhanced_lab = cv2.merge([l, a, b])
    enhanced_image = cv2.cvtColor(enhanced_lab, cv2.COLOR_LAB2BGR)

    return enhanced_image

def enhance_contrast_grayscale(image, clip_limit=2.0, tile_grid_size=(8, 8)):
    # Apply CLAHE (Contrast Limited Adaptive Histogram Equalization) to a grayscale image
    clahe = cv2.createCLAHE(clipLimit=clip_limit, tileGridSize=tile_grid_size)
    enhanced_image = clahe.apply(image)

    return enhanced_image

def refine_red_extraction_and_debug(image, specific_red_rgb, save_path_prefix):
    # Ensure the save_path_prefix directory exists
    os.makedirs(os.path.dirname(save_path_prefix), exist_ok=True)

    img = image

    # # Create a window
    # cv2.namedWindow('image')
    #
    # # create trackbars for color change
    # cv2.createTrackbar('HMin', 'image', 0, 179, nothing)  # Hue is from 0-179 for Opencv
    # cv2.createTrackbar('SMin', 'image', 0, 255, nothing)
    # cv2.createTrackbar('VMin', 'image', 0, 255, nothing)
    # cv2.createTrackbar('HMax', 'image', 0, 179, nothing)
    # cv2.createTrackbar('SMax', 'image', 0, 255, nothing)
    # cv2.createTrackbar('VMax', 'image', 0, 255, nothing)
    #
    # # Set default value for MAX HSV trackbars.
    # cv2.setTrackbarPos('HMax', 'image', 179)
    # cv2.setTrackbarPos('SMax', 'image', 255)
    # cv2.setTrackbarPos('VMax', 'image', 255)
    #
    # # Initialize to check if HSV min/max value changes
    # hMin = sMin = vMin = hMax = sMax = vMax = 0
    # phMin = psMin = pvMin = phMax = psMax = pvMax = 0
    #
    # output = image
    # wait_time = 33
    #
    # while (1):
    #
    #     # get current positions of all trackbars
    #     hMin = cv2.getTrackbarPos('HMin', 'image')
    #     sMin = cv2.getTrackbarPos('SMin', 'image')
    #     vMin = cv2.getTrackbarPos('VMin', 'image')
    #
    #     hMax = cv2.getTrackbarPos('HMax', 'image')
    #     sMax = cv2.getTrackbarPos('SMax', 'image')
    #     vMax = cv2.getTrackbarPos('VMax', 'image')
    #
    #     # Set minimum and max HSV values to display
    #     lower = np.array([hMin, sMin, vMin])
    #     upper = np.array([hMax, sMax, vMax])
    #
    #     # Create HSV Image and threshold into a range.
    #     hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    #     mask = cv2.inRange(hsv, lower, upper)
    #     output = cv2.bitwise_and(image, image, mask=mask)
    #
    #     # Print if there is a change in HSV value
    #     if ((phMin != hMin) | (psMin != sMin) | (pvMin != vMin) | (phMax != hMax) | (psMax != sMax) | (pvMax != vMax)):
    #         print("(hMin = %d , sMin = %d, vMin = %d), (hMax = %d , sMax = %d, vMax = %d)" % (
    #         hMin, sMin, vMin, hMax, sMax, vMax))
    #         phMin = hMin
    #         psMin = sMin
    #         pvMin = vMin
    #         phMax = hMax
    #         psMax = sMax
    #         pvMax = vMax
    #
    #     # Display output image
    #     cv2.imshow('image', output)
    #
    #     # Wait longer to prevent freeze for videos.
    #     if cv2.waitKey(wait_time) & 0xFF == ord('q'):
    #         break
    #
    # cv2.destroyAllWindows()
    # exit(1)

    lower = np.array([18, 0, 0])
    upper = np.array([179, 255, 255])

    # Create HSV Image and threshold into a range.
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower, upper)
    output = cv2.bitwise_and(image, image, mask=mask)
    cv2.imwrite(f"{save_path_prefix}output_img_00_NEW.png", output)

    image = output
    # Apply the mask to isolate red color
    isolated_red = cv2.bitwise_and(image, image, mask=mask)
    cv2.imwrite(f"{save_path_prefix}_03_isolated_red.png", isolated_red)

    # Convert to grayscale
    gray_image = cv2.cvtColor(isolated_red, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(f"{save_path_prefix}_04_gray.png", gray_image)

    # Enhance contrast using histogram equalization
    equalized_image = cv2.equalizeHist(gray_image)
    cv2.imwrite(f"{save_path_prefix}_05_equalized.png", equalized_image)

    # Background is black, text is white. just reverse and return
    #your code
    # Invert the image to get white background and black text
    inverted_image = cv2.bitwise_not(equalized_image)
    cv2.imwrite(f"{save_path_prefix}_06_inverted_for_ocr.png", inverted_image)

    new_img = enhance_contrast_grayscale(inverted_image)
    contrasted_image_path = f"{save_path_prefix}_07_contrasted_for_ocr.png"
    cv2.imwrite(contrasted_image_path, new_img)

    return inverted_image


def process_and_extract_text(screenshot, save_path_prefix):
    image = np.array(screenshot)
    specific_red_rgb = [239, 50, 110]  # The specific red of the text
    processed_image = refine_red_extraction_and_debug(image, specific_red_rgb, save_path_prefix)
    cv2.imwrite(f"{save_path_prefix}ocr_input_image.png", processed_image)

    text = pytesseract.image_to_string(Image.open("test_4.png"), config='--psm 6')
    return text.strip()


def match_template(original_image, template_image, threshold=0.8):
    # Read the main image and template
    main_img = original_image
    template_img = template_image

    # Convert images to grayscale
    main_gray = cv2.cvtColor(main_img, cv2.COLOR_BGR2GRAY)
    template_gray = cv2.cvtColor(template_img, cv2.COLOR_BGR2GRAY)

    # Apply template matching
    res = cv2.matchTemplate(main_gray, template_gray, cv2.TM_CCOEFF_NORMED)

    # Find locations where the matching result exceeds the threshold
    locations = np.where(res >= threshold)
    w, h = template_gray.shape[::-1]

    return locations, w, h
    # Get the dimensions of the template image

    # Draw rectangles around the detected numpad
    for loc in zip(*locations[::-1]):
        top_left = loc
        bottom_right = (top_left[0] + w, top_left[1] + h)
        cv2.rectangle(main_img, top_left, bottom_right, color=(0, 255, 0), thickness=2)

    # If any rectangles are drawn (i.e., numpad is found), save the debug image
    if locations[0].size > 0:
        debug_image_path = save_path_prefix + "detected_numpad.png"
        cv2.imwrite(debug_image_path, main_img)
        print(f"Numpad detected and image saved to {debug_image_path}")
        return True, top_left, bottom_right  # Return the bounding box coordinates of the numpad

    return False, None, None  # Return False if no numpad is found
def find_numpad_in_image(image_path, template_path, save_path_prefix, threshold=0.8):
    # Read the main image and template
    main_img = cv2.imread(image_path)
    template_img = cv2.imread(template_path)

    # Convert images to grayscale
    main_gray = cv2.cvtColor(main_img, cv2.COLOR_BGR2GRAY)
    template_gray = cv2.cvtColor(template_img, cv2.COLOR_BGR2GRAY)

    # Apply template matching
    res = cv2.matchTemplate(main_gray, template_gray, cv2.TM_CCOEFF_NORMED)

    # Find locations where the matching result exceeds the threshold
    locations = np.where(res >= threshold)

    # Get the dimensions of the template image
    w, h = template_gray.shape[::-1]

    # Draw rectangles around the detected numpad
    for loc in zip(*locations[::-1]):
        top_left = loc
        bottom_right = (top_left[0] + w, top_left[1] + h)
        cv2.rectangle(main_img, top_left, bottom_right, color=(0, 255, 0), thickness=2)

    # If any rectangles are drawn (i.e., numpad is found), save the debug image
    if locations[0].size > 0:
        debug_image_path = save_path_prefix + "detected_numpad.png"
        cv2.imwrite(debug_image_path, main_img)
        print(f"Numpad detected and image saved to {debug_image_path}")
        return True, top_left, bottom_right  # Return the bounding box coordinates of the numpad

    return False, None, None  # Return False if no numpad is found

image_path = '5_mob_test.png'
template_path = 'harpy_template_2.png'
save_path_prefix = 'C:/Users/pFFed/PycharmProjects/captcha/'
numpad_found, top_left, bottom_right = find_numpad_in_image(image_path, template_path, save_path_prefix)

if numpad_found:
    print(f"Numpad found at: Top Left - {top_left}, Bottom Right - {bottom_right}")
else:
    print("Numpad not found in the image.")

# Setup paths and pytesseract executable location
save_path_prefix = 'C:\\Users\\pFFed\\PycharmProjects\\easyko'  # Update this path as needed
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Define coordinates and dimensions for the image capture
x, y = 146, 1272
width, height = 400, 30

# Extract text

def extractMobName():
    # screenshot = ImageGrab.grab(bbox=(x, y, x + width, y + height))
    screenshot  = Image.open("test.png")
    debug_image_path = "first_debug_screenshot.png"
    screenshot.save(debug_image_path)
    extracted_text = process_and_extract_text(screenshot, save_path_prefix)
    return extracted_text

# END IMAGE PROCESSING



# INITIALIZATION
def readPixel(x, y):
    if x >= 1920:
        x = 1919
    if y >= 1080:
        y = 1079
    color = win32gui.GetPixel(win32gui.GetDC(win32gui.GetActiveWindow()), x, y)
    r, g, b = rgbint2rgbtuple(color)
    return r, g, b

def checkMonsterHealtLow():
    global HP_R
    x, y = MONSTER_HP_X, MONSTER_HP_y
    r, g, b = readPixel(x, y)
    if(r+10<HP_R):
        return True
    else:
        return False

def checkMana():
    global SELF_MP_R, SELF_MP_G, SELF_MP_B, SELF_MP_X, SELF_MP_Y
    x, y = SELF_MP_X, SELF_MP_Y
    r, g, b = readPixel(x, y)
    # print("Checking mana with RGB: {}, {}, {} against {}, {}, {}".format(r, g, b, MP_R, MP_G, MP_B))
    if r != 0 and g != 0 and b != 0:
         return False
     #   print("MP is above 35%")
    else:
    #    print("Using MP with KEY {}".format(MANA_POT_KEY))
        return True


def checkHealth():
    if checkMana():
        return
    global SELF_HP_R, SELF_HP_G, SELF_HP_B, SELF_HP_X, SELF_HP_Y
    x, y = SELF_HP_X, SELF_HP_Y
    r, g, b = readPixel(x, y)
    #print("Checking health with RGB: {}, {}, {} against {}, {}, {}".format( r, g, b, HP_R, HP_G, HP_B))
    if r != 0 and g != 0 and b != 0:
        return False
         #print("\n")
       # print("HP is above 40%")
    else:
      #  print("Using HP with KEY {}".format(HEALING_POT_KEY))
        return True

def checkPartyMemberHealth(x,y):
    r, g, b = readPixel(x, y)
    print(f"[{x}, {y}] -> RGB: {r} {g} {b}")
    if r == 169 and g == 6 and b == 9:
        return False
    else:
        return True

def clickPartyMember(autohotpy, event, x,y):
    autohotpy.moveMouseToPosition(x,y)
    time.sleep(0.3)
    leftButton(autohotpy, event)

def checkRepair():
    global SELF_ITEM_R, SELF_ITEM_G, SELF_ITEM_B, SELF_ITEM_X, SELF_ITEM_Y
    x, y = SELF_ITEM_X, SELF_ITEM_Y
    r, g, b = readPixel(x, y)
    #print("Checking health with RGB: {}, {}, {} against {}, {}, {}".format( r, g, b, HP_R, HP_G, HP_B))
    if r < 200:
        return False
         #print("\n")
       # print("HP is above 40%")
    else:
      #  print("Using HP with KEY {}".format(HEALING_POT_KEY))
        return True


# def checkPartyMemberHealth(x, y):
#     color = win32gui.GetPixel(win32gui.GetDC(win32gui.GetActiveWindow()), x, y)
#     r, g, b = rgbint2rgbtuple(color)
#     if r < 75:
#         print("Party member [{},{}] is at RGB: {}, {}, {}".format(
#             x, y, r, g, b))

def rgbint2rgbtuple(RGBint):
    red = RGBint & 255
    green = (RGBint >> 8) & 255
    blue = (RGBint >> 16) & 255
    return (red, green, blue)

def recordColorOfCursorPos():
    for i in range(2,0,-1):
        print("Recording color in {} seconds".format(i))
        time.sleep(1)
    x, y = win32api.GetCursorPos()
    r,g,b = readPixel(x,y)
    print("Recored r,g,b = {}, {}, {} at x,y = [{}, {}]".format(r,g,b,x,y))
    return x,y,r,g,b
#
print("Can nereye gelince pot basılsın? (mouse'u üzerinde beklet)")
SELF_HP_X, SELF_HP_Y, SELF_HP_R, SELF_HP_G, SELF_HP_B = recordColorOfCursorPos()

print("Mana nereye gelince pot basılsın? (mouse'u üzerinde beklet)")
SELF_MP_X, SELF_MP_Y, SELF_MP_R, SELF_MP_G, SELF_MP_B = recordColorOfCursorPos()

#print("Ilk party member can nereye gelince party heal atilsin (mouse beklet)")
#time.sleep(1)
#PARTY_FIRST_X, PARTY_FIRST_Y, PARTY_FIRST_R, PARTY_FIRST_G, PARTY_FIRST_B = recordColorOfCursorPos()
#SELF_ITEM_R, SELF_ITEM_G, SELF_ITEM_B = readPixel(PARTY_FIRST_X, PARTY_FIRST_Y)
#print("item rgb {} {} {}".format(SELF_ITEM_R, SELF_ITEM_G, SELF_ITEM_B))
# END INITIALIZATION


# The following function is called when you press ESC.
# autohotpy is the instance that controlls the library, you should do everything through it.
def exitAutoHotKey(autohotpy, event):
    print("Stopping with  " + event)
    autohotpy.stop()  # makes the program finish successfully. Thisis the right way to stop it


def waitBetweenKeys():
    random_number = random.uniform(0.05, 0.1)
    time.sleep(random_number)

def pressZ(autohotpy):
    autohotpy.Z.press()
    waitBetweenKeys()
    return extractMobName()


def leftButton(autohotpy,event):
    """
    This function simulates a left click
    """
    stroke = InterceptionMouseStroke()
    autohotpy.sendToDefaultMouse(stroke)
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_LEFT_BUTTON_DOWN
    autohotpy.sendToDefaultMouse(stroke)
    time.sleep(0.05)
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_LEFT_BUTTON_UP
    autohotpy.sendToDefaultMouse(stroke)

def rightButtonAndDrag(autohotpy, event):
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_RIGHT_BUTTON_DOWN
    autohotpy.sendToDefaultMouse(stroke)
    waitBetweenKeys()
    for i in range(750,901,50):
        event.x += 50
        time.sleep(0.01)
        autohotpy.sendToDefaultMouse(event)
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_RIGHT_BUTTON_UP
    autohotpy.sendToDefaultMouse(stroke)


def torment(autohotpy, event):
    global torment_time
    if torment_time is None:
        torment_time = datetime.now()
        print(f"torment_time recorded at: {malice_time}")
        autohotpy.Z.press()
        time.sleep(0.3)
        pressKeyNTimes(autohotpy.N5)
        time.sleep(0.2)
        leftButton(autohotpy, event)
    else:
        if datetime.now() - torment_time > timedelta(seconds=15):
            print("15 secs have passed since torment_time was recorded.")
            time.sleep(0.2)
            time.sleep(0.3)
            pressKeyNTimes(autohotpy.N5)
            time.sleep(0.2)
            leftButton(autohotpy, event)


def helishCombo(autohotpy):
    autohotpy.R.press()
    time.sleep(0.20)
    autohotpy.R.press()
    time.sleep(0.20)
    autohotpy.R.press()
    time.sleep(0.10)
    autohotpy.R.press()
    time.sleep(0.10)
    autohotpy.N2.press()
    time.sleep(0.10)


kitap_time = None
str_time = None
malice_time = None
torment_time = None

def pressKeyNTimes(key):
    random_number = int(random.uniform(2, 8))
    for i in range(0, random_number):
        key.press()
    key.press()
def kitap(autohotpy):
    global kitap_time
    if kitap_time is None:
        kitap_time = datetime.now()
        print(f"kitap_time recorded at: {kitap_time}")
        pressKeyNTimes(autohotpy.N7)
    else:
        if datetime.now() - kitap_time > timedelta(minutes=0, seconds=21):
            print("4 minutes have passed since kitap_time was recorded.")
            pressKeyNTimes(autohotpy.N7)
            kitap_time = datetime.now()

def selfStr(autohotpy):
    global str_time
    if str_time is None:
        str_time = datetime.now()
        print(f"str_time recorded at: {str_time}")
        pressKeyNTimes(autohotpy.N7)
    else:
        if datetime.now() - str_time > timedelta(minutes=12, seconds=1):
            print("12 minutes have passed since str_time was recorded.")
            pressKeyNTimes(autohotpy.N7)
            str_time = datetime.now()

def malice(autohotpy):
    global malice_time
    if malice_time is None:
        malice_time = datetime.now()
        print(f"malice_time recorded at: {malice_time}")
        time.sleep(0.2)
        autohotpy.Z.press()
        autohotpy.F2.press()
        pressKeyNTimes(autohotpy.N3)
        autohotpy.F1.press()
        malice_time = datetime.now()
        time.sleep(0.8)
    else:
        if datetime.now() - malice_time > timedelta(seconds=8):
            print("8 secs have passed since malice_time was recorded.")
            time.sleep(0.2)
            autohotpy.Z.press()
            autohotpy.F2.press()
            pressKeyNTimes(autohotpy.N3)
            autohotpy.F1.press()
            malice_time = datetime.now()
            time.sleep(0.8)

def sprint(autohotpy):
    pressKeyNTimes(autohotpy.N8)

right_drag_time = datetime.now()

def partyHealer(autohotpy, event):
    global PARTY_FIRST_X, PARTY_FIRST_Y
    partySize = 8
    needs = []
    for i in range(0,partySize):
        needs.append(False)

    trueCount = 0
    for i in range(0, partySize):
        #print(f"Trying to read {(PARTY_FIRST_X, PARTY_FIRST_Y + (i*50))}")
        if i == 7:
            needs[i] = checkPartyMemberHealth(PARTY_FIRST_X, (PARTY_FIRST_Y + (i * 51) + 2))
        else:
            needs[i] = checkPartyMemberHealth(PARTY_FIRST_X, PARTY_FIRST_Y + (i * 51))

        if needs[i]:
            trueCount += 1
            print(f"Party member {i} needs heal")


    if trueCount > 3:
        # party heal
        autohotpy.N2.press()
        autohotpy.N3.press()
    else:
        for i in range(0, partySize):
            if needs[i]:
                clickPartyMember(autohotpy, event, PARTY_FIRST_X, PARTY_FIRST_Y + (i*50))
                time.sleep(0.6)
                autohotpy.N0.press()
                time.sleep(1.62)


def capture_screenshot_to_cv2():
    # Capture the screen
    screenshot = ImageGrab.grab()
    # Convert the screenshot to a numpy array
    screenshot_np = np.array(screenshot)
    # Convert the color space from BGR (Pillow's default) to RGB, which OpenCV uses
    screenshot_cv2 = cv2.cvtColor(screenshot_np, cv2.COLOR_BGR2RGB)
    screenshot_filename = 'screenshot_taken_live.png'
    cv2.imwrite(screenshot_filename, screenshot_cv2)
    return screenshot_cv2


def get_random_point_within_rectangle(top_left, bottom_right):
    """
    Returns a random point within the rectangle defined by top_left and bottom_right.

    Parameters:
    top_left (tuple): A tuple of the form (x, y) representing the top left corner of the rectangle.
    bottom_right (tuple): A tuple of the form (x, y) representing the bottom right corner of the rectangle.

    Returns:
    tuple: A tuple representing a random point within the rectangle.
    """
    if top_left[0] >= bottom_right[0] or top_left[1] >= bottom_right[1]:
        raise ValueError("Top left must be above and to the left of bottom right.")

    random_x = random.randint(top_left[0], bottom_right[0])
    random_y = random.randint(top_left[1], bottom_right[1])

    return (random_x, random_y)


def leftClick(autohotpy, event, x, y):
    # stroke = InterceptionMouseStroke()
    # stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    # stroke.x = x
    # stroke.y = y
    # autohotpy.sendToDefaultMouse(stroke)
    # time.sleep(2)
    # leftButton(autohotpy, event)


    # Simulate a left mouse button click
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_LEFT_BUTTON_DOWN
    autohotpy.sendToDefaultMouse(stroke)
    waitBetweenKeys() # Small delay to simulate hold time of a real click
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_LEFT_BUTTON_UP
    autohotpy.sendToDefaultMouse(stroke)

from PIL import Image, ImageOps, ImageEnhance


def getCoords(autohotpy, event):
    # Create a window
    cv2.namedWindow('image', cv2.WINDOW_NORMAL)

    # Set the window size to 480x480
    cv2.resizeWindow('image', 480, 480)



    # create trackbars for color change
    cv2.createTrackbar('HMin', 'image', 0, 179, nothing)  # Hue is from 0-179 for Opencv
    cv2.createTrackbar('SMin', 'image', 0, 255, nothing)
    cv2.createTrackbar('VMin', 'image', 0, 255, nothing)
    cv2.createTrackbar('HMax', 'image', 0, 179, nothing)
    cv2.createTrackbar('SMax', 'image', 0, 255, nothing)
    cv2.createTrackbar('VMax', 'image', 0, 255, nothing)

    # Set default value for MAX HSV trackbars.
    cv2.setTrackbarPos('HMax', 'image', 179)
    cv2.setTrackbarPos('SMax', 'image', 255)
    cv2.setTrackbarPos('VMax', 'image', 255)

    # Initialize to check if HSV min/max value changes
    hMin = sMin = vMin = hMax = sMax = vMax = 0
    phMin = psMin = pvMin = phMax = psMax = pvMax = 0
    coor_top_left = (2374, 269)
    coor_bottom_right = (2437, 283)

    z_class_type_image = capture_screenshot(coor_top_left, coor_bottom_right)
    image = np.array(z_class_type_image)
    cv2.imwrite("Coords_img.png", image)
    output = image
    wait_time = 33

    while (1):
        coor_top_left = (2374, 269)
        coor_bottom_right = (2437, 283)

        z_class_type_image = capture_screenshot(coor_top_left, coor_bottom_right)
        image = np.array(z_class_type_image)
        cv2.imwrite("Coords_img.png", image)
        # get current positions of all trackbars
        hMin = cv2.getTrackbarPos('HMin', 'image')
        sMin = cv2.getTrackbarPos('SMin', 'image')
        vMin = cv2.getTrackbarPos('VMin', 'image')

        hMax = cv2.getTrackbarPos('HMax', 'image')
        sMax = cv2.getTrackbarPos('SMax', 'image')
        vMax = cv2.getTrackbarPos('VMax', 'image')

        # Set minimum and max HSV values to display
        lower = np.array([hMin, sMin, vMin])
        upper = np.array([hMax, sMax, vMax])

        # Create HSV Image and threshold into a range.
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, lower, upper)
        output = cv2.bitwise_and(image, image, mask=mask)

        # Print if there is a change in HSV value
        if ((phMin != hMin) | (psMin != sMin) | (pvMin != vMin) | (phMax != hMax) | (psMax != sMax) | (pvMax != vMax)):
            print("(hMin = %d , sMin = %d, vMin = %d), (hMax = %d , sMax = %d, vMax = %d)" % (
            hMin, sMin, vMin, hMax, sMax, vMax))
            phMin = hMin
            psMin = sMin
            pvMin = vMin
            phMax = hMax
            psMax = sMax
            pvMax = vMax

        # Display output image
        cv2.imshow('image', output)
        z_class = pytesseract.image_to_string(output)
        z_class = z_class.strip()
        print(f"Coords: {z_class}")

        # Wait longer to prevent freeze for videos.
        if cv2.waitKey(wait_time) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()


    coor_top_left = (2374, 269)
    coor_bottom_right = (2437, 283)

    z_class_type_image = capture_screenshot(coor_top_left, coor_bottom_right)
    z_class_type_image_np = np.array(z_class_type_image)
    # Convert the color space from BGR (Pillow's default) to RGB, which OpenCV uses
    z_class_type_image_np_confirmed = cv2.cvtColor(z_class_type_image_np, cv2.COLOR_BGR2RGB)
    cv2.imwrite("Coords.png", z_class_type_image_np_confirmed)

    z_class = pytesseract.image_to_string(z_class_type_image_np_confirmed)
    z_class = z_class.strip()
    print(f"Coords: {z_class}")

def preprocess_image_for_ocr(image):
    # Convert the image to grayscale
    gray_image = ImageOps.grayscale(image)

    # Enhance the contrast of the image
    enhancer = ImageEnhance.Contrast(gray_image)
    enhanced_image = enhancer.enhance(2.0)  # Adjust the factor to get the desired contrast

    # Invert the image colors if necessary
    inverted_image = ImageOps.invert(enhanced_image)

    # Convert image to binary (black and white) using a threshold
    threshold = 200  # You might need to adjust this threshold
    binary_image = inverted_image.point(lambda p: p > threshold and 255)

    return binary_image
def getZMobName(autohotpy, event):
    autohotpy.Z.press()
    mob_top_left = (762, 78)
    mob_bottom_right = (812, 92)

    z_class_type_image = capture_screenshot(mob_top_left, mob_bottom_right)
    z_class_type_image_np = np.array(z_class_type_image)
    # Convert the color space from BGR (Pillow's default) to RGB, which OpenCV uses
    z_class_type_image_np_confirmed = cv2.cvtColor(z_class_type_image_np, cv2.COLOR_BGR2RGB)
    #cv2.imwrite("3535.png", z_class_type_image_np_confirmed)

    #z_class = pytesseract.image_to_string(z_class_type_image_np_confirmed)
    #z_class = z_class.strip()


    # Assuming you have an image in numpy array format
    # You can convert it to a PIL image for preprocessing
    z_class_type_image_np_confirmed_pil = Image.fromarray(z_class_type_image_np_confirmed)

    # Preprocess the image
    preprocessed_image = preprocess_image_for_ocr(z_class_type_image_np_confirmed_pil)
    preprocessed_image = np.array(preprocessed_image)

    # Use pytesseract to do OCR on the preprocessed image
    z_class = pytesseract.image_to_string(preprocessed_image)
    z_class = z_class.strip()
    print(f"Z ClassType: {z_class}")
    return z_class


def getZEnabled(autohotpy, event):
    mob_top_left = (1111, 63)
    mob_bottom_right = (1185, 87)

    z_class_type_image = capture_screenshot(mob_top_left, mob_bottom_right)
    z_class_type_image_np = np.array(z_class_type_image)
    # Convert the color space from BGR (Pillow's default) to RGB, which OpenCV uses
    z_class_type_image_np_confirmed = cv2.cvtColor(z_class_type_image_np, cv2.COLOR_BGR2RGB)
    cv2.imwrite("z_clsas222s_img.png", z_class_type_image_np_confirmed)

    z_class = pytesseract.image_to_string(z_class_type_image_np_confirmed)
    z_class = z_class.strip()



    def preprocess_image_for_ocr(image):
        # Convert the image to grayscale
        gray_image = ImageOps.grayscale(image)

        # Enhance the contrast of the image
        enhancer = ImageEnhance.Contrast(gray_image)
        enhanced_image = enhancer.enhance(2.0)  # Adjust the factor to get the desired contrast

        # Invert the image colors if necessary
        inverted_image = ImageOps.invert(enhanced_image)

        # Convert image to binary (black and white) using a threshold
        threshold = 200  # You might need to adjust this threshold
        binary_image = inverted_image.point(lambda p: p > threshold and 255)

        return binary_image

    # Assuming you have an image in numpy array format
    # You can convert it to a PIL image for preprocessing
    z_class_type_image_np_confirmed_pil = Image.fromarray(z_class_type_image_np_confirmed)

    # Preprocess the image
    preprocessed_image = preprocess_image_for_ocr(z_class_type_image_np_confirmed_pil)
    preprocessed_image = np.array(preprocessed_image)
    cv2.imwrite("mob_preprocessed.png", preprocessed_image)

    # Use pytesseract to do OCR on the preprocessed image
    z_class = pytesseract.image_to_string(preprocessed_image)
    z_class = z_class.strip()
    print(f"Z ClassType: {z_class}")

    autohotpy.Z.press()
    r,g,b = readPixel(1064, 75)
    if r == 255 and g == 255 and b == 255:
        if z_class != "Priest" and z_class != "Warrior" and z_class != "Rogue" and z_class != "Mage":
            return True
        else:
            return False
    else:
        return False

coor_top_left = (2372, 367)
coor_bottom_right = (2437, 87)

def capture_screenshot(top_left, bottom_right):
    # Capture the entire screen
    screenshot = ImageGrab.grab()

    # Crop the screenshot to the specified area
    # The crop method takes a tuple of (left, top, right, bottom)
    cropped_screenshot = screenshot.crop(top_left + bottom_right)

    # Save or process the cropped screenshot as needed
    cropped_screenshot.save("cropped_screenshot.png")
    return cropped_screenshot
    # For displaying directly in Jupyter, you can use the display function
    # display(cropped_screenshot)
import re
def remove_non_numeric(s):
    # This regex pattern matches any character that is NOT a digit
    return re.sub(r'[^\d]', '', s)
#class CaptchaManager:
    offsets = [(-134, 2, 100, 40), #Captcha
               (-114, 132, 10, 5), #Minus
               (-80, 132, 14, 4), #Plusr
               (6, 67, 92, 27), #Continue
               (-301, -114, 427, 523)
    ]
    def __init__(self):
        pass

    def manageImageExtractionFromOffset(self, screenshot, top_left, index):
        if top_left:
            # Define the offsets for each additional image

            (offset_x, offset_y, width, height) = self.offsets[index]
            new_top_left_x = top_left[0] + offset_x
            new_top_left_y = top_left[1] + offset_y

            # Make sure the coordinates are within the screenshot boundaries
            new_top_left_x = max(new_top_left_x, 0)
            new_top_left_y = max(new_top_left_y, 0)
            new_bottom_right_x = min(new_top_left_x + width, screenshot.shape[1])
            new_bottom_right_y = min(new_top_left_y + height, screenshot.shape[0])

            # Extract the image using calculated coordinates
            extracted_image = screenshot[new_top_left_y:new_bottom_right_y, new_top_left_x:new_bottom_right_x]

            return extracted_image, (new_top_left_x, new_top_left_y), (new_bottom_right_x, new_bottom_right_y)
    def getCaptchaImage(self, screenshot, top_left):
        return self.manageImageExtractionFromOffset(screenshot, top_left, 0)
    def getMinusImage(self, screenshot, top_left):
        return self.manageImageExtractionFromOffset(screenshot, top_left, 1)

    def getPlusImage(self, screenshot, top_left):
        return self.manageImageExtractionFromOffset(screenshot, top_left, 2)

    def getContinueImage(self, screenshot, top_left):
        return self.manageImageExtractionFromOffset(screenshot, top_left, 3)

    def getMacroDetectionImage(self, screenshot, top_left):
        return self.manageImageExtractionFromOffset(screenshot, top_left, 4)

    def isCaptchaOnScreen(self, autohotpy, event) -> bool:
        captcha_template = "captcha_reload.png"
        screenshot = capture_screenshot_to_cv2()
        locations, template_width, template_height = match_template(screenshot, cv2.imread(captcha_template))


        if len(locations[0]) > 0:
            print("Captcha found on screen! Resolving...")

            # Get the first matching location
            top_left = next(zip(*locations[::-1]), None)
            if top_left:
                captcha_image, _, _ = self.getCaptchaImage(screenshot, top_left)
                text = pytesseract.image_to_string(captcha_image, config='--psm 6')
                text = text.strip()
                number_to_enter = remove_non_numeric(text)
                print(f"Extracted text: {number_to_enter}")

                minus_img, minus_top_left, minus_bottom_right = self.getMinusImage(screenshot, top_left)
                plus_img, plus_top_left, plus_bottom_right = self.getPlusImage(screenshot, top_left)
                cont_img, continue_top_left, continue_bottom_right = self.getContinueImage(screenshot, top_left)
                macro_img, macro_top_left, macro_bottom_right = self.getMacroDetectionImage(screenshot, top_left)

                cv2.imwrite(f"continue_image.png", cont_img)
                cv2.imwrite(f"minus_img.png", minus_img)
                cv2.imwrite(f"plus_image.png", plus_img)
                cv2.imwrite(f"captcha_image.png", captcha_image)
                cv2.imwrite(f"macro_img.png", macro_img)

                x, y = get_random_point_within_rectangle(plus_top_left, plus_bottom_right)
                print(f"clicking {x}, {y} in 5 seconds..")
                leftClick(autohotpy, event, x,y)
                autohotpy.S.press()

                def matchWindow():
                    return_obj = None
                    to_match_templates = ["0.png", "-1.png", "1.png", "-2.png", "2.png"]
                    main_img = macro_img

                    for del_template in to_match_templates:
                        resolved_img = cv2.imread(del_template)
                        del_locations, del_temp_w, del_temp_h = match_template(macro_img, resolved_img)

                        # Draw rectangles around the detected numpad
                        for loc in zip(*del_locations[::-1]):
                            top_left = loc
                            bottom_right = (top_left[0] + del_temp_w, top_left[1] + del_temp_h)
                            cv2.rectangle(main_img, top_left, bottom_right, color=(0, 255, 0), thickness=2)

                        # If any rectangles are drawn (i.e., numpad is found), save the debug image
                        if del_locations[0].size > 0:
                            debug_image_path = f"{del_template}_detected_numpad.png"
                            cv2.imwrite(debug_image_path, main_img)
                            print(f"Numpad detected and image saved to {debug_image_path}")
                            return_obj = del_template
                            return return_obj, top_left, bottom_right
                    return return_obj, None, None

                keep_rotating = True

                # Move the mouse to the x, y position
                x, y = get_random_point_within_rectangle(plus_top_left, plus_bottom_right)
                autohotpy.moveMouseToPosition(x, y)
                time.sleep(0.15) # Small delay to ensure the mouse has time to move
                while keep_rotating:
                    screenshot = capture_screenshot_to_cv2()
                    macro_img, macro_top_left, macro_bottom_right = self.getMacroDetectionImage(screenshot,
                                                                                                top_left)
                    template, tp_left, bt_right = matchWindow()
                    if template is not None:
                        print(f"Found template {template}")

                        if template == "0.png":
                            # Success_case click del and enter code
                            #first click del
                            screenshot = capture_screenshot_to_cv2()
                            del_img_locations, template_width, template_height = match_template(screenshot, cv2.imread(template))
                            for loc in zip(*del_img_locations[::-1]):
                                top_left = loc
                                bottom_right = (top_left[0] + template_width, top_left[1] + template_height)

                            x, y = get_random_point_within_rectangle(top_left, bottom_right)
                            autohotpy.moveMouseToPosition(x, y)
                            time.sleep(0.15)  # Small delay to ensure the mouse has time to move
                            leftButton(autohotpy, event)
                            autohotpy.S.press()
                            #then enter number
                            for num in number_to_enter:
                                template_to_detect = number_template_dict[int(num)]
                                screenshot = capture_screenshot_to_cv2()
                                num_locs, num_temp_width, num_temp_height = match_template(screenshot, cv2.imread(template_to_detect))

                                # Draw rectangles around the detected numpad
                                for loc in zip(*num_locs[::-1]):
                                    top_left = loc
                                    bottom_right = (top_left[0] + num_temp_width, top_left[1] + num_temp_height)

                                # If any rectangles are drawn (i.e., numpad is found), save the debug image
                                if num_locs[0].size > 0:
                                    debug_image_path = f"number_{num}_detected_on_numpad.png"
                                    x, y = get_random_point_within_rectangle(top_left, bottom_right)
                                    autohotpy.moveMouseToPosition(x, y)
                                    time.sleep(0.05)  # Small delay to ensure the mouse has time to move
                                    leftButton(autohotpy, event)
                                    autohotpy.S.press()

                            x, y = get_random_point_within_rectangle(continue_top_left, continue_bottom_right)
                            autohotpy.moveMouseToPosition(x, y)
                            time.sleep(0.05)  # Small delay to ensure the mouse has time to move
                            leftButton(autohotpy, event)
                            autohotpy.S.press()
                            return True
                        else:
                            offset_angle = int(template.split(".")[0])
                            if offset_angle < 0:
                                # press MINUS sign
                                print("# press MINUS sign")
                                x, y = get_random_point_within_rectangle(minus_top_left, minus_bottom_right)
                                autohotpy.moveMouseToPosition(x, y)
                                time.sleep(0.15)
                            elif offset_angle > 0:
                                # press() PLUS sign
                                print("# press() PLUS sign")
                                x, y = get_random_point_within_rectangle(plus_top_left, plus_bottom_right)
                                autohotpy.moveMouseToPosition(x, y)
                                time.sleep(0.05)
                            time.sleep(0.05)
                            leftButton(autohotpy, event)
                            autohotpy.S.press()
                    else:
                        time.sleep(0.05)
                        leftButton(autohotpy, event)




        else:
            return False

    #def handleCaptchaIfExists(self, autohotpy, event) -> bool:
        if self.isCaptchaOnScreen(autohotpy, event):
            # No more captcha, find a mob and click to reactivate Z
            print("No more captcha, find a mob and click to reactivate Z")
            mob_template = "mob_health_bar_template.png"
            mob_image = cv2.imread(mob_template)
            locations = ([],[])

            z_enabled = False
            while not z_enabled:
                screenshot = capture_screenshot_to_cv2()
                locations, w, h = match_template(screenshot, mob_image)
                while len(locations[0]) < 1:
                    screenshot = capture_screenshot_to_cv2()
                    locations, w, h = match_template(screenshot, mob_image)
                    if len(locations[0]) < 1:
                        print("Sending MOUSE MIDDLE BUTTON")
                        stroke = InterceptionMouseStroke()
                        autohotpy.sendToDefaultMouse(stroke)
                        stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MIDDLE_BUTTON_DOWN
                        autohotpy.sendToDefaultMouse(stroke)
                        time.sleep(0.05)
                        stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MIDDLE_BUTTON_UP
                        autohotpy.sendToDefaultMouse(stroke)
                        time.sleep(1.50)

                print("Found mob or mobs on screen trying to click")
                z_enabled = getZEnabled(autohotpy, event)
                if not z_enabled:
                    for loc in zip(*locations[::-1]):
                        top_left = loc
                        bottom_right = (top_left[0] + w, top_left[1] + h)

                        x, y = get_random_point_within_rectangle(top_left, bottom_right)
                        x += 65
                        y += 75

                        autohotpy.moveMouseToPosition(x, y)
                        time.sleep(0.21)
                        leftButton(autohotpy, event)
                        autohotpy.S.press()

                        z_enabled = getZEnabled(autohotpy, event)
                        if z_enabled:
                            break
                z_enabled = getZEnabled(autohotpy, event)
                print(f"Z enabled : {z_enabled}")

            return True
        else:
            return False


#captcha_manager = CaptchaManager()
#last_captcha_control_time = None
#def resolveCaptcha(autohotpy, event):
    global captcha_manager
    global last_captcha_control_time

    execute = False
    if last_captcha_control_time is None:
        last_captcha_control_time = datetime.now()
        print(f"last_captcha_control_time recorded at: {last_captcha_control_time}")
        execute = True
    else:
        if datetime.now() - last_captcha_control_time > timedelta(seconds=10):
            print("10 secs have passed since last_captcha_control_time was recorded.")
            execute = True
            last_captcha_control_time = datetime.now()

    if execute:
        if captcha_manager.handleCaptchaIfExists(autohotpy, event):
            print("Captcha found and handled!")
        else:
            print("No captcha is found!")


def superCombo(autohotpy, event):
    """z2
    This function is called when you press "A" key.
    It executes the combo: A -> S -> move left -> move up -> A -> S
    """
    # mob_name = pressZ(autohotpy)
    #print("Mob name " + mob_name)


    r_started = False
    for i in range(0, 100000):
        if checkMana():
            print("Mana needed!")
            autohotpy.N1.press()

        #getZEnabled(autohotpy,event)
        #resolveCaptcha(autohotpy, event)
        #getCoords(autohotpy, event)
        #partyHealer(autohotpy, event)
        #sprint(autohotpy)


        #selfStr(autohotpy)
        kitap(autohotpy)
        #malice(autohotpy)
        if "" in getZMobName(autohotpy, event):
            helishCombo(autohotpy)
        #getCoords(autohotpy, event)

        #z2rz2rztorment(autohotpy, event)

        #
        if checkHealth():
            print("Health needed!")
            autohotpy.N0.press()
            time.sleep(1.60)



# THIS IS WERE THE PROGRAM STARTS EXECUTING!!!!!!!!
if __name__ == "__main__":
    auto = AutoHotPy()  # Initialize the library
    auto.registerExit(auto.F11, AutoHotPy)  # Registering an end key is mandatory to be able to stop the program gracefully
    auto.registerForKeyDown(auto.F10, superCombo)  # This method lets you say: "when I press A in the keyboard, then execute "superCombo"
    auto.start()  # Now that everything is registered we should start runnin the program
