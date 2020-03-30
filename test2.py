from tkinter import *
from tkinter import ttk, colorchooser
from tkinter.filedialog import askopenfilename as ak47
from PIL import ImageTk, Image



class main:
    def __init__(self,master):
        self.master = master
        self.color_fg = 'black'
        self.color_bg = 'white'
        self.old_x = None
        self.old_y = None
        self.penwidth = 5
        self.idcontainer=[]
        self.drawWidgets()
        self.c.bind('<B1-Motion>',self.paint)#drwaing the line 
        self.c.bind('<ButtonRelease-1>',self.reset)
        self.ox=[]
        self.oy=[]
        self.pen=0
        for item in self.idcontainer:
            self.ox[item]=None
            self.oy[item]=None
        '''for item in self.idcontainer:
            self.c.tag_bind(item,'<B1-Motion>',self.mover(item))'''

    def paint(self,e):
        if self.pen == 1:
            self.c.config(cursor="pencil")
            if self.old_x and self.old_y:
                self.c.create_line(self.old_x,self.old_y,e.x,e.y,width=self.penwidth,fill=self.color_fg,capstyle=ROUND,smooth=True)

            self.old_x = e.x
            self.old_y = e.y
        else:
            self.c.config(cursor="hand1")
            if self.old_x and self.old_y:
            #if self.ox[CURRENT] and self.oy[CURRENT]:
                k=e.x-self.old_x
                l=e.y-self.old_y
                self.c.move(CURRENT,k,l)
            self.old_x = e.x
            self.old_y = e.y    
            ##self.oy[CURRENT]=e.y   

    def reset(self,e):    #reseting or cleaning the canvas 
        self.old_x = None
        self.old_y = None      

    def changeW(self,e): #change Width of pen through slider
        self.penwidth = e

    def mover(self,e,id):
        print("inside mover")
        self.c.config(cursor="hand1")
        if self.ox[item] and self.oy[item]:
            k=self.ox[item]-e.x
            l=self.oy[item]-e.y 
            pc=self.c.coords(item)
            self.c.itemconfigure(item,x=k+pc.x,y=l+pc.y)
        self.ox[item]=e.x
        self.oy[item]=e.y     

           

    def clear(self):
        self.c.delete(ALL)

    def entertext(self):
        self.popup = Toplevel(height=300, width=350)
        self.popup.title("Enter Text")
        self.txtframe = Frame(self.popup)
        self.txtframe.pack()
        self.big_text = Text(self.txtframe)
        self.big_text.insert('0.0'," ")
        self.big_text.pack()
        self.grab_text = Button(self.popup,text="Enter",command=self.callback)
        self.grab_text.pack(side=RIGHT)

    def callback(self):
        self.idcontainer.append(self.c.create_text(0,0,anchor=NW,font="Times 20 italic bold",text=self.big_text.get("1.0",'end-1c')))
        self.c.update    


    def change_fg(self):  #changing the pen color
        self.color_fg=colorchooser.askcolor(color=self.color_fg)[1]

    def change_bg(self):  #changing the background color canvas
        self.color_bg=colorchooser.askcolor(color=self.color_bg)[1]
        print(self.color_bg)
        self.c['bg'] = self.color_bg

    def donothing(self):
        x=0

    def selectpen(self):
        if self.pen==1:
            self.pen=0
            self.bpene.config(bg="lightgrey")    
        else:
            self.pen=1    
            self.bpene.config(bg="red")  
    
    def selectfile(self):
        fn=ak47()
        print(fn)
        img=Image.open(fn)
        img=img.resize((100,100))
        self.c.img=ImageTk.PhotoImage(img)
        self.idcontainer.append(self.c.create_image(0,0, image=self.c.img, anchor=NW))   

    def drawWidgets(self):
        
        self.controls = Frame(self.master,padx = 5,pady = 5,bg='DarkSeaGreen3')
        Label(self.controls, text='Pen Width:',font=('arial 10'),bg='DarkSeaGreen3').grid(row=0,column=0)
        self.slider = Scale(self.controls,from_= 5, to = 100,showvalue=0,bg="darkseagreen3",fg="darkseagreen3",command=self.changeW,orient=HORIZONTAL)
        self.slider.set(self.penwidth)
        self.slider.grid(row=0,column=1,ipadx=20)
        self.controls.pack(fill=X)
        
        self.c = Canvas(self.master,width=700,height=500,bg=self.color_bg)
        self.c.pack(side=LEFT,fill=BOTH,expand=True)
        
        
        self.btxte=Button(self.controls,text="T",height=1,command=self.entertext)
        self.btxte.grid(row=0,column=2,padx=10)
        self.bpene=Button(self.controls,text="D",height=1,command=self.selectpen)
        self.bpene.grid(row=0,column=3,padx=10)
        self.bpic=Button(self.controls,text="P",height=1,command=self.selectfile)
        self.bpic.grid(row=0,column=4,padx=10)

        
        self.chat = Frame(self.master,padx = 5,pady = 5,width=200,height=500,bg='DarkGreen')
        self.cframe=Frame(self.chat,height=460,bg="#ffe9c1")
        scrollbar=Scrollbar(self.cframe)
        self.chatdisplay=Listbox(self.cframe,bg="#ffe9c1",yscrollcommand=scrollbar.set)
        self.txtbar=Entry(self.chat,width=100,bg="LightGreen")
        self.sendb=Button(self.chat,text="->",bg="DarkGreen",fg="yellow")
        scrollbar.pack(side=RIGHT,fill=Y)
        self.chat.pack(side=RIGHT,fill=Y,expand=True)
        self.cframe.pack(fill=BOTH,expand=True)
        self.chatdisplay.pack(fill=BOTH,expand=True)
        self.sendb.pack(side=RIGHT)
        self.txtbar.pack(side=LEFT)
        

        menubar=Menu(self.master)
        f1menu=Menu(menubar, tearoff=0)
        f1menu.add_command(label="New page",command=self.donothing)
        f1menu.add_command(label="Save",command=self.donothing)
        f1menu.add_command(label="Settings",command=self.donothing)
        f1menu.add_command(label="Close",command=root.quit)
        menubar.add_cascade(labe="File", menu=f1menu)
        emenu = Menu(menubar)
        menubar.add_cascade(label='Edit',menu=emenu)
        emenu.add_command(label='Brush Color',command=self.change_fg)
        emenu.add_command(label='Background Color',command=self.change_bg)
        emenu.add_command(label='Clear Canvas',command=self.clear)

        f2menu=Menu(menubar, tearoff=0)
        f2menu.add_command(label="New connection", command=self.donothing)
        f2menu.add_command(label="Speed dial", command=self.donothing)
        menubar.add_cascade(labe="Connect", menu=f2menu) 

        self.master.config(menu=menubar)
        

       
        
        


if __name__ == '__main__':
    root = Tk()
    main(root)       
    root.title('Explain Pad')
    root.geometry("1050x600")
    root.mainloop()

    













    