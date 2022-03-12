from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import random
from tkinter import messagebox 
import mysql.connector



class student:
    def __init__(self,root):
        self.root=root
        self.root.geometry('1530x790+0+0')
        self.root.title('Student Management System')

        # variables
        self.var_dept=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()        
        self.var_sem=StringVar()
        self.var_stdid=StringVar()
        self.var_name=StringVar()
        self.var_father=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_addr=StringVar()
        self.var_dob=StringVar()
        self.var_gen=StringVar()


         # first image
        img=Image.open(r"college_images\7th.jpg")
        img=img.resize((510,160),Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        self.btn=Button(self.root,image=self.photoimg,cursor="hand2",)
        self.btn.place(x=0,y=0,width=510,height=160)


         # second image
        img1=Image.open(r"college_images\5th.jpg")
        img1=img1.resize((510,160),Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        self.btn1=Button(self.root,image=self.photoimg1,cursor="hand2",)
        self.btn1.place(x=510,y=0,width=510,height=160)


         # Third image
        img2=Image.open(r"college_images\6th.jpg")
        img2=img2.resize((510,160),Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        self.btn2=Button(self.root,image=self.photoimg2,cursor="hand2",)
        self.btn2.place(x=1020,y=0,width=510,height=160)

        # Background image
        img3=Image.open(r"college_images\university.jpg")
        img3=img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        lbl_bg = Label(self.root,image=self.photoimg3,border=2,relief=RIDGE)
        lbl_bg.place(x=0,y=160,width=1530,height=710)

         #   title label
        lbl_title=Label(lbl_bg,text='STUDENT MANAGEMENT SYSTEM',font=("times new roma",38,"bold"),bg='white',fg='blue')
        lbl_title.place(x=0,y=0,width=1530,height=49)

        # manage frame
        manag_frame=Frame(lbl_bg,relief=RIDGE,bg='white')
        manag_frame.place(x=15,y=53,width=1500,height=560)

        # left frame
        left_frame = LabelFrame(manag_frame,bd=4,relief=RIDGE,padx=2,text='Student Information',font=("times new roma",17,"bold"),bg='white',fg='red')
        left_frame.place(x=10,y=10,width=660,height=540)

        # img
        img4=Image.open(r"college_images\3rd.jpg")
        img4=img4.resize((650,120),Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        self.lbl4=Label(left_frame,image=self.photoimg4,bd=2,relief=RIDGE)
        self.lbl4.place(x=0,y=0,width=650,height=120)

        
        
        # current course label
        std_lbl_info = LabelFrame(left_frame,bd=4,relief=RIDGE,padx=2,text='Current Course Information',font=("times new roma",15,"bold"),bg='white',fg='green')
        std_lbl_info.place(x=0,y=120,width=650,height=115)

        # Label and combo for dept
        lbl_dept = Label(std_lbl_info,text="Department",font=("arial",12,"bold"),bg='white')
        lbl_dept.grid(row=0,column=0,padx=2,sticky=W)

        combo_dept = ttk.Combobox(std_lbl_info,textvariable=self.var_dept,font=("arial",12,"bold"),state="readonly",width=17)
        combo_dept["value"]=("select department","Physical","Biological")
        combo_dept.current(0)
        combo_dept.grid(row=0,column=1,padx=2,pady=10)


        # course
        lbl_course = Label(std_lbl_info,text="Course",font=("arial",12,"bold"),bg='white')
        lbl_course.grid(row=0,column=2,padx=2,pady=10,sticky=W)

        combo_course = ttk.Combobox(std_lbl_info,textvariable=self.var_course,font=("arial",12,"bold"),state="readonly",width=17)
        combo_course["value"]=("select course","PCM","PME","PMCS","CBZ","MCZ",)
        combo_course.current(0)
        combo_course.grid(row=0,column=3,padx=2,pady=10)

        # year
        lbl_year = Label(std_lbl_info,text="Year",font=("arial",12,"bold"),bg='white')
        lbl_year.grid(row=1,column=0,padx=2,sticky=W)

        combo_year = ttk.Combobox(std_lbl_info,textvariable=self.var_year,font=("arial",12,"bold"),state="readonly",width=17)
        combo_year["value"]=("select year","1st year","2nd year","3rd year")
        combo_year.current(0)
        combo_year.grid(row=1,column=1,padx=2,pady=10)

        # semester
        lbl_sem = Label(std_lbl_info,text="Semester",font=("arial",12,"bold"),bg='white')
        lbl_sem.grid(row=1,column=2,padx=2,sticky=W)

        combo_sem = ttk.Combobox(std_lbl_info,textvariable=self.var_sem,font=("arial",12,"bold"),state="readonly",width=17)
        combo_sem["value"]=("select semester", "1 sem","2 sem","3 sem","4 sem","5 sem","6 sem")
        combo_sem.current(0)
        combo_sem.grid(row=1,column=3,padx=2,pady=10)

        # student details frame label
        std_det_info = LabelFrame(left_frame,bd=4,relief=RIDGE,padx=2,text='Student information',font=("times new roma",15,"bold"),bg='white',fg='green')
        std_det_info.place(x=0,y=240,width=650,height=210)

        # first row # id label
        id_lbl =Label(std_det_info,font=("arial",12,"bold"),bg="white",text="student ID : ")
        id_lbl.grid(row=0,column=0,padx=2,pady=10,sticky=W)

        id_entry = ttk.Entry(std_det_info,textvariable=self.var_stdid,font=("arial",12,"bold"),width=20)
        id_entry.grid(row=0,column=1,padx=2,sticky=W,pady=7)

        # name label
        name_lbl=Label(std_det_info,font=("arial",12,"bold"),bg="white",text="Name : ")
        name_lbl.grid(row=0,column=2,padx=2,pady=5,sticky=W)

        id_entry = ttk.Entry(std_det_info,textvariable=self.var_name,font=("arial",12,"bold"),width=20)
        id_entry.grid(row=0,column=3,padx=2,sticky=W,pady=7)

        # second row #dob label
        dob_lbl =Label(std_det_info,font=("arial",12,"bold"),bg="white",text="DOB : ")
        dob_lbl.grid(row=1,column=0,padx=2,pady=7,sticky=W)

        id_entry = ttk.Entry(std_det_info,textvariable=self.var_dob,font=("arial",12,"bold"),width=20)
        id_entry.grid(row=1,column=1,padx=2,sticky=W,pady=7)


        # Father label
        father_lbl =Label(std_det_info,font=("arial",12,"bold"),bg="white",text="Father Name : ")
        father_lbl.grid(row=1,column=2,padx=2,pady=7,sticky=W)

        id_entry = ttk.Entry(std_det_info,textvariable=self.var_father,font=("arial",12,"bold"),width=20)
        id_entry.grid(row=1,column=3,padx=2,pady=7,sticky=W)

        # third row # gender label
        gender_lbl =Label(std_det_info,font=("arial",12,"bold"),bg="white",text="Gender : ")
        gender_lbl.grid(row=2,column=0,padx=2,pady=7,sticky=W)

        combo_dept = ttk.Combobox(std_det_info,textvariable=self.var_gen,font=("arial",12,"bold"),state="readonly",width=18)
        combo_dept["value"]=("select gender","male","female")
        combo_dept.current(0)
        combo_dept.grid(row=2,column=1,padx=2,pady=7)

        # email label
        email_lbl =Label(std_det_info,font=("arial",12,"bold"),bg="white",text="Email : ")
        email_lbl.grid(row=2,column=2,padx=2,pady=7,sticky=W)

        email_entry = ttk.Entry(std_det_info,textvariable=self.var_email,font=("arial",12,"bold"),width=20)
        email_entry.grid(row=2,column=3,padx=2,pady=7,sticky=W)

        #fourth row  # phone label
        phone_lbl =Label(std_det_info,font=("arial",12,"bold"),text="Phone No : ",bg="white")
        phone_lbl.grid(row=3,column=0,padx=2,pady=7,sticky=W)

        phn_entry = ttk.Entry(std_det_info,textvariable=self.var_phone,font=("arial",12,"bold"),width=20)
        phn_entry.grid(row=3,column=1,padx=2,pady=7,sticky=W)

        # addr label
        addr_lbl =Label(std_det_info,font=("arial",12,"bold"),bg="white",text="Address : ")
        addr_lbl.grid(row=3,column=2,padx=2,pady=7,sticky=W)

        addr_entry = ttk.Entry(std_det_info,textvariable=self.var_addr,font=("arial",12,"bold"),width=20)
        addr_entry.grid(row=3,column=3,padx=2,pady=7,sticky=W)

        # frame 3
        f3 = Frame(left_frame,bd=2,padx=2,pady=5,bg="white")
        f3.place(x=0,y=450,width=650,height=45)

        # save btn
        save_btn = Button(f3,text="Save",command=self.add_data,font=("arial",13,"bold"),width=15,bg="cyan")
        save_btn.grid(row=0,column=0,padx=1,pady=2)

         # update btn
        upd_btn = Button(f3,text="Update",command=self.update,font=("arial",13,"bold"),width=15,bg="cyan")
        upd_btn.grid(row=0,column=1,padx=2,pady=2)

         # delete btn
        del_btn = Button(f3,text="Delete",command=self.delete,font=("arial",13,"bold"),width=15,bg="cyan")
        del_btn.grid(row=0,column=2,padx=2,pady=2)

         # reset btn
        reset_btn = Button(f3,text="Reset",command=self.reset,font=("arial",13,"bold"),width=14,bg="cyan")
        reset_btn.grid(row=0,column=3,padx=2,pady=2)


        # right frame
        right_frame = Frame(manag_frame,bd=4,relief=RIDGE,padx=2,bg='white')
        right_frame.place(x=680,y=10,width=800,height=540)

        # # img 
        img5=Image.open(r"college_images\11th.jpg")
        img5=img5.resize((790,200),Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        self.btn5=Button(right_frame,image=self.photoimg5,cursor="hand2",)
        self.btn5.place(x=0,y=0,width=790,height=200)

        # serach frame
        ser_fr = LabelFrame(right_frame,text="Search student Info",font=("arial",12,"bold"),bg="white",fg="red")
        ser_fr.place(x=0,y=205,width=790,height=60)

        # seacrh label
        serby_lbl =Label(ser_fr,font=("arial",12,"bold"),bg="green",text=" Search By",fg="white")
        serby_lbl.grid(row=0,column=0,padx=2,pady=2,sticky=W)

        ser_lbl =Label(ser_fr,font=("arial",12,"bold"),text="Std Id : ",fg="white",bg="red")
        ser_lbl.grid(row=0,column=1,padx=2,pady=7,sticky=W)

        

        self.var_ser = StringVar()
        ser_entry = ttk.Entry(ser_fr,textvariable=self.var_ser,font=("arial",12,"bold"),width=20)
        ser_entry.grid(row=0,column=2,padx=2,pady=2,sticky=W)

        # serch btn
        ser_btn=Button(ser_fr,text="Search",command=self.search,font=("arial",11,"bold"),width=12,bg="cyan")
        ser_btn.grid(row=0,column=3,padx=2,pady=2)

        # showall btn
        showall_btn=Button(ser_fr,text="Show all",command = self.fetch_data,font=("arial",11,"bold"),width=12,bg="cyan")
        showall_btn.grid(row=0,column=4,padx=2,pady=2)


        # ******************* student table and scroll bars****************
        tbl_fr = Frame(right_frame,padx=2,pady=2,bd=4,relief=RIDGE)
        tbl_fr.place(x=0,y=270,width=784,height=260)

        scrollx = ttk.Scrollbar(tbl_fr,orient=HORIZONTAL)      
        scrolly = ttk.Scrollbar(tbl_fr,orient=VERTICAL)

        self.std_tbl = ttk.Treeview(tbl_fr,columns=("dept","course","year","sem","stdid","Name","Dob","father","Gender","Email","phone","Address"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)

        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)

        scrollx.config(command=self.std_tbl.xview)
        scrolly.config(command=self.std_tbl.yview)

        self.std_tbl.heading("dept",text="Dept")
        self.std_tbl.heading("course",text="course")
        self.std_tbl.heading("year",text="year")
        self.std_tbl.heading("sem",text="sem")
        self.std_tbl.heading("Name",text="Name")
        self.std_tbl.heading("stdid",text="Std Id")
        self.std_tbl.heading("Dob",text="DOB")
        self.std_tbl.heading("father",text="Father Name")
        self.std_tbl.heading("Gender",text="Gender")
        self.std_tbl.heading("Email",text="Email")
        self.std_tbl.heading("phone",text="Phone")
        self.std_tbl.heading("Address",text="Address")
        
        self.std_tbl["show"]="headings"

        self.std_tbl.column("dept",width=100)
        self.std_tbl.column("course",width=100)
        self.std_tbl.column("year",width=100)
        self.std_tbl.column("sem",width=100)
        self.std_tbl.column("stdid",width=100)
        self.std_tbl.column("Name",width=100)
        self.std_tbl.column("Dob",width=100)
        self.std_tbl.column("father",width=100)
        self.std_tbl.column("Gender",width=100)
        self.std_tbl.column("Email",width=100)
        self.std_tbl.column("phone",width=100)
        self.std_tbl.column("Address",width=100)
        


        self.std_tbl.pack(fill=BOTH,expand=1)
        self.std_tbl.bind('<ButtonRelease-1>',self.get_cur)
    
        self.fetch_data()

        

        # ************ functions**********

    def add_data(self):
        if self.var_stdid.get()=="" or self.var_phone.get()=="":
            messagebox.showerror("error","all fields are required",parent=self.root)
        else:
            try:
               conn=mysql.connector.connect(host='localhost',username='root',passwd='8310728642',database='mam')
               my_cur=conn.cursor()
               my_cur.execute('insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(self.var_dept.get(),
                                                                                               self.var_course.get(),
                                                                                               self.var_year.get(),
                                                                                               self.var_sem.get(),
                                                                                               self.var_stdid.get(),
                                                                                               self.var_name.get(),
                                                                                               self.var_dob.get(),
                                                                                               self.var_father.get(),
                                                                                               self.var_gen.get(),
                                                                                               self.var_email.get(),
                                                                                               self.var_phone.get(),
                                                                                               self.var_addr.get()
                                                                                                ))
                  
               conn.commit()
               self.fetch_data()
               conn.close()
               
               messagebox.showinfo("success",'student has been added',parent=self.root)
            except Exception as es:
                messagebox.showwarning('warning',f'some thing went wrong:{str(es)}',parent=self.root)

    
    def fetch_data(self):
        conn=mysql.connector.connect(host='localhost',username='root',passwd='8310728642',database='mam')
        my_cur=conn.cursor()
        my_cur.execute("select * from student")
        data=my_cur.fetchall()
        if len(data)!=0:
            self.std_tbl.delete(*self.std_tbl.get_children())
            for i in data:
                self.std_tbl.insert("",END,values=i)
            conn.commit()
        conn.close()


    def get_cur(self,event=""):
        cur_row=self.std_tbl.focus()
        content=self.std_tbl.item(cur_row)
        data=content['values']

       
        self.var_dept.set(data[0])
        self.var_course.set(data[1])
        self.var_year.set(data[2])        
        self.var_sem.set(data[3])
        self.var_stdid.set(data[4])
        self.var_name.set(data[5])
        self.var_dob.set(data[6])
        self.var_father.set(data[7])
        self.var_gen.set(data[8])
        self.var_email.set(data[9])
        self.var_phone.set(data[10])
        self.var_addr.set(data[11])


    def update(self):
        if self.var_stdid.get()=="" or self.var_phone.get()=="":
            messagebox.showerror('error','please enter the fields number',parent=self.root)
        else:
            conn=mysql.connector.connect(host='localhost',username='root',passwd='8310728642',database='mam')
            my_cur=conn.cursor()
            my_cur.execute('update student set dept=%s,course=%s,sem=%s,year=%s,name=%s,dob=%s,father=%s,gender=%s,email=%s,phone=%s,address=%s where stdid=%s',(self.var_dept.get(),
                                                                                                                                                                 self.var_course.get(),
                                                                                                                                                                 self.var_year.get(),
                                                                                                                                                                 self.var_sem.get(),
                                                                                                                                                                 self.var_name.get(),
                                                                                                                                                                self.var_dob.get(),
                                                                                                                                                                   self.var_father.get(),
                                                                                                                                                                   self.var_gen.get(),
                                                                                                                                                                   self.var_email.get(),
                                                                                                                                                                   self.var_phone.get(),
                                                                                                                                                                   self.var_addr.get(),
                                                                                                                                                                   self.var_stdid.get()))
                                                                                                                                                                  
                                                                                                                                                                 
                                                                                                                                                                              
                                                                                                                                                                               
                                                                                                                                                                 
                           
                                                                                                                                                                 
                                                                                                                                                                                                                                                                                           
                                                                                                            
                                                                                               
            conn.commit()
            self.fetch_data()
            messagebox.showinfo('info','student details has been updated',parent=self.root)
            conn.close()


    def delete(self):
        
        mdelete=messagebox.askyesno("Delete","do you want to delete this customer",parent=self.root)
        if mdelete>0:
            conn=mysql.connector.connect(host='localhost',username='root',passwd='8310728642',database='mam')
            my_cur=conn.cursor()
            query="delete from student Where stdid =%s"
            value=(self.var_stdid.get(),)
            my_cur.execute(query,value)
            conn.commit()
            self.fetch_data()
            self.reset()
            conn.close()
            messagebox.showinfo('info','student  has been deleted')

        else:
            if not mdelete:
                return
        

    def reset(self):
            
        self.var_dept.set("select Dept"),
        self.var_course.set("Select Course"),
        self.var_year.set("select year"),       
        self.var_sem.set("select sem"),
        self.var_stdid.set(""),
        self.var_name.set(""),
        self.var_father.set(""),
        self.var_email.set(""),
        self.var_addr.set(""),
        self.var_dob.set(""),
        self.var_gen.set("choose gender"),
        self.var_phone.set("")


    #************** search ********
    def search(self):
        if self.var_ser.get()=="":
            messagebox.showerror('error','please enter the fields ',parent=self.root)
        else:
            conn=mysql.connector.connect(host='localhost',username='root',passwd='8310728642',database='mam')
            my_cur=conn.cursor()
            my_cur.execute("select * from student where stdid like '%" +self.var_ser.get()+"%'") 
            data = my_cur.fetchall()   


            if len(data)!=0:
                self.std_tbl.delete(*self.std_tbl.get_children())
                for i in data:
                    self.std_tbl.insert("",END,values=i)
                    conn.commit()




if __name__=="__main__":
    root=Tk()
    obj=student(root)
    root.mainloop()
                
            
#str(self.var_com_ser.get()) + " LIKE '%"+str(self.var_ser.get())+"%'")

            
             
        
        
       












    
            
      
    
