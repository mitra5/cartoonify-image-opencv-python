import cv2
import easygui
import numpy as np
import imageio
import sys
import matplotlib.pyplot as plt
import os
import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image

top = tk.Tk()
top.geometry('400x400')
top.title('Cartoonify your image!')
top.configure(background='white')
label = Label(top, background='#CDCDCD', font=('calibri', 20, 'bold'))


def upload():
    ImagePath = easygui.fileopenbox()
    cartoonify(ImagePath)

def cartoonify(ImagePath):
    originalimg = cv2.imread(ImagePath)

    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    if originalimg is None:
        print('can not find any image.')
        sys.exit()

    # converting an image to grayscale
    grayScaleImage = cv2.cvtColor(originalimg, cv2.COLOR_BGR2GRAY)
    #faces = face_cascade.detectMultiScale(grayScaleImage, 1.08, 5)
    faces = face_cascade.detectMultiScale(grayScaleImage, 1.2, 5)
    for(x, y, w, h) in faces:
        cv2.rectangle(originalimg, (x, y), (x+w, y+h), (255, 0, 0), 2)
    cv2.imshow('img', originalimg)


    save1 = Button(top, text="Save cartoon image", command=lambda: save(originalimg, ImagePath), padx=30, pady=5)
    save1.configure(background='#364156', foreground='white', font=('calibri', 10, 'bold'))
    save1.pack(side=TOP, pady=50)

    plt.show()


def save(ReSized6, ImagePath):
    # saving an image using imwrite()
    newName = "cartoonified_Image"
    path1 = os.path.dirname(ImagePath)
    extension = os.path.splitext(ImagePath)[1]
    path = os.path.join(path1, newName + extension)
    cv2.imwrite(path, cv2.cvtColor(ReSized6, cv2.COLOR_RGB2BGR))
    I = "Image saved by name " + newName + " at " + path
    tk.messagebox.showinfo(title=None, message=I)


upload = Button(top, text="Cartoonify an Image", command=upload, padx=10, pady=5)
upload.configure(background='#364156', foreground='white', font=('calibri', 10, 'bold'))
upload.pack(side=TOP, pady=50)

top.mainloop()

