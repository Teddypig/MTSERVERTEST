# -*- coding: utf-8 -*-
import Tkinter as tk
import os
import time
import subprocess
import signal
import tkMessageBox





def save1():
    pfile = open("./pfile.txt", "w")
    pfile.write(pentry.get())
    pfile.close()
    pwindow.destroy()



if not os.path.exists("./pfile.txt"):
    pwindow = tk.Toplevel()
    pwindow.title("Path")
    plabel = tk.Label(pwindow, text="Path to your Minetest executable")
    pentry = tk.Entry(pwindow)
    pbutton = tk.Button(pwindow, text="save", command=save1)
    plabel.pack(side="left")
    pentry.pack(side="left")
    pbutton.pack(side="left")
    pwindow.mainloop()

with open("./pfile.txt", "rw") as p:
    path = p.readline()





def start():
    global serverprocess
    serverprocess = subprocess.Popen([path])
    print "Server is live!"



def stop():
    global serverprocess
    if serverprocess is not None:
        print "Server Shutting Down"
        serverprocess.send_signal(signal.SIGINT)
        serverprocess = None



def restart():
    global serverprocess
    print "Server Restaring. Takes up to 30 seconds"
    stop()
    serverprocess.wait()
    start()
    serverprocess.wait()
    print "Server Sucessfully Restarted"

def confirm():
    confirm = tk.Toplevel()
    confirm.wm_geometry("400x100")
    confirm.title("Confirm")
    conlabel = tk.Label(confirm, text="Are you sure you want to restart your"
    " server?")
    yes = tk.Button(confirm, text="Yes", command=restart)
    no = tk.Button(confirm, text="no", command=confirm.destroy)
    conlabel.pack()
    yes.pack()
    no.pack()



class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)


    def show(self):
        self.lift()


class Page1(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = tk.Label(self, text="Server Settings")
        label.grid(column=6, row=1, pady=10, padx=10)
        adlabel = tk.Label(self, text="Admin's Name")
        adlabel.grid(column=1, row=2, padx=5)
        admin = tk.Entry(self, justify="center")
        admin.insert(0, "ADMIN")
        admin.grid(column=1, row=3, padx=5)
        portlable = tk.Label(self, text="Server Port")
        portlable.grid(column=1, row=4, padx=5)
        port = tk.Entry(self, justify="center")
        port.insert(0, "30000")
        port.grid(column=1, row=5, padx=5)
        namelabel = tk.Label(self, text="Server Name")
        namelabel.grid(column=1, row=6, padx=5)
        name = tk.Entry(self, justify="center")
        name.insert(0, "My Minetest Server")
        name.grid(column=1, row=7, padx=5)
        deslabel = tk.Label(self, text="Server Description")
        deslabel.grid(column=2, row=2, padx=5)
        des = tk.Entry(self, justify="center")
        des.insert(0, "Mine Here")
        des.grid(column=2, row=3, padx=5)




class Page2(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = tk.Label(self, text="Physics Settings")
        label.pack(side="top", fill="both", expand=True)


class Page3(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = tk.Label(self, text="Mapgen Settings")
        label.pack(side="top", fill="both", expand=True)

class Page4(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = tk.Label(self, text="Console To Game Chat (This will take a"
        " while)")
        label.pack(side="top", fill="both", expand=False)
        cnlabel = tk.Label(self, text="Console Name")
        cnlabel.pack(side="left")
        cname = tk.Entry(self)
        cname.pack(side="left")
        cnbutton = tk.Button(self, text="Save")
        cnbutton.pack(side="left")
        tex = tk.Text(self)
        tex.config(state="disabled")
        def send():
            tex.config(state="normal")
            tex.insert(tk.END, chat.get() + "\n")
            tex.see(tk.END)
            chat.delete(0, "end")
            tex.config(state="disabled")
        tex.pack()
        chat = tk.Entry(self)
        chat.pack()
        cbutton = tk.Button(self, text="Send", command=send)
        cbutton.pack()
        chat.bind("<Return>", send())

class Page5(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = tk.Label(self, text="Terminal (not yet working)")
        label.pack(side="top", fill="both", expand=True)



class Page6(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = tk.Label(self, text="Server Settings")
        label.pack(side="top", fill="both", expand=True)


class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        p1 = Page1(self)
        p2 = Page2(self)
        p3 = Page3(self)
        p4 = Page4(self)
        p5 = Page5(self)
        p6 = Page6(self)

        buttonframe = tk.Frame(self)
        container = tk.Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p4.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p5.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p6.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        b1 = tk.Button(buttonframe, text="Server", command=lambda: p1.lift())
        b2 = tk.Button(buttonframe, text="Physics", command=lambda: p2.lift())
        b3 = tk.Button(buttonframe, text="Mapgen", command=lambda: p3.lift())
        b4 = tk.Button(buttonframe, text="Chat", command=lambda: p4.lift())
        b5 = tk.Button(buttonframe, text="Terminal", command=lambda: p5.lift())
        b6 = tk.Button(buttonframe, text="New", command=lambda: p6.lift())
        startbutton = tk.Button(self, text="Start", command=start)
        rsbutton = tk.Button(self, text="Restart", command=confirm)
        stopbutton = tk.Button(self, text="Shutdown", command=stop)

        b1.pack(side="left")
        b2.pack(side="left")
        b3.pack(side="left")
        b4.pack(side="left")
        b5.pack(side="left")
        b6.pack(side="left")
        startbutton.pack(side="right")
        rsbutton.pack(side="right")
        stopbutton.pack(side="right")

        p1.show()


if __name__ == "__main__":
    root = tk.Tk()
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.title("Minetest Server GUI")
    root.wm_geometry("900x900")
    root.mainloop()
