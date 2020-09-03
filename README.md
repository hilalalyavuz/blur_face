##Blur Faces

This project detects faces and blur faces on what image you want. You can choose a file or folder to process it. In this project, you can process images which has jpg extension. It detects faces on every images but if you want to blur faces you should press the 'b' key of your keyboard. If you need any help about the system, you should press the 'h' key of your keyboard. Also it saves the blurred images with png extension to your computer too. If you make your operations with a folder, you can use 'left and right arrow' keys of the keyboard to change the image.

For execute the project, you should install some of the python packages. These are:

import cv2

import numpy as np

import os

import glob

import urllib.request as urlreq

from tkinter import filedialog

from tkinter import *

from tkinter import messagebox

You can install them  from the command line or your IDE programs's interpreters section.

First of all, when program runs there is a GUI screen appears. You can choose file or folder type for processing. Then you choose the exact file or folder name for the other steps. There is operator(path) function and this function makes all the work on this code. When you choose file/folder, it starts to make it's job and detect faces on the images. If you want to make blur faces, you should press 'b' and if you want to close the blur, you should press 'b' again. If you choose a folder, you can also use left and right arrow keys to change the image. If you press the right arrow key, it will continue with the next image, if you press the left arrow key then it will be back to the past image. If you need any help about the directions, you can press 'h' key. For quit the program, you can press 'q' key.

For using my project, you should use haarcascade_frontalface_default.xml file too, I upload it here but my project already searchs for this file on your computer and if you don't have, It is going to download this file from here automatically.
