import pygame
import sys
from config import WARNING_MESSAGE
from PyQt5.QtWidgets import QMessageBox, QApplication, QPushButton



if WARNING_MESSAGE == 1:
	app = QApplication([])
	msg = QMessageBox()
	msg.setIcon(QMessageBox.Warning)
	msg.setText("This build is unstable!")
	msg.setWindowTitle("Warning!")
	msg.show()
	app.exec()


def WindowModeError():
	app = QApplication([])
	msg = QMessageBox()
	msg.setIcon(QMessageBox.Critical)
	msg.setText("Window mode is wrong!")
	msg.setWindowTitle("ERROR")
	msg.show()
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

def MainCoreInitError():
	app = QApplication([])
	msg = QMessageBox()
	msg.setIcon(QMessageBox.Critical)
	msg.setText("Game initialization failed")
	msg.setWindowTitle("Main core initialization error")
	msg.show()
	MainCoreInitErrorLog()
	app.exec()	
	
def FileCorruptionErrorMSG():
	app = QApplication([])
	msg = QMessageBox()
	msg.setIcon(QMessageBox.Critical)
	msg.setText("File corruption error")
	msg.setWindowTitle("Loading Error")
	msg.show()
	InitErrorLog()
	app.exec()
