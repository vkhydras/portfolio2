from pygame import mixer
from tkinter import *
from tkinter import filedialog
import tkinter.font as font

root=Tk()
root.title ('DataFlair Python MP3 Music Player App')

mixer.init()

songs_list=Listbox(root, selectmode=SINGLE,bg ='black', fg="white", font=('arial',15),height=12,width=47,selectbackground='gray',selectforeground='black')
songs_list.grid(columnspan=9)

defined_font= font.Font(family="Helvetica")

play_button=Button(root,text="Play",width=7,command=Place )
play_button['font']=defined_font
play_button.grid(row=1,column=0)

pause_button=Button(root,text="Pause",width=7, command=Place)
pause_button['font']= defined_font
pause_button.grid(row=1,column=1)

mainloop()