#!/usr/bin/env python
# coding: utf-8

# In[3]:


from tkinter import*

parent=Tk()
parent.mainloop()


# In[6]:


from tkinter import*

parent=Tk()
name=Label(parent,text='name',fg='red',bg='black').pack()
parent.mainloop()


# In[7]:


from tkinter import*

parent=Tk()
but1=Button(parent,text='red',bg='red',fg='white').pack(side=LEFT)
but1=Button(parent,text='yellow',bg='yellow',fg='white').pack(side=RIGHT)
but1=Button(parent,text='orange',bg='orange',fg='white').pack(side=TOP)
but1=Button(parent,text='pink',bg='pink',fg='white').pack(side=BOTTOM)
parent.mainloop()


# In[11]:


from tkinter import*

parent=Tk()
parent.geometry('300x200')
name=Label(parent,text='name').grid(row=0,column=0)
password=Label(parent,text='password').grid(row=2,column=0)
submit=Button(parent,text='submit').grid(row=3,column=1)
text1=Entry(parent).grid(row=0,column=1)
text2=Entry(parent).grid(row=2,column=1)
parent.mainloop()


# In[21]:


from tkinter import*

parent=Tk()
parent.geometry('300x200')
name=Label(parent,text='name').place(x=20,y=50)
password=Label(parent,text='password').place(x=20,y=80)
submit=Button(parent,text='submit').place(x=130,y=140)
text1=Entry(parent).place(x=100,y=50)
text2=Entry(parent).place(x=100,y=80)
parent.mainloop()


# In[34]:


from tkinter import*
from tkinter import messagebox

def mes1():
    messagebox.showinfo('welcome','you enterd red button')
def mes2():
    messagebox.showinfo('welcome','you enterd yellow button')
def mes3():
    messagebox.showinfo('welcome','you enterd orange button')
def mes4():
    messagebox.showinfo('welcome','you enterd pink button')
        
parent=Tk()
parent.geometry('300x200')
but1=Button(parent,text='red',activeforeground='yellow',activebackground='black',command=mes1,bg='red',fg='white').pack(side=LEFT)
but1=Button(parent,text='yellow',bg='yellow',command=mes2,fg='white').pack(side=RIGHT)
but1=Button(parent,text='orange',bg='orange',command=mes3,fg='white').pack(side=TOP)
but1=Button(parent,text='pink',bg='pink',command=mes4,fg='white').pack(side=BOTTOM)
parent.mainloop()


# In[45]:


from tkinter import*

parent=Tk()
parent.geometry('300x300')
c=Canvas(parent,bg='pink',height='200',width='250').pack()
parent.mainloop()


# In[62]:


from tkinter import *   
      
parent = Tk()  
parent.geometry("200x200")    
c = Canvas(parent,bg = "pink",height = "200",width = 200)  
arc = c.create_arc((5,20,150,200),start = 0,extent = 150, fill= "white")  
c.pack()  
parent.mainloop()  


# In[203]:


from tkinter import *   
      
parent = Tk()  
parent.geometry('300x200')
var1=IntVar()
var2=IntVar()
var3=IntVar()
chbut1=Checkbutton(parent,text='C',variable=var1,onvalue=1,offvalue=0).pack()
chbut2=Checkbutton(parent,text='Python',variable=var2,onvalue=1,offvalue=0).pack()
chbut3=Checkbutton(parent,text='Java',variable=var3,onvalue=1,offvalue=0).pack()
parent.mainloop()


# In[123]:


from tkinter import*
from functools import partial  
       
       
def call_result(label_result, n1, n2):  
    num1 = (n1.get())  
    num2 = (n2.get())   
    result = int(num1)+int(num2)  
    label_result.config(text="Result = %d" % result)  
    return  
       
root = Tk()  
root.geometry('400x200')  
root.title('Calculator')  
number1 = StringVar()  
number2 = StringVar()  
labelNum1 =Label(root, text="A").grid(row=1, column=0)  
labelNum2 =Label(root, text="B").grid(row=2, column=0)  
labelResult =Label(root)  
labelResult.grid(row=7, column=2)  
entryNum1 = Entry(root, textvariable=number1).grid(row=1, column=2)  
entryNum2 = Entry(root, textvariable=number2).grid(row=2, column=2)  
call_result = partial(call_result, labelResult, number1, number2)  
buttonCal = Button(root, text="Calculate", command=call_result).grid(row=3, column=0)  
root.mainloop()  


# In[155]:


from tkinter import*

parent=Tk()
parent.geometry('500x400')
lab=Label(text='following language are very good').pack()
box=Listbox(parent)
box.insert(1,'python')
box.insert(2,'ml')
box.insert(3,'dl')
box.insert(4,'ai')
box.pack()
but1=Button(parent,text='delete',command=lambda box=box:box.delete(ANCHOR)).pack()


parent.mainloop()


# In[174]:


from tkinter import*

