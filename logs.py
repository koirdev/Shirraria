import logging
import subprocess
from config import DEBUG_MODE
logging.basicConfig(level=logging.INFO, filename="logs.txt",filemode="w",format="%(asctime)s %(levelname)s %(message)s")


def WinModeErrorLog():
	if DEBUG_MODE == 1:
		logging.critical("Windows Mode Error")

def InitErrorLog():
	if DEBUG_MODE == 1:
		logging.critical("Initialization Error")

def LevelErrorLog():
	logging.critical("Level not founded")

def OpenLogs():
	programName = "notepad.exe"
	fileName = "logs.txt"
	subprocess.Popen([programName, fileName])



# Example

#logging.debug("A DEBUG Message")
#logging.info("An INFO")
#logging.warning("A WARNING")
#logging.error("An ERROR")
#logging.critical("A message of CRITICAL severity")

