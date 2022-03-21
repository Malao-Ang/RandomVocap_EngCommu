import random
import tkinter as tk
import json
import sys
from tkinter import messagebox  
from tkinter import *
import time

v = open('vocap.json')
data = json.load(v)
t = data["Vocap"]

root = tk.Tk()
root.geometry('400x150')
root.title("Random vocap สู้ชีวิต")


def Ran():
    ranV = random.choice(t)
    messagebox.showinfo("Your Vocap",ranV)  



def startCountdown():
	try:
		userinput = (int(minute.get())*60 + int(second.get()))
	except:
		messagebox.showwarning('', 'Invalid Input!')
	while userinput >-1:
		mins,secs = divmod(userinput,60) 

		if mins >60:
			
		
			mins = divmod(mins, 60)
	
		minute.set("{0:2d}".format(mins))
		second.set("{0:2d}".format(secs))

	
		root.update()
		time.sleep(1)

	
		if (userinput == 0):
			messagebox.showinfo("Time's Up", "ชีวิตสู้กลับคุณและคุณแพ้")
		

		userinput -= 1


minute=StringVar()
second=StringVar()
minute.set("00")
second.set("00")

mins_tf= Entry(root, width=3, textvariable=minute).grid(row = 1, column=1,padx=50, pady=10)
sec_tf = Entry(root, width=3, textvariable=second).grid(row = 1, column=2,padx=50, pady=10)
start_btn = Button(root, text='START', command= startCountdown).grid(row = 1, column=3,padx=50, pady=30)
Ranbtn = tk.Button(root, text = "Random", command=Ran).grid(row = 2, column=2)


root.mainloop()
    