import tkinter as tk
from tkinter import filedialog, simpledialog
import ttkbootstrap as tkb
from ttkbootstrap.constants import *
import io
from PIL import Image, ImageTk
import requests
import os
from io import BytesIO
import time

#For Image plaace holder refer to 
# https://picsum.photos/   https://placehold.co/
# Using external downloadm3u8 command lline 
#/Library/Frameworks/Python.framework/Versions/3.10/bin/downloadm3u8

### MAIN WINDOW SECTION ###
root = tkb.Window(themename="litera")
root.title("Series Downloader")
root.iconbitmap('icon.ico')
root.geometry('545x635')

# colors Default, primary, secondary, success, info,
# warning, danger, light, dark
num = 0
eps = 0
title = ''
idname = ''
description = ''
#----Title Section------
lb_title = tkb.Label(text="Anime Series Donwloader",
                     font=('Calibri', 24), 
                     bootstyle="success")
lb_title.grid(row=0,column=0, columnspan=5)
lb_seprator = tkb.Separator(bootstyle="light")
lb_seprator.grid(row=1,column=2,pady=15)
#----Entry  id section------
lb_entry = tkb.Label(text="Paste here the Anime id from GoGoAnime",
                     font=('Calibri', 14), 
                     bootstyle="warning")
lb_entry.grid(row=2,column=1, columnspan=3)
myidx = tk.StringVar()
entry_id = tkb.Entry(bootstyle="primary",
                     width=40,
                     textvariable=myidx)
entry_id.grid(row=3,column=1, columnspan=3,pady=8)

def getInfo():
    global myidx
    global title
    global eps
    global idname
    global description
    global poster
    global poster_image
    print(f"Info about the anime serie {myidx.get()}")
    url = f"https://api.consumet.org/anime/gogoanime/info/{myidx.get()}"
    response = requests.get(url)
    info = response.json()
    #print(info)
    title =info['title']
    lb_title2.config(text = title)
    eps = info['totalEpisodes']
    idname = info['id']
    description = info['description']
    txt_anime.insert(tk.END,description)
    lb_title3.config(text=f"Total number of episodes: {eps}")
    pb_download.config(maximum=eps)
    poster = info['image']
    print(poster)
    print(info['title'])
    print("---------------")
    print(info['description'])
    print("Total Num of Episodes: "+str(info['totalEpisodes']))
    title = title.replace(' ','_')
    #------Image poster Section-----
    image_url = poster
    response = requests.get(image_url)
    img_data = response.content
    orig_img = Image.open(BytesIO(img_data))
    imready = orig_img.resize((165, 200))
    poster_image = ImageTk.PhotoImage(imready)
    img_lb.config(image=poster_image)

bt_info = tkb.Button(root, text="1.Get Anime Info", 
                command=getInfo, 
                bootstyle=INFO)
bt_info.grid(row=4,column=1)

def get_dir():
   global dest_dir
   dest_dir =  tk.filedialog.askdirectory()
   dwn_info.config(text=f"Destination directory: {dest_dir}",
                   background='darkgrey')
   print(dest_dir)

def one_episode():
  global myepisode
  myepisode = tk.simpledialog.askinteger(title, "Select episode number: ")
  dwn_info.config(text=f"You selected episode number {myepisode}",
                  background='darkgrey')
  print(myepisode)

bt_ep = tkb.Button(root, text="3.Select episode", 
                command=one_episode, 
                bootstyle=DANGER)
bt_ep.grid(row=4,column=3)
bt_dir = tkb.Button(root, text="2.Select Destination", 
                command=get_dir, 
                bootstyle=WARNING)
bt_dir.grid(row=4,column=2)
lb2_seprator = tkb.Separator(bootstyle="light")
lb2_seprator.grid(row=5,column=2,pady=15)
#------Anime Information Section---------
lb_title2 = tkb.Label(text="Anime Information",
                     font=('Calibri', 18), 
                     bootstyle="Primary")
lb_title2.grid(row=6, column=1, columnspan=3)

anime_img =tk.PhotoImage(file='animeposter.png')
img_lb = tkb.Label(image=anime_img)
img_lb.grid(row=7, column=1, columnspan=1)
txt_anime = tkb.Text(font=('Calibri', 11),
                    width=40,
                    height=14,
                    wrap='word')
#txt_anime.insert(tk.END,temp_txt)
txt_anime.grid(row=7, column=2, columnspan=3,padx=10)
lb_title3 = tkb.Label(text=f"Total number of episodes: {eps}",
                     font=('Calibri', 18), 
                     bootstyle="Primary")
