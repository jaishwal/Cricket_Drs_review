'''
Cricket Drs review system
Author = Dheeraj
'''
import tkinter  # in-built module
import cv2    # pip install opencv-python
import PIL.Image , PIL.ImageTk  # pip install pillow
from functools import partial # in-built module
import threading  # in-built module
import imutils # pip install imultils
import time   # in-built module
import pyttsx3 # pip install pywin32

engine = pyttsx3.init('sapi5') # for voice
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id) # voice id 0 for male and 1 for female
stream = cv2.VideoCapture("C:\\Users\\Dheer\\Pictures\\DRS\\sonu2.mp4") # path for video

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def play(speed):
    print(f"you clicked on play. Speed is {speed}")
    # play the vid in reverse mode and forward mode
    frame1 = stream.get(cv2.CAP_PROP_POS_FRAMES) # read frame
    stream.set(cv2.CAP_PROP_POS_FRAMES, frame1 + speed)  # back to normal
    grabbed, frame = stream.read()  # video reading
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)  # resize our pic and vid
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame)) # normal tkinter syntax
    canvas.image = frame
    canvas.create_image(0,0, image=frame, anchor=tkinter.NW) # NW=northwest

def pending(decision):
    # 1. Display decision pending image
    frame = cv2.cvtColor(cv2.imread("C:\\Users\\Dheer\\Pictures\\DRS\\pending.jpg"), cv2.COLOR_BGR2RGB)
    speak("decision is pending, wait a while second")
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0 , 0, image=frame, anchor=tkinter.NW)
    # 2. wait for a second
    time.sleep(1.5)
    # 3. Display sponsor image
    frame = cv2.cvtColor(cv2.imread("C:\\Users\\Dheer\\Pictures\\DRS\\sponseredw.jpg"), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)
    speak("sponsered by sonu traders")
    # 4. wait for 2 sec
    time.sleep(2.5)
    # 5. Display out\ not out
    if decision == "Out":
        decisionImg = "C:\\Users\\Dheer\\Pictures\\DRS\\OUT.jpg"
        speak("Player is out")

    else:
        decisionImg = "C:\\Users\\Dheer\\Pictures\\DRS\\NOT OUT.jpg"
        speak("player is Not out")

    frame = cv2.cvtColor(cv2.imread(decisionImg), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0, image=frame, anchor=tkinter.NW)

# out and not out conditions
def Out():
    thread = threading.Thread(target=pending, args=("Out",))
    thread.daemon = 1
    thread.start()
    print("player is out")

def Not_out():
    thread = threading.Thread(target=pending, args=("Not out",))
    thread.daemon = 1
    thread.start()
    print("player is not out")

# Display height and width
SET_WIDTH = 620
SET_HEIGHT = 368
# welcome screen
window = tkinter.Tk()
window.title("Dheeraj Drs Review System")
speak("Welcome to Dj Review system")
cv_image = cv2.cvtColor(cv2.imread("C:\\Users\\Dheer\\Pictures\\DRS\\welcomedj.jpg"), cv2.COLOR_BGR2RGB)
canvas = tkinter.Canvas(window, width=SET_WIDTH, height=SET_HEIGHT)
photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_image))
image_on_canvas = canvas.create_image(0,0, ancho=tkinter.NW, image=photo)
canvas.pack()
# buttons to control playback
btn = tkinter.Button(window, text="<< Previous(fast)", width=50, command=partial(play,25))
btn.pack()
btn = tkinter.Button(window, text=" Next(fast)>>", width=50, command=partial(play,25))
btn.pack()


btn = tkinter.Button(window, text="<< Previous(slow)", width=50, command=partial(play,-2))
btn.pack()
btn = tkinter.Button(window, text=" Next(slow)>>", width=50, command=partial(play,2))
btn.pack()

btn = tkinter.Button(window, text=" Give not out ", width=50, command= Not_out)
btn.pack()
btn = tkinter.Button(window, text=" Give Out ", width=50, command= Out)
btn.pack()

window.mainloop() # Main loop of software

