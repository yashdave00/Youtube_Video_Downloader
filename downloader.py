import youtube_dl
from tkinter import *  

ydl_opts = {} 

global zxt
def dwl_vid():
	global zxt
	with youtube_dl.YoutubeDL(ydl_opts) as ydl:
		ydl.download([zxt])
channel = 1
def makeUI():
	top = Tk()  
	top.geometry("400x250")  
	top.configure(bg="mediumslateblue")
	name = Label(top, text = "Paste the Link here:",bg='salmon1').place(x = 30,y = 50)
	link = StringVar()  
	e1 = Entry(top,textvariable=link) 
	e1.place(x = 170, y = 50)
	def sub():
		dwl_vid()
	def save():
		global zxt
		lnk=link.get()
		zxt=lnk.strip()

	sbmitbtn = Button(top, text = "Submit",bg='salmon1',activebackground = "pink", activeforeground = "blue",command=sub)
	sbmitbtn.place(x = 30, y = 170)

	savebtn = Button(top, text = "Save",bg='salmon1',activebackground = "pink", activeforeground = "blue",command=save)
	savebtn.place(x = 30, y = 130)    
	top.mainloop()
	


makeUI()