lb_title3.grid(row=8, column=1, columnspan=3,pady=4)
#------ProgressBar Section---------
lb_title4 = tkb.Label(text=f"Progress: ",
                     font=('Calibri', 14), 
                     bootstyle="Primary",
                     justify='right')
lb_title4.grid(row=10, column=1,pady=15)
pb_download = tkb.Progressbar(length= 250,
                              maximum= 13,
                              value = num,
                              bootstyle="dark")
pb_download.grid(row=10,column=2, columnspan=2, pady=15)
dwn_info = tkb.Label(bootstyle="light",
                          width=45,
                          background='darkgrey',
                          text="Status messages...")
dwn_info.grid(row=11,column=1, columnspan=4, pady=5)
#column 0 filler
col0 = tkb.Label(text="",width=3)
col0.grid(row=11,column=0)
#column 6 filler
col6 = tkb.Label(text="",width=3)
col6.grid(row=11,column=6)

"""def pb_add():
  global i
  i = i + 1
  pb_download.config(value=i)
  dwn_info.config(text=f"Downloading episode number {i}")
  print(f"Downloading episode number {i}")"""

def one_episode():
  if myepisode in range(1,eps):
    dwn_info.config(text=f"Downloading episode number {myepisode}")
    dwn_info.update()
    url = f"https://api.consumet.org/anime/gogoanime/watch/{idname}-episode-{myepisode}"
    response = requests.get(url, params={"server": "vidstreaming"})
    data = response.json()
    link = data['sources'][0]['url']
    filename=f"{dest_dir}/{title}_ep_{myepisode}.mp4"
    #dwn_info.config(text=f"Downloading episode number {i}")
    f = f'ffmpeg -nostats -loglevel 0 -i {link} -c copy {filename}'
    print(f"executing: {f}")
    with os.popen(f):
       pass
    dwn_info.config(text="Single episode Download completed")
  else:
    dwn_info.config(text=f"This Episode does not exists",
                     background='red')
    dwn_info.update()
  pass

def down_episodes():
  def pb_add(num):
    pb_download.config(value=num)
    dwn_info.config(text=f"Downloading episode number {num}")
    print(f"Downloading episode number {num}")
    print(dwn_info.cget(key='text'))
    dwn_info.update()
  global ep
  #pb_download.config(maximum=eps)
  for ep in range(1,eps+1):
    print(ep)
    pb_add(ep)
    #pb_download.config(value=i)
    url = f"https://api.consumet.org/anime/gogoanime/watch/{idname}-episode-{ep}"
    response = requests.get(url, params={"server": "vidstreaming"})
    data = response.json()
    link = data['sources'][0]['url']
    filename=f"{dest_dir}/{title}_ep_{ep}.mp4"
    #dwn_info.config(text=f"Downloading episode number {i}")
    s = 'downloadm3u8 -o '+filename + ' '+link+' &> /dev/null'
    f = f'ffmpeg -nostats -loglevel 0 -i {link} -c copy {filename}'
    print(f"executing: {f}")
    with os.popen(f):
       pass
  print("completed")
  dwn_info.config(text="Download completed")

b1 = tkb.Button(root, text="Download Anime", 
                command=down_episodes, 
                bootstyle=INFO)
b1.grid(row=9,column=1)
bone = tkb.Button(root, text="Download episode", 
                command=one_episode, 
                bootstyle=DANGER)
bone.grid(row=9,column=2, pady=9)
b2 = tkb.Button(root, text="Close Application", 
                bootstyle=(DARK, OUTLINE), 
                command=root.destroy)
b2.grid(row=9,column=3)




root.mainloop()



######  STUDY NOTES ##########
"""
var1 = IntVar()
var2 = StringVar()

def changer():
  if var1.get() == 1:
    widget.config(..)
  else:
    widget.config(...)

mychk = tbk.Checkbutton(
   bootstyle="primary",
   variable = var1,
   onvalue = 1,
   offvalue = 0,
   command = changer)

#ROUND TOGGLE
myround = tbk.Checkbutton(
   bootstyle="success, round-toggle",
   variable = var1,
   onvalue = 1,
   offvalue = 0,
   command = changer)

#SQUARE TOGGLE
myround = tbk.Checkbutton(
   bootstyle="warning, square-toggle",
   variable = var1,
   onvalue = 1,
   offvalue = 0,
   command = changer)


"""