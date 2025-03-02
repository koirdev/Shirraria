import pyautogui
import pygame
import sys
from config import WARNING_MESSAGE
from logs import *
from PyQt5.QtWidgets import QMessageBox, QApplication, QPushButton



if WARNING_MESSAGE == 1:
	MessageStart = 0
	pyautogui.alert("WARNING: Do not distribute build!")
	#pyautogui.alert("making with love!")


def JoystickModeError():
	pygame.quit()
	pyautogui.alert("Edit value 'JOYSTICK_MODE' to '1'")
	exit()


#def WindowModeError():
#	pygame.quit()
#	pyautogui.alert("Window mode is incorrect!")
#	exit()

def WindowModeError():
	app = QApplication([])
	msg = QMessageBox()
	msg.setIcon(QMessageBox.Critical)
	msg.setText("Window mode is wrong!")
	msg.setWindowTitle("ERROR")
	msg.show()
	WinModeErrorLog()
	running = False
	pygame.quit()
	app.exec()

def LevelNotFounded():
	app = QApplication([])
	msg = QMessageBox()
	msg.setIcon(QMessageBox.Critical)
	msg.setText("Level not founded")
	msg.setWindowTitle("Level Error")
	msg.show()
	ErrorLog()
	running = False
	app.exec()

def InitError():
	app = QApplication([])
	msg = QMessageBox()
	msg.setIcon(QMessageBox.Critical)
	msg.setText("Game initialization failed")
	msg.setWindowTitle("Init Error")
	msg.show()
	InitErrorLog()
	app.exec()	
	
