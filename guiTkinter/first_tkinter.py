# my first program with tkinter (python GUI)
import tkinter as tk

# create new windows (assigned to a_window)
a_window = tk.Tk()

txt = tk.Label(text = "DAYDREAMER, NIGHTTHINKER!") # create text(label) widget
txt.pack() # add text widget to the window

a_window.mainloop()	# loop event
