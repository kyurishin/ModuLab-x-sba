from tkinter import*
import tkinter.ttk as ttk

print('running code...')
window = Tk()
window.title("Kyuri's GUI")
window.geometry("550x430")
window.resizable(True, True)

# create labels

label = ttk.Label(window, text= 'Label')
label.grid(column = 0, row = 0)

window.mainloop()
print('complete!')
