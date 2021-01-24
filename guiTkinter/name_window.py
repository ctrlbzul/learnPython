import tkinter as tk

while True:
	print("// Show Name //")

	name = str(input("Input a name\t: "))
	txt_color = str(input("Text color (black, white, etc.)\t: "))
	bg_color = str(input("Background color (black, white, etc.)\t: "))

	# empty input = the window will not be shown
	if(name == "" or txt_color == "" or bg_color == ""):
		print("Please fill all the input!")
		break
	else:
		a_window = tk.Tk()

		txt = tk.Label(
			text = name,
			fg = txt_color, # shorthand for "foreground : set text color
			bg = bg_color, # shorthand for "background" : set background color
			width = 10, # label's width
			height = 2 # label's height
			)
		txt.pack()

		a_window.mainloop()

		# program's loop
		again = str(input("\nWanna use program again ? (y/n): "))
		if again == "n" or again == "N" or again != "y":
			break 

	
