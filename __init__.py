# -*- coding: utf-8 -*-
import Tkinter as tk
import os
import sys
import time
import subprocess


os.path.expanduser("~")
path = "~/minetest/bin/minetest"



def start():
    serverprocess = subprocess.Popen(path)
    print "Server is live!"


def kill():
    print "Server Shutting Down"
    serverprocess.send.signal(signal_SIGINT) #as per Donillo's instruction
    time.sleep(10)

def restart():
    print "Server Restaring. Takes up to 30 seconds"
    serverprocess.send.signal(signal_SIGINT) #as per Donillo's instruction
    time.sleep(5)
    serverprocess = subprocess.Popen(path)
    print "Server Sucessfully Restarted"

class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

    def show(self):
        self.lift()


class Page1(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = tk.Label(self, text="This is page 1")
        label.pack(side="top", fill="both", expand=True)


class Page2(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = tk.Label(self, text="This is page 2")
        label.pack(side="top", fill="both", expand=True)


class Page3(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = tk.Label(self, text="Terminal")
        label.pack(side="top", fill="both", expand=True)


class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        p1 = Page1(self)
        p2 = Page2(self)
        p3 = Page3(self)

        buttonframe = tk.Frame(self)
        container = tk.Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        b1 = tk.Button(buttonframe, text="Page 1", command=lambda: p1.lift())
        b2 = tk.Button(buttonframe, text="Page 2", command=lambda: p2.lift())
        b3 = tk.Button(buttonframe, text="Terminal", command=lambda: p3.lift())
        b4 = tk.Button(self, text="Start", command=start)
        b5 = tk.Button(self, text="Restart", command=restart)
        b6 = tk.Button(self, text="Shutdown", command=kill)

        b1.pack(side="left")
        b2.pack(side="left")
        b3.pack(side="left")
        b4.pack(side="right")
        b5.pack(side="right")
        b6.pack(side="right")

        p1.show()

if __name__ == "__main__":
    root = tk.Tk()
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.title("Minetest Server GUI")
    root.wm_geometry("900x900")
    root.mainloop()
