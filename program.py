import tkinter as tk
from tkinter import *
import re

# Class to inherit
class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()

# Home page
class Page1(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       welcome = tk.Label(self, text="Welcome to Typing-Tutor")
       welcome.pack()

# Middle row
class Page2(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = tk.Label(self, text="asdfghjkl;<space>", font=('arial', 10, 'bold'), bg="Pink")
       label.pack(side="top", fill="both")# ,expand=True
       self.inputfield = tk.Text(self, bg="White")
       self.inputfield.pack(fill="both", expand=True)
       self.inputfield.bind('<Control-v>', lambda _: 'break')
       self.inputfield.bind('<Control-c>', lambda _: 'break')
       self.inputfield.bind('<BackSpace>', lambda _: 'break')
       self.inputfield.bind('<Control-x>', lambda _: 'break')
       self.inputfield.bind('<Control-a>', lambda _: 'break')
       self.bframe = tk.Frame(self)
       self.bframe.pack(side="bottom")
       self.sb = tk.Button(self.bframe, text="Stop", width = 10, height = 2, bd = 0, bg = "#eee", cursor = "hand2", command=self.stopfunction)
       self.sb.pack(side="left")
       self.cb = tk.Button(self.bframe, text="Clear", width = 10, height = 2, bd = 0, bg = "#eee", cursor = "hand2", command=self.clearfunction)
       self.cb.pack(side="left")
       
   def stopfunction(self):
   	   entered_string = self.inputfield.get("1.0",'end-1c')
   	   if entered_string:
   	   	regexx = re.compile(r'asdfghjkl; ')
   	   	p = regexx.findall(entered_string)
   	   	self.inputfield.delete('1.0', 'end')
   	   	self.inputfield.insert('1.0', 'The number of times you entered correctly is %d'%(len(p)))
   	   else:
   	   	self.inputfield.insert('1.0', "you didn't enter anything!")

   def clearfunction(self):
   	   self.inputfield.delete('1.0', 'end')

# Top row
class Page3(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = tk.Label(self, text="qwertyuiop<space>", font=('arial', 10, 'bold'), bg="Pink")
       label.pack(side="top", fill="both")# ,expand=True
       self.inputfield = tk.Text(self, bg="White")
       self.inputfield.pack(fill="both", expand=True)
       self.inputfield.bind('<Control-v>', lambda _: 'break')
       self.inputfield.bind('<Control-c>', lambda _: 'break')
       self.inputfield.bind('<BackSpace>', lambda _: 'break')
       self.inputfield.bind('<Control-x>', lambda _: 'break')
       self.inputfield.bind('<Control-a>', lambda _: 'break')
       self.bframe = tk.Frame(self)
       self.bframe.pack(side="bottom")
       self.sb = tk.Button(self.bframe, text="Stop", width = 10, height = 2, bd = 0, bg = "#eee", cursor = "hand2", command=self.stopfunction)
       self.sb.pack(side="left")
       self.cb = tk.Button(self.bframe, text="Clear", width = 10, height = 2, bd = 0, bg = "#eee", cursor = "hand2", command=self.clearfunction)
       self.cb.pack(side="left")

   def stopfunction(self):
   	   entered_string = self.inputfield.get("1.0",'end-1c')
   	   if entered_string:
   	   	regexx = re.compile(r'qwertyuiop ')
   	   	p = regexx.findall(entered_string)
   	   	self.inputfield.delete('1.0', 'end')
   	   	self.inputfield.insert('1.0', 'The number of times you entered correctly is %d'%(len(p)))
   	   else:
   	   	self.inputfield.insert('1.0', "you didn't enter anything!")

   def clearfunction(self):
   	   self.inputfield.delete('1.0', 'end')

# Bottom row
class Page4(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = tk.Label(self, text="zxcvbnm,./<space>", font=('arial', 10, 'bold'), bg="Pink")
       label.pack(side="top", fill="both")
       self.inputfield = tk.Text(self, bg="White")
       self.inputfield.pack(fill="both", expand=True)
       self.inputfield.bind('<Control-v>', lambda _: 'break')
       self.inputfield.bind('<Control-c>', lambda _: 'break')
       self.inputfield.bind('<BackSpace>', lambda _: 'break')
       self.inputfield.bind('<Control-x>', lambda _: 'break')
       self.inputfield.bind('<Control-a>', lambda _: 'break')
       self.bframe = tk.Frame(self)
       self.bframe.pack(side="bottom")
       self.sb = tk.Button(self.bframe, text="Stop", width = 10, height = 2, bd = 0, bg = "#eee", cursor = "hand2", command=self.stopfunction)
       self.sb.pack(side="left")
       self.cb = tk.Button(self.bframe, text="Clear", width = 10, height = 2, bd = 0, bg = "#eee", cursor = "hand2", command=self.clearfunction)
       self.cb.pack(side="left")


   def stopfunction(self):
   	   entered_string = self.inputfield.get("1.0",'end-1c')
   	   if entered_string:
   	   	regexx = re.compile(r'zxcvbnm,\./ ')
   	   	p = regexx.findall(entered_string)
   	   	self.inputfield.delete('1.0', 'end')
   	   	self.inputfield.insert('1.0', 'The number of times you entered correctly is %d'%(len(p)))
   	   else:
   	   	self.inputfield.insert('1.0', "you didn't enter anything!")
   	   

   def clearfunction(self):
   	   self.inputfield.delete('1.0', 'end')
       
class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        p1 = Page1(self)
        p2 = Page2(self)
        p3 = Page3(self)
        p4 = Page4(self)

        buttonframe = tk.Frame(self)
        container = tk.Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p4.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        b1 = tk.Button(buttonframe, text="Home", fg = "black", width = 10, height = 1, bd = 0, bg = "#eee", cursor = "hand2", command=p1.lift)
        b2 = tk.Button(buttonframe, text="Middle row", fg = "black", width = 10, height = 1, bd = 0, bg = "#eee", cursor = "hand2", command=p2.lift)
        b3 = tk.Button(buttonframe, text="Top row", fg = "black", width = 10, height = 1, bd = 0, bg = "#eee", cursor = "hand2", command=p3.lift)
        b4 = tk.Button(buttonframe, text="Bottom row", fg = "black", width = 10, height = 1, bd = 0, bg = "#eee", cursor = "hand2", command=p4.lift)

        b1.pack(side="left")
        b2.pack(side="left")
        b3.pack(side="left")
        b4.pack(side="left")

        p1.show()
class Page1(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = tk.Label(self, text="Welcome to Typing Tutor")
       label.pack(side="top", fill="both", expand=True)
       

# Driver code

if __name__ == "__main__":
    root = tk.Tk()
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.title("Typing Tutor")
    root.wm_geometry("500x600")
    root.mainloop()
    
    
