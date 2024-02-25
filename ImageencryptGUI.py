from tkinter import *
from tkinter import filedialog
import tkinter as tk
from PIL import Image, ImageTk
import os
from stegano import lsb

root=Tk()
root.title('Image Encryption-Decryption GUI (STEGANOGRAPHY)')
root.geometry("900x600+200+200")
root.resizable(False,False)
root.configure(bg='grey')

def showimg():
    global filename
    filename=filedialog.askopenfilename(initialdir=os.getcwd(),title='Select image file',filetype=(('PNG file','*.png'),('JPG file','*.jpg'),('All file','*.txt')))
    img=Image.open(filename)
    img=ImageTk.PhotoImage(img)
    lbl.configure(image=img,width=280,height=280)
    lbl.image=img

def hideimg():
    global secret
    message=text.get(1.0,END)
    secret = lsb.hide(str(filename),message)

def show():
    clear_message = lsb.reveal(filename)
    text.delete(1.0,END)
    text.insert(END,clear_message)

def save():
    secret.save("hidden.png")

#Name stamp
Label(root,text="-Nikhil Surve-",bg='grey',fg='white', font='tahoma 15' ).place(x=760,y=580, width=150,height=20)
    

#First frame
f=Frame(root,bd=3,bg='navy blue',width=420,height=350,relief=GROOVE)
f.place(x=10,y=80)
lbl=Label(f,bg='navy blue')
lbl.place(x=40,y=10)

#Second frame
f2=Frame(root,bd=3,bg='white',width=420,height=350,relief=GROOVE)
f2.place(x=460,y=80)
text=Text(f2,bg='white',fg='black',font='roboto 15',relief=GROOVE)
text.place(x=0,y=0,width=420,height=350)

#scrollbar1=Scrollbar(f2)
#scrollbar1.place(x=440,y=0,height=350)
#scrollbar1.configure(command=text.yview)
#text.configure(yscrollcommand=scrollbar1.set) 

#Third Frame
f3= Frame(root,bd=3,bg='grey',width=380,height=100,relief=GROOVE)
f3.place(x=10,y=450)
Button(f3,text="Open Image",width=20,height=3,font='roboto 10',command=showimg).place(x=20,y=30)
Button(f3,text="Save Image",width=20,height=3,font='roboto 10',command=save).place(x=180,y=30)
Label(f3,text="Image, Photo file, Picture",bg='grey',fg='black').place(x=20,y=5)

#Fourth Frame
f4=Frame(root,bd=3,bg='grey',width=380,height=100,relief=GROOVE)
f4.place(x=500,y=450)
Button(f4,text="Encrypt",width=20,height=3,font='roboto 10',command=hideimg).place(x=20,y=30)
Button(f4,text="Decrypt",width=20,height=3,font='roboto 10',command=show).place(x=180,y=30)
Label(f4,text="Image, Photo file, Picture",bg='grey',fg='black').place(x=20,y=5)



root.mainloop()