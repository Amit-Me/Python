import pyautogui as pg
import time
time.sleep(10)

for i in range(10):
    pg.write("call")
    pg.press('Enter')