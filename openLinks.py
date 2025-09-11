import os
import webbrowser

def OpenLogFile():
	LogFileLocation = "logs.log"
	os.startfile(LogFileLocation)

def OpenGitHubLink():
	webbrowser.open('https://github.com/koirdev/Shirraria', new=0)

def	OpenDebugLinkLocal():
	webbrowser.open('http://localhost:8000/#debug', new=0)