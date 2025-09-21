import tkinter as tk

root = tk.Tk()
root.title("Grid Example")

# Create three labels
label1 = tk.Label(root, text="first name")
label2 = tk.Label(root, text="last name")
label3 = tk.Label(root, text="age")

# Grid the labels in a 2x2 grid
label1.grid(row=0, column=0)
label2.grid(row=1, column=0)
label3.grid(row=2, column=0, columnspan=1)

root.mainloop()