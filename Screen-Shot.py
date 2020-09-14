import time
import pyautogui
import tkinter as tk


def screenshot():
    name = int(round(time.time()) * 1000)
    name = 'D:/Screenshot/{}.png'.format(name)
    time.sleep(5)
    img = pyautogui.screenshot(name)
    img.show()


root = tk.Tk()
root.title('SCREENSHOT')
root.geometry('500x80')
frame = tk.Frame(root)
frame.pack()

button = tk.Button(frame, text='Take Screenshot', command=screenshot)

button.pack()

close = tk.Button(frame, text='Quit', command=quit)

close.pack()

root.mainloop()
