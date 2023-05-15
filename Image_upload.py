# DO NOT MODIFY THE CODE
from tkinter import *
from tkinter import ttk
import tkinter as tk
import tkinter.font as tkFont
from tkinter import filedialog
import os, shutil
import PIL.Image
import webbrowser

def submit():
    img = e1.get()
    if e1.get()[-3:] == 'png':
        image = PIL.Image.open(img, 'r')
        data = ''
        imgdata = iter(image.getdata())
        while (True):
                pixels = [value for value in imgdata.__next__()[:3] + imgdata.__next__()[:3] + imgdata.__next__()[:3]]
                binstr = ''
                for i in pixels[:8]:
                    if (i % 2 == 0):
                        binstr += '0'
                    else:
                        binstr += '1'            
                data += chr(int(binstr, 2))
                if (pixels[-1] % 2 != 0):
                        print(data)
                        if(len(data)!=84):
                            print(data)
                            tk.Label(master,text="Method is correct but you are not in the correct place. Think !",fg='#ff0000',bg = '#0ff0fc').grid(row=7,column=0)
                            break
                        e3 = tk.Label(master,text = data,fg = '#015efe',bg='#fbff00')
                        e3.grid(row=5,column=0)
                        e3.bind("<Button-1>", lambda e: webbrowser.open_new_tab(data))
                        tk.Label(master, text="Welcome to Round 3, you have been given a task already, complete it to go to the next round. All the best on your quest",fg='#ff0000',bg='#0ff0fc').grid(row=7,column=0)
                        break
    else:
        tk.Label(master,text="You are doing the right thing but using the wrong thing",fg='#ffffff',bg = '#000000').grid(row=7,column=0)
        
master = tk.Tk()
master.configure(bg='#9b3dd1')
master.title("WELCOME TO IoTHINC VIT Chennai -> ROUND-3")
tk.Label(master, text="Uhh... Ohh Seems like you are in the wrong portal. Seems like you got misguided. Look out for more clues and possibly then you might get through ??? Hopefully !!!",bg='#5e007d',fg='#ffffff').grid(row=0,column=0)

e1 = tk.Entry(master,width = 100)
e1.grid(row=0, column=1)

tk.Button(master, 
          text='SUBMIT', 
          command=submit,bg='#e197f7').grid(row=3, column=0, sticky=tk.W,pady=4)

tk.mainloop()
