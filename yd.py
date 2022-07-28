import pyautogui
import time
import mymodules
import webbrowser

webbrowser.open('https://en.y2mate.is/13/')
time.sleep(2)
mymodules._beep()
mymodules._los('start_button.png')
pyautogui.moveTo(int(pyautogui.position()[0]) - 100 , int(pyautogui.position()[1]))
pyautogui.click()
pyautogui.hotkey('ctrl','v')
time.sleep(5)
mymodules._beep()
try:
	mymodules._los('convert_button.png')
except:
	mymodules._beep()
	mymodules._beep()
	mymodules._beep()
	time.sleep(3)
	mymodules._beep()
	mymodules._los('convert_button.png')

time.sleep(1)
pyautogui.click()
time.sleep(5)
pyautogui.click()
time.sleep(2)
pyautogui.hotkey('ctrl','w')
