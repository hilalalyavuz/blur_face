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
#haarcascade_url = "https://github.com/hilalalyavuz/hilal/blob/master/haarcascade_frontalface_default.xml"

haar_model_url = "https://github.com/opencv/opencv/raw/master/data/haarcascades/"

model_file = 'haarcascade_frontalface_default.xml'
#model_file = 'haarcascade_frontalface_alt.xml'
#model_file = 'haarcascade_frontalface_alt2.xml'
#model_file = 'haarcascade_frontalface_alt_tree.xml'

haar_file = os.path.join(haar_model_url, model_file)

if(model_file in os.listdir(os.curdir)):
    print("File exist.")
else:
    urlreq.urlretrieve(haar_file, model_file)
    print("File downloaded")

face_cascade = cv2.CascadeClassifier(model_file)
def operator(path):
  length = (len(path))
  i = 0
  last_read = -1
  show_blur = False
  cv2.namedWindow("Image")

  face_scale = 1.1
  face_nb = 3

  while i != length and not keyboard.is_pressed('q'):

     if last_read != i:
         last_read = i

         img = cv2.imread(path[i])
         #Check if we read image successfully
         if not img:
             print("Cannot open image: ", path[i])
             quit(-1)

         height, width = img.shape[:2]
         imResize = cv2.resize(img,(700, (int)((700.0/width)*height)))
         names = np.array(path[i].split("/"))
         imBlur = np.copy(imResize)
         gray = cv2.cvtColor(imResize, cv2.COLOR_BGR2GRAY)
         #faces = face_cascade.detectMultiScale(gray, 1.1, 1)
         print("Detecting faces with ", face_scale, " " , face_nb, " parameters")
         faces = face_cascade.detectMultiScale(gray, face_scale, face_nb)
         for (x,y,w,h) in faces:
             cv2.rectangle(imResize,(x,y),(x+w,y+h),(255,0,0),2)

             # x, y, w, h = [ v for v in f ]
             sub_face = imResize[y:y + h, x:x + w]
             sub_face = cv2.GaussianBlur(sub_face, (23, 23), 30)
             imBlur[y:y + sub_face.shape[0], x:x + sub_face.shape[1]] = sub_face



         #cv2.imshow('{}'.format(names[-1]),imResize)

     if not show_blur:
         cv2.imshow("Image", imResize)
     else:
         cv2.imshow("Image", imBlur)

     k = cv2.waitKey()

     if k == 27:
         cv2.destroyAllWindows()

     #Blur Switch
     if keyboard.is_pressed('b'):
         show_blur = not show_blur

     #Save blurred image
     if keyboard.is_pressed('s'):
         cv2.imwrite("./image{}_blur.png".format(i), imBlur)

     if keyboard.is_pressed('right'):
         print('you pressed right')
         i = (i + 1) % length
         show_blur = False
         #cv2.destroyAllWindows()
         continue
         print(i)

     if keyboard.is_pressed('left'):
         print('you pressed left')
         i = (i - 1) % length
         show_blur = False
         #cv2.destroyAllWindows()
         continue
         print(i)

     if keyboard.is_pressed('up'):
         face_scale += 0.005
         last_read = -1

     if keyboard.is_pressed('down'):
         face_scale -= 0.005
         face_scale = np.max([face_scale, 1.01])
         last_read = -1

     if keyboard.is_pressed('e'):
         face_nb += 1
         last_read = -1
     if keyboard.is_pressed('d'):
         face_nb -= 1
         last_read = -1


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
root.geometry("450x150")
button2 = Button(text="Open File", command=lambda:[open_file(),root.destroy],height=10,width=20,activebackground="red")
button2.grid(row=100,column = 100)
button3 = Button(text="Open Folder", command=lambda:[open_folder(),root.destroy],height=10,width=20,activebackground="red")
button3.grid(row=100, column=120)
button4 = Button(text="Quit", command=lambda:[quit(),root.destroy], height =10, width=20,activebackground="red")
button4.grid(row=100,column=180)
mainloop()








