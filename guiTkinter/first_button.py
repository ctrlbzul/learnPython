import tkinter as tk

window = tk.Tk()
# a text label
txt = tk.Label(
	text = "WATCH THE BUTTON!",
	width = 22,
	bg = "gold")
txt.pack()
# a clickable button
btn = tk.Button(
	text = "A Button",
	bg = "#eaeaea",
	height = 1
)
btn.pack()
# user input
user_input = tk.Entry()
user_input.pack()

window.mainloop()