def _beep():
	import playsound
	playsound.playsound('beep.wav')

def _los(file):
	import pyautogui
	button = list(pyautogui.locateOnScreen(file))
	button = list(pyautogui.center(tuple(button)))
	pyautogui.moveTo(button[0],button[1])

