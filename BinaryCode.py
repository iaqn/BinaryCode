#  !/usr/bin/env python3.9
#  -*- coding: utf-8 -*-
#  author:朱亦菲

import tkinter as tk
import tkinter.messagebox
import platform
import numpy as np
import random 
from itertools import combinations
from itertools import permutations
window=tk.Tk()
window.title("Home")
window.geometry("600x300")


def val():
    global val_value
    validation = tk.Toplevel(window)
    validation.geometry('600x300')
    validation.title('validation')
    text = tk.Label(validation,bd=4,fg='red',text='Please enter the total number of binary code to verify:')
    text.pack()
    #设置文本只能输入数字
    def test(content):
        # 如果不加上==""的话，就会发现删不完。总会剩下一个数字 isdigit函数：isdigit函数方法检测字符串是否只由数字组成。
        if content.isdigit() or content == "":
            return True
        else:
            return False
    v = tk.StringVar()  #跟踪变量的值的变化，以保证值的变更随时可以显示在界面上
    test_cmd = validation.register(test)  # 需要将函数包装一下，必要的
    val_e = tk.Entry(validation, show=None, font=('Arial', 14),
                    textvariable = v,  #文本框的值，是一个StringVar()对象 ，这样与StringVar 就能更新
                    validate = "key",  # 发生任何变动的时候，就会调用validatecommand 这个调动受后面‘Key’影响，类似键盘监听 如果换成“'focusout'"就是光标
                    validatecommand = (test_cmd, '%P'))  # %P代表输入框的实时内容 # %P表示 当输入框的值允许改变，该值有效。该值为当前文本框内容 # %v(小写大写不一样的)，当前validate的值  # %W表示该组件的名字)  # 显示成明文
    val_e.pack()
    
    
    
    
    
    
    def create_label():   
        n=val_e.get()  #这个只能是数字，并且是大于1的整数
        
        n=int(n)
        if n>1:
            class ScrollFrame(tk.Frame):
                def __init__(self, parent):
                    super().__init__(parent) # create a frame (self)

                    self.canvas = tk.Canvas(self, borderwidth=0, background="#ffffff")          #place canvas on self
                    self.viewPort = tk.Frame(self.canvas, background="#ffffff")                    #place a frame on the canvas, this frame will hold the child widgets 
                    self.vsb = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview) #place a scrollbar on self 
                    self.canvas.configure(yscrollcommand=self.vsb.set)                          #attach scrollbar action to scroll of canvas

                    self.vsb.pack(side="right", fill="y")                                       #pack scrollbar to right of self
                    self.canvas.pack(side="left", fill="both", expand=True)                     #pack canvas to left of self and expand to fil
                    self.canvas_window = self.canvas.create_window((4,4), window=self.viewPort, anchor="nw",            #add view port frame to canvas
                                            tags="self.viewPort")
                    

                    self.viewPort.bind("<Configure>", self.onFrameConfigure)                       #bind an event whenever the size of the viewPort frame changes.
                    self.canvas.bind("<Configure>", self.onCanvasConfigure)                       #bind an event whenever the size of the canvas frame changes.
                        
                    self.viewPort.bind('<Enter>', self.onEnter)                                 # bind wheel events when the cursor enters the control
                    self.viewPort.bind('<Leave>', self.onLeave)                                 # unbind wheel events when the cursorl leaves the control

                    self.onFrameConfigure(None)                                                 #perform an initial stretch on render, otherwise the scroll region has a tiny border until the first resize
                    # 端口input
                    self._port_var = tk.StringVar()
                    self._port_entry =tk.Entry(self.viewPort,textvariable=self._port_var, width=10)
                    #self._port_entry.grid(row=0, column=1, padx=5, pady=5)
                    self._port_entry.bind('<KeyPress>', lambda e: e if (e.keycode != 299 and e.char in set('01')) or e.keycode==46 or e.keycode==8 else "break")  # 46 represents delete and 8 represents backspace
                def onFrameConfigure(self, event):                                              
                    '''Reset the scroll region to encompass the inner frame'''
                    self.canvas.configure(scrollregion=self.canvas.bbox("all"))                 #whenever the size of the frame changes, alter the scroll region respectively.

                def onCanvasConfigure(self, event):
                    '''Reset the canvas window to encompass inner frame when required'''
                    canvas_width = event.width
                    self.canvas.itemconfig(self.canvas_window, width = canvas_width)            #whenever the size of the canvas changes alter the window region respectively.

                def onMouseWheel(self, event):                                                  # cross platform scroll wheel event
                    if platform.system() == 'Windows':
                        self.canvas.yview_scroll(int(-1* (event.delta/120)), "units")
                    elif platform.system() == 'Darwin':
                        self.canvas.yview_scroll(int(-1 * event.delta), "units")
                    else:
                        if event.num == 4:
                            self.canvas.yview_scroll( -1, "units" )
                        elif event.num == 5:
                            self.canvas.yview_scroll( 1, "units" )
                
                def onEnter(self, event):                                                       # bind wheel events when the cursor enters the control
                    if platform.system() == 'Linux':
                        self.canvas.bind_all("<Button-4>", self.onMouseWheel)
                        self.canvas.bind_all("<Button-5>", self.onMouseWheel)
                    else:
                        self.canvas.bind_all("<MouseWheel>", self.onMouseWheel)

                def onLeave(self, event):                                                       # unbind wheel events when the cursorl leaves the control
                    if platform.system() == 'Linux':
                        self.canvas.unbind_all("<Button-4>")
                        self.canvas.unbind_all("<Button-5>")
                    else:
                        self.canvas.unbind_all("<MouseWheel>")

    

    # ********************************
    # Example usage of the above class
    # ********************************

            class Example(tk.Frame):
                def __init__(self, root):

                    tk.Frame.__init__(self, root)
                    self.scrollFrame = ScrollFrame(self) # add a new scrollable frame.
                    
                    # Now add some controls to the scrollframe. 
                    # NOTE: the child controls are added to the view port (scrollFrame.viewPort, NOT scrollframe itself)
                    my_entries =[]
                    
                    def caculate():
                        num=0
                        sum_z=0
                        val_value=[]
                        alr_val=[]
                        for i in range(n):
                            val_value.append(my_entries[i].get())
                        before_len=len(val_value[0])
                        for i in val_value:
                            after_len=len(i)
                            num=num+1
                            #偶数位
                            if len(i)%2!=0:
                                tkinter.messagebox.showwarning(title='Warning', message='第%s行不是偶数位!!!'%num)  
                            else:    
                                if after_len!=before_len: #大小相等
                                    tkinter.messagebox.showwarning(title='Warning', message='第%s行位数与前面不同!!!'%num)  
                                else:
                                    if i in alr_val:  #所有码不能有重复的
                                        tkinter.messagebox.showwarning(title='Warning', message='第%s行重复了!!!'%num)
                                    else:
                                        alr_val.append(i)    
                        if len(val_value)==len(alr_val):
                            for i in range(after_len):
                                sum_zero=0
                                for j in alr_val:
                                    #计算0的个数
                                    if j[i]=='0':
                                        sum_zero=sum_zero+1
                                if sum_zero%2==0:
                                    sum_z=sum_z+1
                                else:
                                    sum_z=sum_z-1
                            if sum_z==0:
                                tkinter.messagebox.showinfo(title='Successfully', message='正交!')
                            else:
                                tkinter.messagebox.showerror(title='error', message='不正交!')
                                
                                
                                    
                                    
                                    
                                
                                    
                                    
                        
                        
                        
                
                    for row in range(n):
                        a = row
                        tk.Label(self.scrollFrame.viewPort, text="%s" % (a+1), width=3, borderwidth="1").grid(row=row, column=0)
                        
                        # 端口input
                        port_var = tk.StringVar()
                        port_entry =tk.Entry(self.scrollFrame.viewPort,textvariable=port_var, width=25)
                        port_entry.grid(row=a, column=1, padx=5, pady=5)
                        port_entry.bind('<KeyPress>', lambda e: e if (e.keycode != 299 and e.char in set('01')) or e.keycode==46 or e.keycode==8 else "break")  # 46 represents delete and 8 represents backspace
                        my_entries.append(port_entry)
                        #valuelist[n][a]
                        
                        
                        '''
                        if port_entry.get()%2!=0:
                            tk.Label(self.scrollFrame.viewPort, text="输入位数不满足偶数位！！！" , width=3, borderwidth="1").grid(row=row, column=3)'''
                        
                    

                        
                        '''
                        #设置文本只能输入0/1
                        def test(content):
                            # 如果不加上==""的话，就会发现删不完。总会剩下一个数字 isdigit函数：isdigit函数方法检测字符串是否只由数字组成。
                            if content.isdigit() or content == "":
                                return True
                            else:
                                return False
                        v = tk.StringVar()  #跟踪变量的值的变化，以保证值的变更随时可以显示在界面上
                        test_cmd = validation.register(test)  # 需要将函数包装一下，必要的
                        val_e = tk.Entry(validation, show=None, font=('Arial', 14),
                                        textvariable = v,  #文本框的值，是一个StringVar()对象 ，这样与StringVar 就能更新
                                        validate = "key",  # 发生任何变动的时候，就会调用validatecommand 这个调动受后面‘Key’影响，类似键盘监听 如果换成“'focusout'"就是光标
                                        validatecommand = (test_cmd, '%P'))  # %P代表输入框的实时内容 # %P表示 当输入框的值允许改变，该值有效。该值为当前文本框内容 # %v(小写大写不一样的)，当前validate的值  # %W表示该组件的名字)  # 显示成明文
                        val_e.pack()
                        
                        
                        
                        
                        
                        
                        tk.Entry(self.scrollFrame.viewPort, width=30,show=None,relief="solid").grid(row=row, column=1)'''

                    # when packing the scrollframe, we pack scrollFrame itself (NOT the viewPort)
                    
                        
                        
                    val_b2 = tk.Button(self.scrollFrame.viewPort, text='confirm', width=10,height=2, command=caculate)
                    val_b2.place(relx=1,rely=1,anchor='se')
                    self.scrollFrame.pack(side="top", fill="both", expand=True)
                    
                
                def printMsg(self, msg):
                    print(msg)
        
            if __name__ == "__main__":
                root=tk.Tk()
                Example(root).pack(side="top", fill="both", expand=True)
                root.title("input binary code")
                root.mainloop()
                
        else:
            tkinter.messagebox.showwarning(title='Warning', message='输入数量必须大于1!')                
            '''         
            can=tk.Canvas(validation, borderwidth=0, background="#ffffff") 
            frame = tk.LabelFrame(can, text="input binary code")
            #滚动条
            roll = tk.Scrollbar(validation,orient="vertical") #创建滚动条
            roll.pack(side = tk.RIGHT,fill = tk.Y)

            for i in range(int(n)):
                numlabel=tk.Label(frame,text='第%s行'%(i+1))
                numlabel.grid(row=i, column=0)
                
                val_n=tk.Entry(frame,width=20,show=None)
                val_n.grid(row=i, column=1)
                val_value.append(val_n.get())
                can.pack()
            frame.pack(padx=20, pady=5, ipadx=10, ipady=10)
            #绑定
            can.config(yscrollcommand=roll.set) # text绑定垂直滚动条
            roll.config(command=can.yview) '''  
            #else:
            #    tkinter.messagebox.showinfo(title='Tip', message='please reopening the page!')  
    val_b1 = tk.Button(validation, text='confirm', width=10,height=2, command=create_label)
    val_b1.pack()  

            
            
            
            