parent=Tk()
parent.geometry('500x400')
menu=Menubutton(parent,text='file',relief=FLAT)
menu.m=Menu(menu)
menu['menu']=menu.m
menu.m.add_checkbutton(label='new project',variable=IntVar())
menu.m.add_checkbutton(label='open',variable=IntVar())
menu.m.add_checkbutton(label='save',variable=IntVar())
menu.m.add_checkbutton(label='save_as',variable=IntVar())
menu.m.add_checkbutton(label='exit',variable=IntVar())
menu.grid()
parent.mainloop()



# In[171]:


from tkinter import*

def simple():
    messagebox.showinfo('welcome','hello!!!!!')

parent=Tk()
menubar=Menu(parent)
menubar.add_command(label='hello',command=simple)
menubar.add_command(label='quit',command=parent.quit)
parent.config(menu=menubar)
parent.mainloop()


# In[202]:


from tkinter import*
from tkinter import Toplevel,Button,Tk,Menu

parent=Tk()
menubar=Menu(parent)

file=Menu(menubar,tearoff=0)
file.add_command(label='open')
file.add_command(label='new projet')
file.add_command(label='save')
file.add_command(label='save as')
file.add_separator()
file.add_command(label='exit')
menubar.add_cascade(label='File',menu=file)

edit=Menu(menubar,tearoff=0)
edit.add_command(label='undo')
edit.add_command(label='redo')
edit.add_separator()
edit.add_command(label='cut')
edit.add_command(label='copy')
edit.add_command(label='past')
menubar.add_cascade(label='Edit',menu=edit)
parent.config(menu=menubar)
parent.mainloop()


# In[229]:


from tkinter import*

def show():  
   selection = "You selected the option " + str(radio.get())  
   label.config(text = selection)  
parent=Tk()
parent.geometry('400x300')
lab=Label(text='please select the skils').pack()
radio=IntVar()
ch1=Radiobutton(parent,text='C',variable=radio,value=1,command=show)
ch1.pack(anchor=W)
ch2=Radiobutton(parent,text='C++',variable=radio,value=2,command=show)
ch2.pack(anchor=W)
ch3=Radiobutton(parent,text='java',variable=radio,value=3,command=show)
ch3.pack(anchor=W)
ch4=Radiobutton(parent,text='.net',variable=radio,value=4,command=show)
ch4.pack(anchor=W)
label=Label(parent)
label.pack()
parent.mainloop()


# In[243]:


from tkinter import*

def sample():  
   selection = "You selected the value " + str(v.get())  
   lab.config(text = selection)  

parent=Tk()
parent.geometry('400x300')
v=IntVar()
sc=Scale(parent,from_=1,to=10,variable=v,orient=HORIZONTAL)
but=Button(parent,text='Enter',command=sample)
lab=Label(parent)
lab.pack()
sc.pack(anchor=W)
but.pack(anchor=W)
parent.mainloop()


# In[261]:


from tkinter import*

parent=Tk()
#parent.geometry('400x300')
bar=Scrollbar(parent)
data=Listbox(parent,yscrollcommand=bar.set)
for i in range (1,30):
    data.insert(END,'number' + str(i))
data.pack(side=LEFT)
bar.pack(side=RIGHT,fill=Y)
bar.config(command=data.yview)
but=Button(parent,text='DELETE',command=lambda data=data:data.delete(ANCHOR)).pack()
parent.mainloop()
        


# In[266]:


from tkinter import*

parent=Tk()
parent.geometry('400x300')
box=Text(parent).pack()
parent.mainloop()


# In[270]:


from tkinter import*

def nex():
    top=Toplevel(parent)
    top.mainloop()
    
parent=Tk()
parent.geometry('400x300')
but=Button(parent,text='next',command=nex).pack()
parent.mainloop()


# In[271]:


from tkinter import*

parent=Tk()
parent.geometry('400x300')
s=Spinbox(parent,from_=1,to=10).pack()
parent.mainloop()


# In[283]:


from tkinter import*
def mes():
    messagebox.showinfo('information','hai welcome to the daniel softech_solution')
def war():
    messagebox.showwarning('warnings','wrong selecction')
def err():
    messagebox.showerror('error','file cannot open')                    
def qu():
    messagebox.askquestion('question','are you sure?')
def ok():
    messagebox.askokcancel('ok or cancel','delete this file')
def ret():
    messagebox.askretrycancel('retry','process destroyed')
def yes():
    messagebox.askyesno('yes or no','save this files')
        
parent=Tk()
parent.geometry('400x300')
radio=IntVar()
but=Button(parent,text='information',command=mes).pack()
but1=Button(parent,text='warnings',command=war).pack()
but2=Button(parent,text='error',command=err).pack()
but3=Button(parent,text='askquestion',command=qu).pack()
but4=Button(parent,text='askokcancel',command=ok).pack()
but5=Button(parent,text='askretrycancel',command=ret).pack()
but6=Button(parent,text='askyesno',command=yes).pack()
parent.mainloop()


# In[ ]:




