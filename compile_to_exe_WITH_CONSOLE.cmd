
@echo The PyInstaller library was used to build the game
@echo Building to exe file...
@echo Please wait...
pyinstaller -F --distpath win_build -n shirraria main.py
@echo Done
pause