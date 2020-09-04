import cv2
import numpy as np
import sys
import glob
from tkinter import filedialog
from tkinter import *
from tkinter import messagebox
import urllib.request as urlreq
import os
import keyboard


#author hilalalyavuz
#user selects the file or folder then the program detects faces on the image and blur faces
haarcascade_url = "https://github.com/hilalalyavuz/hilal/blob/master/haarcascade_frontalface_default.xml"
haar_file = 'haarcascade_frontalface_default.xml'
if(haar_file in os.listdir(os.curdir)):
    print("File exist.")
else:
    urlreq.urlretrieve(haarcascade_url, haar_file)
    print("File downloaded")

face_cascade = cv2.CascadeClassifier(haar_file)
def operator(path):
  length = (len(path))
  i = 0
  while i != length and not keyboard.is_pressed('q'):

     img = cv2.imread(path[i])
     imResize = cv2.resize(img,(700,400))
     names = np.array(path[i].split("/"))
     copy_img = np.copy(imResize)
     gray = cv2.cvtColor(imResize, cv2.COLOR_BGR2GRAY)
     faces = face_cascade.detectMultiScale(gray, 1.1, 1)
     for(x,y,w,h) in faces:
          cv2.rectangle(imResize,(x,y),(x+w,y+h),(255,0,0),2)

     cv2.imshow('{}'.format(names[-1]),imResize)
     k = cv2.waitKey()
     if k == 27:
         cv2.destroyAllWindows()
     if k == ord('b'):
          if len(faces) != 0:
                    for f in faces:
                       x, y, w, h = [ v for v in f ]
                       sub_face = imResize[y:y+h, x:x+w]
                       sub_face = cv2.GaussianBlur(sub_face,(23, 23), 30)
                       imResize[y:y+sub_face.shape[0], x:x+sub_face.shape[1]] = sub_face
                       cv2.imwrite("./image{}_blur.png".format(i), imResize)

     cv2.imshow('{}'.format(names[-1]),imResize )
     cv2.waitKey()
     cv2.destroyAllWindows()

     if keyboard.is_pressed('right'):
         print('you pressed right')
         i = i + 1
         continue
         print(i)

     if keyboard.is_pressed('left'):
          print('you pressed left')
          i = i - 1
          continue
          print(i)



     if keyboard.is_pressed('h'):
        top = Tk()
        messagebox.showinfo("help,about","Hilal YAVUZ (c) 2020, Kullanım şekli:İşlem yapmak istediğiniz dosya veya klasörü seçin, program seçilen dosya veya klasördeki resimlerden insan yüzlerini algılar ve yüzleri blurlar")
        top.destroy()




def open_file():
    # Allow user to select a directory and store it in global var
    # called folder_path44
    global folder_path
    filename = filedialog.askopenfilename()
    folder_path.set(filename)
    path = np.array(glob.glob(r"{}".format(filename)))
    root.destroy()
    operator(path)


def open_folder():
    # Allow user to select a directory and store it in global var
    # called folder_path
    global folder_path
    filename = filedialog.askdirectory()
    folder_path.set(filename)
    path = np.array(glob.glob(r"{}/*.jpg".format(filename)))
    root.destroy()
    operator(path)


root = Tk()
folder_path = StringVar()
root.geometry("450x450")
button2 = Button(text="Open File", command=lambda:[open_file(),root.destroy],height=10,width=20,activebackground="red")
button2.grid(row=100,column = 100)
button3 = Button(text="Open Folder", command=lambda:[open_folder(),root.destroy],height=10,width=20,activebackground="red")
button3.grid(row=100, column=180)
button4 = Button(text="Quit", command=lambda:[quit,root.destroy], height =10, width=20,activebackground="red")
button4.grid(row=200,column=120)
mainloop()








