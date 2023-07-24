import time
import pyautogui
import tkinter as tk
def screenshot():
    name=int(round(time.time()*1000))
    name="{}.png".format(name)
    time.sleep()
    img=pyautogui.screenshot(name)
    img.show()
root=tk.Tk()
frame=tk.Frame(root)
frame.pack()
button=tk.Button(
    frame,
    command=screenshot,
    text="Take Screenshot"
)
button.pack(side=tk.LEFT)
close=tk.Button(
    frame,
    command=quit,
    text='close'
)
close.pack(side=tk.RIGHT)
tk.mainloop()
    