
import os
import keyboard
from selenium import webdriver
from time import sleep
from pynput.mouse import Button, Controller
import pyautogui
import mouse

Mouse = Controller()

driver = webdriver.Chrome(os.getcwd() + '\chromedriver.exe')
#paste link to desired yt channel
driver.get('https://www.youtube.com/channel/UCSYbn1wWN7m_APGza8vyzEQ')
sleep(2)
Mouse.press(Button.left)
Mouse.release(Button.left)
sleep(0.5)
pyautogui.scroll(-750)
sleep(2)

pyautogui.moveTo(989, 606)
mouse.press('left')
mouse.release('left')

sleep(0.5)

pyautogui.moveTo(760, 679)
mouse.press('left')
mouse.release('left')
sleep(0.5)
pyautogui.moveTo(771, 714)
mouse.press('left')
mouse.release('left')

sleep(0.2)
pyautogui.moveTo(984, 29)
mouse.press('left')
mouse.release('left')

sleep(1)
pyautogui.moveTo(896, 661)
sleep(0.5)
mouse.press('left')
mouse.release('left')
sleep(0.4)
pyautogui.moveTo(907, 696)
mouse.press('left')
mouse.release('left')


def newVid():
    #change x and y for desired yt vid
    sleep(1)
    pyautogui.moveTo(896, 661)
    sleep(0.5)
    mouse.press('left')
    mouse.release('left')
    sleep(0.4)
    pyautogui.moveTo(907, 696)
    mouse.press('left')
    mouse.release('left')

counter = 0

#input number of views
while counter < 20:
    newVid()
    counter = counter + 1
