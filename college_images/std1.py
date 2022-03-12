from tkinter import*
from tkinter import ttk
from tkinter import font
from PIL import Image,ImageTk

class student:
    def __init__(self,root):
        self.root=root
        self.root.geometry('1530x790+0+0')
        self.root.title('Student Management System')


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

         #    label title
        lbl_title=Label(lbl_bg,text='STUDENT MANAGEMENT SYSTEM',font=("times new roma",37,"bold"),bg='white',fg='blue')
        lbl_title.place(x=0,y=0,width=1530,height=50)

        # manage frame
        manag_frame=Frame(lbl_bg,relief=RIDGE,bg='white')
        manag_frame.place(x=15,y=55,width=1500,height=560)

        # left frame
        left_frame = LabelFrame(manag_frame,bd=4,relief=RIDGE,padx=2,text='Student Information',font=("times new roma",17,"bold"),bg='white',fg='red')
        left_frame.place(x=10,y=10,width=660,height=540)

        # img
        img4=Image.open(r"college_images\3rd.jpg")
        img4=img4.resize((650,120),Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        self.lbl4=Label(left_frame,image=self.photoimg4,bd=2,relief=RIDGE)
        self.lbl4.place(x=0,y=0,width=650,height=120)

        
        # right frame
        right_frame = LabelFrame(manag_frame,bd=4,relief=RIDGE,padx=2,text='Student Information',font=("times new roma",17,"bold"),bg='white',fg='red')
        right_frame.place(x=680,y=10,width=800,height=540)

        # current course label
        std_lbl_info = LabelFrame(left_frame,bd=4,relief=RIDGE,padx=2,text='Current Course Information',font=("times new roma",15,"bold"),bg='white',fg='red')
        std_lbl_info.place(x=0,y=120,width=650,height=115)

        # Labels
        lbl_dept = Label(std_lbl_info,text="Department",font=("arial",12,"bold"),bg='white')
        lbl_dept.grid(row=0,column=0,padx=2,sticky=W)

        # combo 
        dept_combo = ttk.Combobox(std_lbl_info,width=17,font=("arial",12,"bold"))
        dept_combo.grid(row=0,column=1)
       



if __name__=="__main__":
    root=Tk()
    obj = student(root)
    root.mainloop()
