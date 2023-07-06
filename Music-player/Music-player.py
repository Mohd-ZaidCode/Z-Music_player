import time
from tkinter import *
from tkinter import filedialog
from pygame import mixer
import os


# main Frame Properties
root = Tk()
root.title("Z-Music player MP3")
root.geometry("485x600+290+10")
root.resizable(False,False)
root.configure(background = '#cb6ce6')
mixer.init()

# Function to add music by selecting file
def Addmusic():
    path = filedialog.askdirectory()
    if path:os.chdir(path)
    songs=os.listdir(path)
    
    for song in songs:
        if song.endswith(".mp3"):
            Playlist.insert(END,song) 
            
# Function to play music based on the  selection
def PlayMusic():
    Music_Name = Playlist.get(ACTIVE)
    print(Music_Name[0:-4])
    mixer.music.load(Playlist.get(ACTIVE))
    mixer.music.play(0)
    
# Defining Gif 
frameCnt = 30
frames = [PhotoImage(file='playerBG.gif',format = 'gif -index %i' %(i)) for i in range(frameCnt)]

# Loop to play gif properly
def update(ind):
    frame = frames[ind]
    ind +=1
    if ind == frameCnt:
        ind =0

    label.configure(image= frame)
    root.after(210,update, ind)
    
label = Label(root)
label.place(x=0,y=0)
root.after(0, update, 0)


# menu frame for play pause button
Bottom_frame = Frame(root,bg = "#ffffff",width=485, height = 160)
Bottom_frame.place(x=0,y=370)


# fevicon image
icon_image = PhotoImage(file="fevicon.png")
root.iconphoto(False, icon_image)

# Music list frame propeties are defined here
Menu = PhotoImage(file ="menu_image.png")
Label(root,image = Menu).place(x=0,y=480,width=485,height=120)
Frame_music = Frame(root, bd =2, relief=RIDGE)
Frame_music.place(x=0,y=485,width=485,height=100)

# play button defining the properties 
Buttonplay = PhotoImage(file= "playBtn.png")
Button(root, image= Buttonplay, bg="#ffffff", bd = 0, height = 60,width=60, command= PlayMusic).place(x=215,y=387)


# Stop button properties
ButtonStop= PhotoImage(file= "stop_btn.png")
Button(root,image= ButtonStop,bg="#ffffff", bd = 0, height=60, width=60, command=mixer.music.stop).place(x=130,y=387)

# Pause button properties
ButtonPause= PhotoImage(file= "pause_btn.png")
Button(root,image= ButtonPause,bg="#ffffff", bd = 0, height=60, width=60, command=mixer.music.pause).place(x=300,y=387)

# # Volume Button image properties are not yet been added 
# Volume = PhotoImage(file="volume.png")
# panel = Label(root,image=Volume,bg="black", bd = 0, height=60, width=60).place(x=20, y=350)



#Find song Button
Button(root, text="🔍Find Song",width= 40,height=1, font=("roboto mono", 15, "bold"), fg = "#ffffff", bg = "#5e17eb", command = Addmusic).place(x=0, y = 450)

# Scroll baar  properties definesd here
Scroll = Scrollbar(Frame_music)
Playlist  = Listbox(Frame_music, width= 100,font =("roboto mono", 10),bg = "#ffde59",fg = "black",selectbackground= '#d9d9d9', cursor= "hand2",bd = 0, yscrollcommand=Scroll.set)

# posiition of scroll bar is defined here 
Scroll.config(command = Playlist.yview)
Scroll.pack(side = RIGHT, fill = Y)
Playlist.pack(side = RIGHT, fill = BOTH)

root.mainloop()