# n的数量有限制吗？
#输入位数只能是偶数位
#只能是0 1，不满足要进行报错提醒在XXX个，并且提示报错理由
#后一个的位数必须等于前一个的位数，不满足位数要进行报错提醒在XXX个
#所有码不能有重复的


###
#所有行不能有重复
#1-64超出范围直接报错
#正交码数量必须大于等于2    
def ach():
    create = tk.Toplevel(window)
    create.geometry('600x300')
    create.title('create')
    text = tk.Label(create,bd=4,fg='red',text='Enter a specific value of 1-64 bits (integer):')
    text.pack()
    #设置文本只能输入数字
    def test2(content):
        # 如果不加上==""的话，就会发现删不完。总会剩下一个数字 isdigit函数：isdigit函数方法检测字符串是否只由数字组成。
        if content.isdigit() or content == "":
            return True
        else:
            return False
    v2 = tk.StringVar()  #跟踪变量的值的变化，以保证值的变更随时可以显示在界面上
    test_cmd2 = create.register(test2)  # 需要将函数包装一下，必要的
    val_2 = tk.Entry(create, show=None, font=('Arial', 14),
                    textvariable = v2,  #文本框的值，是一个StringVar()对象 ，这样与StringVar 就能更新
                    validate = "key",  # 发生任何变动的时候，就会调用validatecommand 这个调动受后面‘Key’影响，类似键盘监听 如果换成“'focusout'"就是光标
                    validatecommand = (test_cmd2, '%P'))  # %P代表输入框的实时内容 # %P表示 当输入框的值允许改变，该值有效。该值为当前文本框内容 # %v(小写大写不一样的)，当前validate的值  # %W表示该组件的名字)  # 显示成明文
    val_2.pack()
    text2 = tk.Label(create,bd=4,fg='red',text='Enter the amount of binary code that needs to be orthogonal:')
    text2.pack()
    v3 = tk.StringVar()
    val_3 = tk.Entry(create, show=None, font=('Arial', 14),
                    textvariable = v3,  #文本框的值，是一个StringVar()对象 ，这样与StringVar 就能更新
                    validate = "key",  # 发生任何变动的时候，就会调用validatecommand 这个调动受后面‘Key’影响，类似键盘监听 如果换成“'focusout'"就是光标
                    validatecommand = (test_cmd2, '%P'))  # %P代表输入框的实时内容 # %P表示 当输入框的值允许改变，该值有效。该值为当前文本框内容 # %v(小写大写不一样的)，当前validate的值  # %W表示该组件的名字)  # 显示成明文
    val_3.pack()
    def create_code():
        n1=val_2.get()
        n2=val_3.get()
        n1=int(n1)
        n2=int(n2)
        if n1<2 or n1>64:#2-64超出范围直接报错
            tkinter.messagebox.showwarning(title='Warning', message='输入的比特数值超出范围,应在2-64之间!') 
        else:
            if n1%2!=0:#正交码位数必须为偶数
                tkinter.messagebox.showwarning(title='Warning', message='正交码位数必须为偶数!') 
            else:
                if n2<2:#正交码数量必须大于等于2
                    tkinter.messagebox.showwarning(title='Warning', message='正交码数量不能小于2!') 
                else:
                    base_list=[0,1]
                    #所有行不能有重复
                    judge_conf=False
                    def judge(list):  #judge o
                        sum_z2=0
                        for i in range(n1):
                            sum_zero2=0
                            for j in range(n2):
                                #计算0的个数
                                if list[j][i]==0:
                                    sum_zero2=sum_zero2+1
                            if sum_zero2%2==0:
                                sum_z2=sum_z2+1
                            else:
                                sum_z2=sum_z2-1   
                        if sum_z2==0:
                            return True
                        else:
                            return False
                    #分成两部分，小于等于8和大于8
                    #1
                    #first step generate baselist                                                                              
                    baselist=[]
                    if n1<=8:
                        if n1==2:
                            for i in base_list:
                                for j in base_list:
                                    baselist.append([i,j])
                        if n1==4:
                            for i in base_list:
                                for j in base_list:
                                    for m in base_list:
                                        for n in base_list:
                                            baselist.append([i,j,m,n])
                        if n1==6:
                            for i in base_list:
                                for j in base_list:
                                    for m in base_list:
                                        for n in base_list:
                                            for a in base_list:
                                                for b in base_list:
                                                    baselist.append([i,j,m,n,a,b])    
                        if n1==8:
                            for i in base_list:
                                for j in base_list:
                                    for m in base_list:
                                        for n in base_list:
                                            for a in base_list:
                                                for b in base_list:
                                                    for c in base_list:
                                                        for d in base_list:                                               
                                                            baselist.append([i,j,m,n,a,b,c,d]) 
                        
                        
                        loop_num=0   
                        while(judge_conf==False):
                            comb_list=[]#second step generate combnation
                            while(len(comb_list)<n2):
                                ro=random.choice(baselist)
                                if ro not in comb_list:#不能重复
                                    comb_list.append(ro)
                            if judge(comb_list):
                                judge_conf=True
                                result=comb_list
                                break
                            loop_num=loop_num+1
                            if loop_num>20000:
                                break     
                                       
                    
                                                     
                    #2
                    #所有行不能有重复
                    if n1>8 :
                        if n2>(pow(2,n1)/7):######
                            tkinter.messagebox.showerror(title='error', message='不存在这样数量的二分码!') 
                        else:
                            while(judge_conf==False):
                                validation_list=[]
                                numrow=0
                                while(numrow<n2):
                                    row=[]
                                    for j in range(n1):
                                        row.append(random.choice(base_list))
                                    if row not in validation_list:
                                        validation_list.append(row)
                                        numrow=numrow+1
                                if judge(validation_list):
                                        judge_conf=True
                                        result=validation_list
                    
                                        
                    if judge_conf==False:
                        tkinter.messagebox.showerror(title='error', message='不存在这样数量的二分码!')                             
                                
                    if judge_conf:
                        def make_menu(w):
                            global the_menu
                            the_menu = tk.Menu(w, tearoff=0)
                            the_menu.add_command(label="Cut")
                            the_menu.add_command(label="Copy")
                            the_menu.add_command(label="Paste")

                        def show_menu(e):
                            w = e.widget
                            the_menu.entryconfigure("Cut",
                            command=lambda: w.event_generate("<<Cut>>"))
                            the_menu.entryconfigure("Copy",
                            command=lambda: w.event_generate("<<Copy>>"))
                            the_menu.entryconfigure("Paste",
                            command=lambda: w.event_generate("<<Paste>>"))
                            the_menu.tk.call("tk_popup", the_menu, e.x_root, e.y_root)                        
                        binary_code = tk.Toplevel(window)
                        binary_code.geometry('400x300')
                        binary_code.title('binary code ')
                        
                        
                        #滚动条
                        roll = tk.Scrollbar(binary_code ) #创建滚动条
                        roll.pack(side = tk.RIGHT,fill = tk.Y)
                        text_input = tk.Text(binary_code ,width=100,height=20)
                        for i in result: #在文本中插入数据
                            text_input.insert('insert','%s\n'%i)
                            text_input.pack(expand=tk.YES,fill=tk.BOTH)
                            #绑定
                            text_input.config(yscrollcommand=roll.set) # text绑定垂直滚动条
                            roll.config(command=text_input.yview)
                        #复制粘贴剪切效果
                        make_menu(binary_code)
                        text_input.bind_class("Text", "<Button-3><ButtonRelease-3>", show_menu)
    
    val_b5 = tk.Button(create, text='confirm', width=10,height=2, command=create_code)
    val_b5.pack()
    
    
    
    
    
    
    
    
    
