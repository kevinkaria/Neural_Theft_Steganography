from base64 import encode
from cProfile import label
import os
from tkinter import *
from turtle import back, goto, home, width
from tkinter.filedialog import *
from urllib import response
from PIL import ImageTk,Image
from anyio import open_file
from click import command
from isort import file
from stegano import exifHeader as stg
from tkinter import messagebox

from sympy import symbols

global main
global enc

enc = None

def mainfunc():
	global main
	global enc

	if enc != None:
		enc.destroy()

	main=Tk()
	main.title("SDS 1.0")
	main.geometry("250x550+300+150")
	main.backGroundImage = PhotoImage(file = "D:\Darsh\Coding\Python\Steganography\cypher.png")
	main.backGroundImageLabel = Label(main, image = main.backGroundImage)
	main.backGroundImageLabel.place(x=0,y=0)

	encodeb=Button(text="Encode",command=encode)
	encodeb.place(relx=0.35,rely=0.40,height=40,width=80)

	decodeb=Button(text="Decode",command=decode)
	decodeb.place(relx=0.35,rely=0.65,height=40,width=80)

	main.mainloop()

def encode():
		global main
		global enc

		main.destroy()
		
		enc=Tk()
		enc.title("ECS")
		enc.geometry("250x550+300+150")
		enc.backGroundImage = PhotoImage(file = "D:\Darsh\Coding\Python\Steganography\cypher.png")
		enc.backGroundImageLabel = Label(enc, image = enc.backGroundImage)
		enc.backGroundImageLabel.place(x=0,y=0)
		backbutton = Button(text = "Back", command=mainfunc)
		backbutton.place(relx=0.02,rely=0.02)

		label1=Label(text="Message:")
		label1.place(relx=0.05,rely=0.1,height=20,width=100)

		entry=Entry()
		entry.place(relx=0.4,rely=0.1)

		# label2=Label(text="Choose File:")
		# label2.place(relx=0.05,rely=0.2,height=20,width=100)

		# entrysave=Entry()
		# entrysave.place(relx=0.4,rely=0.2)

		def openfile():
			global fileopen
			fileopen=StringVar()
			fileopen=askopenfilename(initialdir=os.getcwd(),title="Select File",filetypes=(("jpeg,png files","*jpg *png"),("all files","*.*")))
		
			label3=Label(text=fileopen)
			label3.place(relx=0.05,rely=0.3)

		def encode1():
			response=messagebox.askyesno("Encode","Encode?")
			if response==1:
				stg.hide(fileopen,fileopen[:-4]+'_encoded.jpg',entry.get())
				messagebox.showinfo("Pop Up","Encoded!")	

			else:
				messagebox.showwarning("Error","Could Not Encode!")
		buttonselect=Button(text="Select File",command=openfile)
		buttonselect.place(relx=0.37,rely=0.4)

		buttonencode=Button(text="Encode",command=encode1)
		buttonencode.place(relx=0.4,rely=0.5)

def decode():
		global main
		global enc

		main.destroy()

		enc=Tk()
		enc.title("DCS")
		enc.geometry("250x550+300+150")
		enc.backGroundImage = PhotoImage(file = "D:\Darsh\Coding\Python\Steganography\cypher.png")
		enc.backGroundImageLabel = Label(enc, image = enc.backGroundImage)
		enc.backGroundImageLabel.place(x=0,y=0)
		backbutton = Button(text = "Back", command=mainfunc)
		backbutton.place(relx=0.02,rely=0.02)

		def openfile():
			global fileopen
			fileopen=StringVar()
			fileopen=askopenfilename(initialdir=os.getcwd(),title="Select File",filetypes=(("jpeg,png files","*jpg *png"),("all files","*.*")))
		
		def decode1():
			message=stg.reveal(fileopen)
			label4=Label(text=message)
			label4.place(relx=0.43,rely=0.7)
		buttonselect=Button(text="Select File",command=openfile)
		buttonselect.place(relx=0.37,rely=0.3)

		buttonencode=Button(text="Decode",command=decode1)
		buttonencode.place(relx=0.4,rely=0.5)

mainfunc()