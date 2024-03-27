
#!/usr/bin/env python3
"""
__authors__    = ["Blaze Sanders"]
__contact__    = "blazes@mfc.us"
__copyright__  = "Copyright 2023"
__license__    = "MIT License"
__status__     = "Development"
__deprecated__ = "False"
__version__    = "0.0.1"
__doc__        = "Generate QR code with simple interger vales for asset tracking"
"""

# Disable PyLint linting messages that seem unuseful
# https://pypi.org/project/pylint/
# pylint: disable=invalid-name
# pylint: disable=global-statement

# Installed using "pip install qrcode"
# https://pypi.org/project/qrcode/
import qrcode

# Control MacOS, Windows, or Linux GUI to automate tasks
# https://pyautogui.readthedocs.io/en/latest/index.html
import pyautogui

# Pause program
# https://realpython.com/python-sleep/
from time import sleep


# Static location of GUI elements as defined at https://github.com/mammothfactory/QR-Code-Generator-Asset-Tracking/SETUP.png
SAFARI_URL = 1300, 65
GITHUB_SEARCH_BOX = 1450, 225
SIDE_CLICK_AREA =  120, 300
DEBUG_STATEMENTS_ON = True

def generate_int_qr_codes(qty: int, startInt: int = 0) -> None:
    # Serial number from 0 to 1,0000,000 for OpenBOM part numbers 100-00001 where 100 to 900
    for qrCodeSerialNumber in range(startInt, qty):
        img = qrcode.make(qrCodeSerialNumber)
        type(img)  # The type is "qrcode.image.pil.PilImage"
        img.save(f"images/{qrCodeSerialNumber}_SerialNumber.png")
        if qrCodeSerialNumber % 10000 == 0: print(f"{qrCodeSerialNumber/10000} * 10K QR codes generated!")


# TODO
def convert_to_moe_build_part_number_qr_code(qrCodeSerialNumber: int, prefix: int, maxItemNumber: int, maxVerisonNumber: int) -> None:
    # Moe Build LLC part numbers from 100-00001-1 to 999-99999-99 for OpenBOM cross reference
    for i in range(prefix, prefix+100):
        for j in range(maxItemNumber+1):
            for k in range(maxVerisonNumber+1):
                partNumberString = str(i)+ "-" + str(j) + "-" + str(k)
                img = qrcode.make(partNumberString)
                type(img)  # The type is "qrcode.image.pil.PilImage"
                img.save(f"{partNumberString}_MoeBuildPartNumber.png")
                if j % 1000 == 0: print(f"{j} QR codes generated!")   # Every 1K QR code print progress to standard out


def layout_pictures_in_microsoft_word(firstImageFilename: str, shortSideQty: int = 3, longSideQty: int = 4) -> None:
    pass # Similar to def layout_pictures_in_apple_pages(firstImageFilename: str, shortSideQty: int = 3, longSideQty: int = 4) -> None:


def layout_pictures_in_apple_pages(firstImageFilename: str, shortSideQty: int = 3, longSideQty: int = 4) -> None:

    screenWidth, screenHeight = pyautogui.size() # Get the size of the primary monitor.
    print("Pausing program for 5 seconds")
    print(f"Screen Size: {(screenWidth, screenHeight)}")
    print(f"Laying out {shortSideQty * longSideQty} images")
    print("MAKE SURE *** NO *** EXTERNAL MONITORS ARE PLUGGED INTO BLAZE'S 16 INCH M2 MACBOOK PRO (SERIAL NUMBER J2J3JKDHJG) SET TO 1728 x  1117 RESOLUTION")
    print("Please configure screen layout (Apple Pages on left half of screen, private Safari window on right top half of screen, and terminal on right bottom half of screen)")
    sleep(5)

    numberOfStickersPerSheet = shortSideQty * longSideQty
    imageFilenames = create_image_filenames(firstImageFilename, numberOfStickersPerSheet)
    if DEBUG_STATEMENTS_ON: print(f"The create_image_filenames() function created and returned: {imageFilenames}")
    for boxNumber in range(numberOfStickersPerSheet):
        # Starts with box number zero
        open_github_repo_folder()
        search_repo_click_first_result(imageFilenames[boxNumber])
        #copy_image()
        #select_box_and_highlight_text(boxNumber)
        #Might not need if paste_images works as expected   resize_image_with_shift_drag()
        #paste_image(imageFilenames[boxNumber])

    duplicate_template()


def duplicate_template() -> None:
    pyautogui.click(200, 80)  # Move the mouse to XY coordinates and click it.


def create_image_filenames(filename: str, qty: int) -> list:
    # Find leading digits in a filename
    parts = filename.split('_')
    # Serial number from 0 to 1,0000,000 for OpenBOM part numbers 100-00001 where 100 to 900
    resultsList = [filename]
    for nextQrCodeSerialNumber in range(int(parts[0]) + 1, qty):
        resultsList.append(str(nextQrCodeSerialNumber) + "_" + parts[1])

    return resultsList


def open_github_repo_folder() -> None:
    pyautogui.click(SAFARI_URL)   # Move the mouse to XY coordinate of URL bar in new Safari window and click
    pyautogui.write("https://github.com/mammothfactory/QR-Codes-V2/?search=1", interval=0.010)
    pyautogui.press("enter")


def search_repo_click_first_result(filename: str) -> None:
    pyautogui.click(GITHUB_SEARCH_BOX)   # Move the mouse to XY coordinate of repo searchbox and click
    pyautogui.write(filename, interval=0.010)
    pyautogui.press("enter")


def resize_image_with_shift_drag() -> None: #TODO Might not need if paste_images works
    # Shift key is released automatically
    with pyautogui.hold('shift'):  # Press the Shift key down and hold it.
        pyautogui.press(['down', 'down', 'down', 'down'])  # Press the down arrow key 4 times.



def copy_image(filename: str) -> list:
    pass #TODO


def paste_image(filename: str) -> None:
    pass #TODO


def select_box_and_highlight_text(boxNumber: int) -> None :
    """ Box numbers start in the upper left and increase by 1 to right and going down

    """
    pyautogui.move(400, 0)          # Move mouse to center of box
    pyautogui.doubleClick()         # Double click the mouse.
    pyautogui.hotkey('ctrl', 'a')   # Press the Ctrl-A hotkey combination to select all the text in a template textbox


if __name__ == "__main__":
    generate_int_qr_codes(1000, 0)   # TODO Change this to generate_int_qr_codes(10000, 0) once code is polished

    image = "0_SerialNumber.png"

    # Pause 0.5 seconds after every command to give website on slow internet time to load
    pyautogui.PAUSE = 0.5

    # Moving the mouse to the upper-left will raise a pyautogui.FailSafeException and abort the program
    pyautogui.FAILSAFE = True

    # Start placing QR codes into a Apple Pages document from image files in oiut MFC GitHub repo
    #TODO REMOVE AFTE TESTING VLADS CODE layout_pictures_in_apple_pages(image, shortSideQty=3, longSideQty=4)

    # TODO Useful anywhere? pyautogui.click('button.png') # Find where button.png appears on the screen and click it.
    # TODO Back up Barcode font https://www.dafont.com/barcode-font.font if this QR code thing fails :)
