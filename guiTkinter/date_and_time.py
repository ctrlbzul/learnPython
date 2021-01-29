# importing whole module 
from tkinter import *
from tkinter.ttk import *

# importing strftime and datetime functions 
from datetime import datetime
from time import strftime

# create tkinter window
a_window = Tk()
a_window.title('Date and Time')
a_window.configure(bg = '#3498db')

# current date and time
now = datetime.now()
now_date = now.strftime("%d/%m/%Y") 

show_date = Label(
	font = ('helvetica', 40, 'bold'),
	text = (now_date),
	background = "#3498db",
	foreground = "#fff")

# show current date on a_window
show_date.pack(anchor = 'center')

# function to display current time on window
def now_time():
	str_time = strftime("%H:%M:%S %p")
	show_time.config(text = str_time)
	show_time.after(1000, now_time)
  
# generate and show current time
show_time = Label(
	a_window, font = ('helvetica', 40, 'bold'),
	background = "#3498db",
	foreground = "#fff")
	
show_time.pack(anchor = 'center')
now_time()

mainloop()