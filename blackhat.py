from Tkinter import *
from PIL import Image
from PIL import ImageTk
import tkFileDialog
import cv2
import numpy as np
 
def select_image():
	# grab a reference to the image panels
	global panelA, panelB
 
	# open a file chooser dialog and allow the user to select an input
	# image
	path = tkFileDialog.askopenfilename()
	# ensure a file path was selected
	if len(path) > 0:
		# load the image from disk, convert it to grayscale, and detect
		# edges in it
		image = cv2.imread(path)
                kernel = np.ones((5,5),np.uint8)
                blackhat = cv2.morphologyEx(image, cv2.MORPH_BLACKHAT, kernel)
 
		# OpenCV represents images in BGR order; however PIL represents
		# images in RGB order, so we need to swap the channels
		image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                blackhat = cv2.cvtColor(blackhat, cv2.COLOR_BGR2RGB) 
		# convert the images to PIL format...
		image = Image.fromarray(image)
		blackhat = Image.fromarray(blackhat)
 
		# ...and then to ImageTk format
		image = ImageTk.PhotoImage(image)
		blackhat = ImageTk.PhotoImage(blackhat)
		# if the panels are None, initialize them
		if panelA is None or panelB is None:
			# the first panel will store our original image
			panelA = Label(image=image)
			panelA.image = image
			panelA.pack(side="left", padx=10, pady=10)
 
			# while the second panel will store the edge map
			panelB = Label(image=blackhat)
			panelB.image = blackhat
			panelB.pack(side="right", padx=10, pady=10)
 
		# otherwise, update the image panels
		else:
			# update the pannels
			panelA.configure(image=image)
			panelB.configure(image=blackhat)
			panelA.image = image
			panelB.image = blackhat
# initialize the window toolkit along with the two image panels
root = Tk()
panelA = None
panelB = None
 
# create a button, then when pressed, will trigger a file chooser
# dialog and allow the user to select an input image; then add the
# button the GUI
btn = Button(root, text="Select an image", command=select_image)
btn.pack(side="bottom", fill="both", expand="yes", padx="10", pady="10")
 
# kick off the GUI
root.mainloop()

