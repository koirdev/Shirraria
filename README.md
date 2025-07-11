# Shirraria

*A non-commercial, open source game written using Python and the Pygame library* 

# Credits
***koirdev*** - _Programmer, Artist_

***VENUX*** - _Tester_

***James BoT*** - _Tester_

***MOTVER*** - _Tester_

# Controls

- Quit from game - '***Q***'
- Back to the Main Menu - '***Backspace***'
- Switch between sections in the Main Menu - '***ARROW UP***' and '***ARROW DOWN***'
- Select section - '***ENTER***' or '***SPACE***'

# Player controls

- Go left - '***Left key***'
- Go right - '***Right key***'
- Run - '***Left shift***'

# For controlling the XBOX 360 gamepad (Not completely)

- Character movement - '***D-PAD***' (Left stick)
- Run - '***X***' button

# Libraries for running the game:

- Pygame (Game library)
- PyAutoGUI (Message boxes)
- PyInstaller (To compile the game)
- PyQt5 (Message boxes)

# Installation:

1: Download [Git](https://git-scm.com)

2: Open terminal and enter this command:

 ```git clone https://github.com/koirdev/Shirraria```

# Compilation:

### To get started, check out the PyInstaller library

https://pyinstaller.org/en/stable/

## Compiling for ***Windows***:

1. Download PyInstaller library using command in "CMD":

    ```pip install pyinstaller```

2. Open "CMD" in the game folder, and enter this command:

      ```pyinstaller --noconsole -F --distpath win_build -n shirraria main.py``` - (*Normal compilation*)
   
      ```pyinstaller -F --distpath win_build -n shirraria main.py``` - (*For debugging* - ***Don't forget to change the*** "```DEBUG_MODE```" ***parameter to "1" in the game's configuration file before compiling***)

If you want to compile the game, you can also use "CMD" files for normal compilation - "_compile_to_exe.cmd_", for debug compilation - "_compile_to_exe_WITH_CONSOLE.cmd_" If you want to remove compiled files then use - "_remove_compiled_files.cmd_"

After that copy the 'assets' folder to the 'win_build' folder and run the "EXE" file

***(WARNING: The game may not work correctly)***

# Shirraria Configuration:

- ```WIDTH, HEIGHT``` - Screen Resolution
- ```FPS``` - Count of frames *(To display the FPS value on the console, change the '```DEBUG_MODE```' value to '1')*
- ```WINDOW_MODE``` - Changes the parameters of the game window  *('0' - Default, '1' - Resizable, '2' - Fullscreen, '3' - Hardware render)*
- ```WARNING_MESSAGE``` - Showing message box "WARNING: This build is unstable"
- ```MUSIC``` - Off and on music
- ```SFX``` - Off and on sound effects (in development)
- ```CURSOR``` - Custom cursor (in development)
- ```TEST_MODE``` - Mode for testers
- ```DEBUG_MODE``` - Debug Mode
- ```SPLASHES``` - Turn random splashes on and off in the main menu
- ```VERSION``` - Game version
- ```WARNING_TEXT``` - Show text "This build is unstable!"
- ```CONTROLS``` - Control device (Keyboard - '1', XBOX 360 gamepad - '2') , 


<!--# All links:

- https://pygame.org
- https://pypi.org/project/pygame
- https://python.org
- https://pypi.org/project/PyAutoGUI
- https://pypi.org/project/pyinstaller
- https://pyinstaller.org/en/stable/
- https://pypi.org/project/PyQt5/
- https://pypi.org/project/pyscreenshot/!-->

# License

Released under [***MIT*** *License*](LICENSE)

# Font licenses

[Open Sans License](assets/fonts/open-sans-license.txt)

[42dotSans License](assets/fonts/42dotSans-license.txt)

# Branches

[Go to '*backup*' branch](https://github.com/koirdev/Shirraria/tree/backup)

[Go to '*dev*' branch (Development builds)](https://github.com/koirdev/Shirraria/tree/dev)


## (**The game is not finished because I am porting it to pygame**)
### ***Thank you for your attention!***
##### *Written with love*


