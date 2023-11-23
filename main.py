from time import strftime
from  tkinter import *
from tkinter import filedialog
import os 
import time
import datetime
from pygame import mixer

page=Tk()
page.title("Alarm-Clock")

mixer.init()

def AddMusic():
    path=filedialog.askdirectory()
    if path:
        os.chdir(path)
        songs=os.listdir(path)
        
        for song in songs:
            if song.endswith(".mp3"):
                Playlist.insert(END,song)

def PlayMusic():
    MusicName=Playlist.get(ACTIVE)
    print(MusicName[0:-4])
    # mixer.music.load(Playlist.get(ACTIVE))
    mixer.music.load(MusicName)
    mixer.music.play()




def setalarm():
    alarmtime=f"{hrs.get()}:{mins.get()}:{secs.get()}"
    print(alarmtime)
    if(alarmtime!="::"):
        alarmclock(alarmtime)

def alarmclock(alarmtime):
    while True:
        time.sleep(1)
        time_now=datetime.datetime.now().strftime("%H:%M:%S")
        print(time_now)
        if time_now==alarmtime:
            Wakeup=Label(page).grid(row=6,columnspan=3)
            print("wake up!")
            # mixer.music.load(Playlist.get(ACTIVE))
            # mixer.music.play()
            PlayMusic()
            break
        
hrs=StringVar()
mins=StringVar()
secs=StringVar()

Frame_Music=Frame(page,bd=2,relief=RIDGE)
Frame_Music.grid(row=6,columnspan=3)

Button(page,text="Add Music",command=AddMusic,bg="DodgerBlue2",
fg="white",font=('arial',20,"bold")).grid(row=5,columnspan=3)
Scroll=Scrollbar(Frame_Music)
Playlist=Listbox(Frame_Music,width=15,height=2,yscrollcommand=Scroll.set)
Scroll.config(command=Playlist.yview)
Scroll.pack(side=RIGHT,fill=Y)
Playlist.pack(side=LEFT,fill=BOTH)

#set alarm
greet=Label(page,font=('arial',20,'bold'),
text="Take a short nap").grid(row=1,columnspan=3)
hrbtn=Entry(page,textvariable=hrs,width=5,font=('arial',20))
hrbtn.grid(row=2,column=1)

minbtn=Entry(page,textvariable=mins,
width=5,font=('arial', 20, 'bold')).grid(row=2,column=2)

secbtn=Entry(page,textvariable=secs,
width=5,font=('arial', 20, 'bold')).grid(row=2,column=3)

setbtn=Button(page,text="set alarm",command=setalarm,bg="DodgerBlue2",
fg="white",font=('arial',20,"bold")).grid(row=4,columnspan=3)

timeleft=Label(page,font=('arial', 20, 'bold'))
timeleft.grid()

page.geometry('450x450')
page.mainloop()