## the index page
x = {"red": "cross", "orange": "boat", "lightgreen": "clock", "lightblue": "star"}
for i in x:
    # 建立四个不同底色的框架与光标形状
    tkinter.Frame(bg=i, cursor=x[i], height=300, width=150).pack(side=tkinter.LEFT)
    
b1 = tk.Button(window, text='validation', width=10,height=2, command=val)
b1.place(x=350,y=90,anchor='nw')

b2 = tk.Button(window, text='create ', width=10,height=2, command=ach)
b2.place(x=200,y=90,anchor='nw')





from PIL import Image, ImageTk



def create_docx():
    help_document = tk.Toplevel(window)
    help_document.geometry('1000x800')
    help_document.title('Help Document')
    #滚动条
    roll = tk.Scrollbar(help_document) #创建滚动条
    roll.pack(side = tk.RIGHT,fill = tk.Y)
    text_input = tk.Text(help_document,width=100,height=20)
    #在文本中插入数据
    text_input.insert('insert',"介绍：\n    初始界面：Home\n    菜单栏： File-exit（退出程序） help- help document（帮助文档）\n    主界面按钮：\n  create（生成正交二分码）\n  validation（验证二分码）\n")
    text_input.insert('insert',"操作：\n（一）生成正交二分码：\n1.点击“create”进入创建页面\n")
    
    
    photo = tk.PhotoImage(file="./image/1.gif")
    text_input.image_create("current", image=photo)#用这个方法创建一个图片对象，并插入到“END”的位置
    text_input.insert("insert","\n")
    text_input.insert("insert","2.输入想要生成的正交二分码比特位数（仅限2bite-64bite的偶数位）\n")
    photo2 = tk.PhotoImage(file="./image/2.gif")
    text_input.image_create("current", image=photo2)#用这个方法创建一个图片对象，并插入到“END”的位置
    text_input.insert("insert","\n")
    text_input.insert("insert","3.输入想要生成的正交二分码数量（若数量过大，会造成卡顿）\n")
    photo3 = tk.PhotoImage(file="./image/3.gif")
    text_input.image_create("current", image=photo3)#用这个方法创建一个图片对象，并插入到“END”的位置
    text_input.insert("insert","\n")
    text_input.insert("insert","4.点击“confirm”按钮进行确认\n")
    photo4 = tk.PhotoImage(file="./image/4.gif")
    text_input.image_create("current", image=photo4)#用这个方法创建一个图片对象，并插入到“END”的位置
    text_input.insert("insert","\n")
    text_input.insert("insert","5.正确输入并确认之后，会生成“binary code”界面，可通过鼠标右键进行复制、粘贴、剪切\n")
    photo5 = tk.PhotoImage(file="./image/5.gif")
    text_input.image_create("current", image=photo5)#用这个方法创建一个图片对象，并插入到“END”的位置
    text_input.insert("insert","\n")
    text_input.insert("insert","（二）验证二分码：\n1.点击“validation”按钮进入验证页面\n")
    photo6 = tk.PhotoImage(file="./image/6.gif")
    text_input.image_create("current", image=photo6)#用这个方法创建一个图片对象，并插入到“END”的位置
    text_input.insert("insert","\n")
    text_input.insert("insert","2.输入想要验证的正交二分码数量（若数量过大，会造成卡顿）,并点击confirm按钮\n")
    photo7 = tk.PhotoImage(file="./image/7.gif")
    text_input.image_create("current", image=photo7)#用这个方法创建一个图片对象，并插入到“END”的位置
    text_input.insert("insert","\n")
    text_input.insert("insert","3.正确填写每个框中的二分码\n")
    photo8 = tk.PhotoImage(file="./image/8.gif")
    text_input.image_create("current", image=photo8)#用这个方法创建一个图片对象，并插入到“END”的位置
    text_input.insert("insert","\n")
    text_input.insert("insert","4.填写完成后，点击“confirm”按钮，进行确认。若错误会有相应的错误提示。\n")
    photo9 = tk.PhotoImage(file="./image/9.gif")
    text_input.image_create("current", image=photo9)#用这个方法创建一个图片对象，并插入到“END”的位置
    text_input.insert("insert","\n")
    text_input.insert("insert","5.正确输入后会弹出提示框，告知判断结果。\n")
    photo10 = tk.PhotoImage(file="./image/10.gif")
    text_input.image_create("current", image=photo10)#用这个方法创建一个图片对象，并插入到“END”的位置
    text_input.insert("insert","\n")
    
    text_input.pack(expand=tk.YES,fill=tk.BOTH)
    #绑定
    text_input.config(yscrollcommand=roll.set) # text绑定垂直滚动条
    roll.config(command=text_input.yview)
    help_document.mainloop()

    
    


## section--menu
menubar = tk.Menu(window)
filemenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='Exit', command=window.quit) # 用tkinter里面自带的quit()函数
editmenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='help', menu=editmenu)
editmenu.add_command(label='help document', command=create_docx) # 用tkinter里面自带的quit()函数
window.config(menu=menubar) 
# 第6步，主窗口循环显示
window.mainloop()


#实现功能
'''
滑轮滚动
鼠标右键复制粘贴剪切
菜单退出
帮助文档
错误提示
限制输入
等
'''