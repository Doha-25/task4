import tkinter as tk
r = tk.Tk()
r.title('Counting Seconds')
button = tk.Button(r, text='HELLO WORLD', width=25, command=r.destroy)
button.pack()
r.mainloop()