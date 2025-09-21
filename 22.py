import tkinter as tk

root = tk.Tk()
root.title("Pack Example")

# Create three buttons
button1 = tk.Button(root, text="Button 1")
button2 = tk.Button(root, text="Button 2")
button3 = tk.Button(root, text="Button 3")
button4 = tk.Button(root, text="Button 4")
button5 = tk.Button(root, text="Button 5")
button6 = tk.Button(root, text="Button 6")

# Pack the buttons vertically
button1.pack()
button2.pack()
button3.pack()
button4.pack()
button5.pack()
button6.pack()

root.mainloop()