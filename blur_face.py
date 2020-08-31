import cv2
import numpy as np
import sys
import glob
from tkinter import filedialog
from tkinter import *
from tkinter import messagebox

#author hilalalyavuz
#user selects the file or folder then the program detects faces on the image and blur faces
haar_file = 'haarcascade_frontalface_default.xml'
face_cascade = cv2.CascadeClassifier(haar_file)
def operator(path):
    for i in range(len(path)):
     img = cv2.imread(path[i])
     copy_img = np.copy(img)
     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
     faces = face_cascade.detectMultiScale(gray, 1.1, 1)
     for(x,y,w,h) in faces:
          cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

     cv2.imshow('hilal',img)
     k = cv2.waitKey(0)
     if k == 27:
         cv2.destroyAllWindows()
     elif k == ord('b'):
          if len(faces) != 0:
                    for f in faces:
                       x, y, w, h = [ v for v in f ]
                       sub_face = img[y:y+h, x:x+w]
                       sub_face = cv2.GaussianBlur(sub_face,(23, 23), 30)
                       img[y:y+sub_face.shape[0], x:x+sub_face.shape[1]] = sub_face
                       cv2.imwrite("./image{}_blur.png".format(i), img)

     elif k == ord('c'):
         image_edges = cv2.Canny(img,100,200)
         cv2.imwrite("./image_edges.png",image_edges)
     elif k == ord('h'):
            messagebox.showinfo("help,about","Hilal YAVUZ (c) 2020, Kullanım şekli:İşlem yapmak istediğiniz dosya veya klasörü seçin, program seçilen dosya veya klasördeki resimlerden insan yüzlerini algılar ve yüzleri blurlar")

     cv2.imshow('hilal',img)
     cv2.waitKey(0)
     cv2.destroyAllWindows()
     i = i +1

def open_file():
    # Allow user to select a directory and store it in global var
    # called folder_path
    global folder_path
    filename = filedialog.askopenfilename()
    folder_path.set(filename)
    path = np.array(glob.glob(r"{}".format(filename)))
    operator(path)


def open_folder():
    # Allow user to select a directory and store it in global var
    # called folder_path
    global folder_path
    filename = filedialog.askdirectory()
    folder_path.set(filename)
    path = np.array(glob.glob(r"{}/*.jpg".format(filename)))
    operator(path)


root = Tk()
folder_path = StringVar()
button2 = Button(text="Open File", command=open_file)
button2.grid(row=0, column=3)
button3 = Button(text="Open Folder", command=open_folder)
button3.grid(row=0, column=8)
mainloop()







