import pyscreenshot 

def screen_shot():
	image = pyscreenshot.grab()
	image.show()
	image.save("screenshots/scrsht1.png")