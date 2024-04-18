from tkinter import *
from tkinter import Scale
from PIL import Image, ImageTk
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
import webbrowser
import subprocess

root=Tk() 
root.title('Enter here')
root.geometry('500x500')

noiDung = tk.Entry(root)
noiDung.place(x=100, y=350, width=400, height=40)
noiDung.pack()

def get_text():
  text=noiDung.get()
  print('NỘI DUNG NHẬP: ', text)

def show_text():
    Input = noiDung.get()
    lb_hello=Label (root, font=("Arial", 20), text=Input)
    lb_hello.place(x = 100, y = 100, width= 400, height = 40)
    
BtNoiDung = Button(root, text= "NỘI DUNG NHẬP", command=show_text, bg= "blue")
BtNoiDung.place(x = 380, y = 200, width= 100, height = 100)

devices = AudioUtilities.GetSpeakers()
interface = devices. Activate (IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volumeControl = cast (interface, POINTER (IAudioEndpointVolume))

def upVolume(value):
    volumeLevel = float(value) / 100
    volumeControl.SetMasterVolumeLevelScalar(volumeLevel, None)
    
volumeSlider = Scale (root, from_=0, to=100, orient=tk.HORIZONTAL, label="Âm lượng", command=upVolume)

currentVolume = volumeControl.GetMasterVolumeLevelScalar()
volumeSlider.set(current_volume*100)


def changeBrightness(value):
    brightness = int(value) / 100

brightnessScale = Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, label="Ánh sáng", command=changeBrightness)
brightnessScale.set(50)
volumeSlider.place (x=600, y=320, width=500, height=100)

def openYoutube():
    url="https://www.facebook.com/profile.php?id=100045750752976"
    webbrowser.open_new(url)

btFb=Button(root,text="Facebook",command=openYoutube, bg="red")
btFb(x=380, y=380, width=100, height=100)

def viewImage():
    image_path = "image.jpg"
    image = Image.open(image_path)
    photo = ImageTk.PhotoImage(image)
    image_window = tk.Toplevel(root)
    image_window.title("Image Viewer")
    label = tk.Label(image_window, image=photo)
    label.image = photo
    
btImage = tk.Button(root, text="Open Image", command=viewImage)
btImage.pack(padx=20, pady=10)
root.mainloop()

