from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from mysql.connector import *
from std1 import student

def main():
    win=Tk()
    app=login_window(win)
    win.mainloop()

class login_window:
    def __init__(self,root):    
        self.root=root
        self.root.title('login')
        self.root.geometry('1550x800+0+0')


        #main photo
        img1=Image.open(r'C:\Users\MAMATA\Desktop\pip\nature.jpg')
        img1=img1.resize((1550,800),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        lblimg=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lblimg.place(x=5,y=2,width=1550,height=800)

        frame=Frame(self.root,bg='black')
        frame.place(x=610,y=170,width=340,height=450)

        #first image
        img2=Image.open(r'C:\Users\MAMATA\Desktop\pip\m.jpg')
        img2=img2.resize((110,90),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        li=Label(image=self.photoimg2,bg='black',borderwidth=0)
        li.place(x=730,y=175,width=110,height=90)

        get_str=Label(frame,text='get started',font=('times new roman',21,'bold'),borderwidth=0,fg='black')
        get_str.place(x=120,y=100)

        #label
        username_lbl=Label(frame,text='Username',font=('times new roman',20,'bold'),fg='white',bg='black')
        username_lbl.place(x=70,y=155)

        self.txtuser=StringVar()
        self.txt_user=ttk.Entry(frame,textvariable=self.txtuser,font=('times new roman',15,'bold'))
        self.txt_user.place(x=40,y=187,width=270)

        self.txtpass=StringVar()
        username_pass=Label(frame,text='Password',font=('times new roman',20,'bold'),fg='white',bg='black').place(x=70,y=217)
        self.txt_pass=ttk.Entry(frame,textvariable=self.txtpass,font=('times new roman',15,'bold'))
        self.txt_pass.place(x=40,y=253,width=270)

        #*******************icon images*********
            
        #user pic
        img3=Image.open(r'C:\Users\MAMATA\Desktop\pip\m.jpg')
        img3=img3.resize((25,25),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        lblimg1=Label(frame,image=self.photoimg3,bd=4,relief=RIDGE)
        lblimg1.place(x=38,y=157,width=25,height=25)
        

        #password pic
        img4=Image.open(r'C:\Users\MAMATA\Desktop\pip\pass.png')
        img4=img4.resize((25,25),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        lblimg1=Label(frame,image=self.photoimg4,bd=4,relief=RIDGE)
        lblimg1.place(x=38,y=223,width=25,height=25)


       #login button
        login_but=Button(frame,text="login",command=self.login,font=('times new roman',15,'bold'),bd=3,relief=RIDGE,bg='green',fg='white',activebackground='red')
        login_but.place(x=110,y=300,width=120,height=35)

        #register butoon
        reg_but=Button(frame,text="New User Register",command=self.register_window,borderwidth=0,font=('times new roman',13,'bold'),relief=RIDGE,bg='black',fg='white',activebackground='black',activeforeground='white')
        reg_but.place(x=18,y=350,width=150)

        #forgott passwd
        fg_but=Button(frame,text="Forgot password",command=self.forgot_win,borderwidth=0,font=('times new roman',13,'bold'),relief=RIDGE,bg='black',fg='white',activebackground='black',activeforeground='white')
        fg_but.place(x=16,y=380,width=160)

    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=register(self.new_window)




    def login(self):
        if self.txt_user.get()=="" or self.txt_pass.get()==" ":
            messagebox.showerror('error','All fields required')
        elif self.txt_user.get()=='mam' and self.txt_pass.get()=='raj':
            messagebox.showinfo('success','Welcome to hotel pane page')
        else:
            conn=connect(host='localhost',user='root',password='8310728642',database='mam')
            cur=conn.cursor()
            cur.execute('select * from register where email=%s and password=%s',(self.txtuser.get(),self.txtpass.get()))
            row=cur.fetchone()
            if row==None:
                messagebox.showerror('error','Invalid username and password')
            else:
                self.new_window=Toplevel(self.root)
                self.app=student(self.new_window)
                
            conn.commit()
            conn.close()

    def reset(self):
        if self.combo_sec.get()=="select":
            messagebox.showerror('error','select security quetion',parent=self.root2)
        #elif self.password.get()=='':
         #   messagebox.showerror('error','please enter new password',parent=self.root2)
        else:
            conn=connect(host='localhost',user='root',password='8310728642',database='mam')
            cur=conn.cursor()
            query=('select * from register where email=%s and seq_qns=%s and seq_ans=%s')
            value=(self.txtuser.get(),self.combo_sec.get(),self.sq.get())
            cur.execute(query,value)
            row=cur.fetchone()
            if row==None:
                messagebox.showerror('error','please enter the correct answer',parent=self.root2)
            else:
                query=('update register set password=%s where email=%s')
                value=(self.txt_newpass.get(),self.txtuser.get())
                cur.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo('info','password changed succesfully',parent=self.root2)
                self.root2.destroy()
                

            
    def forgot_win(self):
        if self.txtuser.get()=="":
            messagebox.showerror('error','Please enter email')
        else:
            conn=connect(host='localhost',user='root',password='8310728642',database='mam')
            cur=conn.cursor()
            query=('select * from register where email=%s')
            value=(self.txtuser.get(),)
            cur.execute(query,value)
            row=cur.fetchone()
            #print(row)

            if row==None:
                messagebox.showerror('my error','Please enter valid user name')
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title('Forget password')
                self.root2.geometry('340x450+610+170')

                l=Label(self.root2,text="forget password",font=('times new roman',20,'bold'),bg='white',fg='red')
                l.place(x=50,y=10)

                sec=Label(self.root2,text='Select security question',font=('times new roman',15,'bold'),bg='white')
                sec.place(x=50,y=80)


                self.combo_sec=ttk.Combobox(self.root2,font=('times new roman',15,'bold'),state='readonly')
                self.combo_sec['values']=('select','your birth place','your bestfriend name','your pet name')
                self.combo_sec.current(0)
                self.combo_sec.place(x=50,y=110,width=250)
        

                
                sec_ans=Label(self.root2,text='Security Answer',font=('times new roman',15,'bold'),bg='white')
                sec_ans.place(x=50,y=150)

                self.sq=StringVar
                sec_entry=ttk.Entry(self.root2,textvariable=self.sq,font=('times new roman',15))
                sec_entry.place(x=50,y=180,width=250)

                
                passw=Label(self.root2,text='New Password',font=('times new roman',15,'bold'),bg='white')
                passw.place(x=50,y=220)

                self.password=StringVar
                p_entry=ttk.Entry(self.root2,textvariable=self.password,font=('times new roman',15))
                p_entry.place(x=50,y=250,width=250)

                btn=Button(self.root2,text='Reset',command=self.reset,font=('times new roman',15),fg='white',bg='green')
                btn.place(x=100,y=300)

                
class register:
    def __init__(self,root):
        self.root=root
        self.root.title('Register')
        self.root.geometry('1600x900+0+0')

       #*******vaiables****
        self.fname=StringVar()
        self.lname=StringVar()
        self.contact=StringVar()
        self.email=StringVar()
        self.sq=StringVar()
        self.sa=StringVar()
        self.passw=StringVar()
        self.cp=StringVar()



        #***********main frame******
        frame=Frame(self.root,bg='white')
        frame.place(x=10,y=50,width=800,height=550)

        reg_lbl=Label(frame,text='REGISTER HERE',font=('times new roman',20,'bold'),fg='darkgreen')
        reg_lbl.place(x=20,y=20)

        #********label and entry******

        #first row
        fname=Label(frame,text='First Name',font=('times new roman',15,'bold'),bg='white')
        fname.place(x=50,y=100)

        fname_entry=ttk.Entry(frame,textvariable=self.fname,font=('times new roman',15))
        fname_entry.place(x=50,y=130,width=250)

        lname=Label(frame,text='Last Name',font=('times new roman',15,'bold'),bg='white')
        lname.place(x=370,y=100)

        lname_entry=ttk.Entry(frame,textvariable=self.lname,font=('times new roman',15))
        lname_entry.place(x=370,y=130,width=250)


        #second row
        con=Label(frame,text='Contact No',font=('times new roman',15,'bold'),bg='white')
        con.place(x=50,y=170)

        c_entry=ttk.Entry(frame,textvariable=self.contact,font=('times new roman',15))
        c_entry.place(x=50,y=200,width=250)


        email=Label(frame,text='Email',font=('times new roman',15,'bold'),bg='white')
        email.place(x=370,y=170)

        e_entry=ttk.Entry(frame,textvariable=self.email,font=('times new roman',15))
        e_entry.place(x=370,y=200,width=250)


        #third row
        sec=Label(frame,text='Select security question',font=('times new roman',15,'bold'),bg='white')
        sec.place(x=50,y=240)

        self.combo_sec=ttk.Combobox(frame,textvariable=self.sq,font=('times new roman',15,'bold'),state='readonly')
        self.combo_sec['values']=('select','your birth place','your bestfriend name','your pet name')
        self.combo_sec.current(0)
        self.combo_sec.place(x=50,y=270,width=250)
        

        sec_ans=Label(frame,text='Security Answer',font=('times new roman',15,'bold'),bg='white')
        sec_ans.place(x=370,y=240)

        sec_entry=ttk.Entry(frame,textvariable=self.sa,font=('times new roman',15))
        sec_entry.place(x=370,y=270,width=250)

        #fourth row
        passw=Label(frame,text='Password',font=('times new roman',15,'bold'),bg='white')
        passw.place(x=50,y=310)

        p_entry=ttk.Entry(frame,textvariable=self.passw,font=('times new roman',15))
        p_entry.place(x=50,y=340,width=250)


        cp=Label(frame,text='Confirm password',font=('times new roman',15,'bold'),bg='white')
        cp.place(x=370,y=310)

        e_entry=ttk.Entry(frame,textvariable=self.cp,font=('times new roman',15))
        e_entry.place(x=370,y=340,width=250)


        #************checkbox****
        self.var_check=IntVar()
        checkbtn=Checkbutton(frame,variable=self.var_check,text='I Agree The Terms And Conditions',font=('times new roman',12),onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=380)


        #butoons
        img=Image.open(r'C:\Users\MAMATA\Desktop\pip\reg.jpg')
        img=img.resize((200,60),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimage1,borderwidth=0,command=self.register_data,cursor='hand2',font=('times new roman',15,'bold'))
        b1.place(x=10,y=420,width=200)

             
        img1=Image.open(r'C:\Users\MAMATA\Desktop\pip\last.jpg')
        img1=img1.resize((200,63),Image.ANTIALIAS)
        self.photoimage2=ImageTk.PhotoImage(img1)
        b2=Button(frame,image=self.photoimage2,borderwidth=0,command=self.login,cursor='hand2',font=('times new roman',15,'bold'))
        b2.place(x=350,y=420,width=200)


    #function declaration
    def register_data(self):
        if self.fname.get()=="" or self.email.get()=="" or self.sq.get()=='selct':
            messagebox.showerror('error','All fields required',parent=self.root)
        elif self.passw.get()!=self.cp.get():
            messagebox.showerror('error','Password and confirm password must be same',parent=self.root)
        elif self.var_check.get()==0:
             messagebox.showerror('error','Please agree our terms and conditions',parent=self.root)
        else:
            conn=connect(host='localhost',user='root',password='8310728642',database='mam')
            cur=conn.cursor()
            query=('select * from register where email=%s')
            value=(self.email.get(),)
            cur.execute(query,value) 

            row=cur.fetchone()
            if row!=None:
                messagebox.showerror('error','User already exits,please try another email',parent=self.root)
            else:
                cur.execute('insert into register values(%s,%s,%s,%s,%s,%s,%s)',(\
                    self.fname.get(),self.lname.get(),\
                    self.contact.get(),self.email.get(),\
                    self.sq.get(),self.sa.get(),self.passw.get()))
            conn.commit()
            conn.close()
            messagebox.showinfo('info','Registerd successfully',parent=self.root)
            

            
                
            

        

        
        
        

        

if __name__=='__main__':
    main()
