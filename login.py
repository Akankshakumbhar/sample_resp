from tkinter import *
from tkinter import ttk
from  PIL import Image,ImageTk
class LoginWindow:
                   def __init__(self,root):
                           self.root=root
                           self.root.title("Login")
                           self.root.geometry("150x80+0+0")
                           self.bg=ImageTk.PhotoImage(file='cat1.jpg')
                           bg_lbl=Label(self.root,image=self.bg,bd=1,relief=RAISED)
                           bg_lbl.place(x=0,y=0,relwidth=3,relheight=1)

                           logo_img=Image.open('horse.jpg')
                           logo_img=logo_img.resize((40,40),Image.ADAPTIVE)
                           self.Photo_logo=ImageTk.PhotoImage(logo_img)

                           #title Frame
                           title_frame=Frame(self.root,bd=1,relief=RIDGE)
                           title_frame.place(x=450,y=28,width=550,height=60)
                           title_label=Label(title_frame,image=self.Photo_logo,compound=LEFT,text='User Login  form',font=('times new roman',30,'bold'),fg='darkblue')
                           title_label.place(x=10,y=10)




                           #information frame
                           main_frame=Frame(self.root,bd=1,relief=RIDGE)
                           main_frame.place(x=450,y=110,width=550,height=600)
                           #username
                           username=Label(main_frame,text='username',font=('times new roman',16,'bold'))
                           username.grid(row=0,column=0,padx=10,pady=10,sticky=W)
                           # textbox of user
                           user_entry=ttk.Entry(main_frame,font=('times new roman',16,'bold'),width=25)
                           user_entry.grid(row=0,column=1,padx=10,pady=10,sticky=W)
                            # email
                           email=Label(main_frame,text='email',font=('times new roman',16,'bold'))
                           email.grid(row=1,column=0,padx=10,pady=10,sticky=W)
                           #textbox of email
                           email_entry=ttk.Entry(main_frame,font=('times new roman',16,'bold'),width=25)
                           email_entry.grid(row=1,column=1,padx=10,pady=10,sticky=W)
                           #contact

                           contact=Label(main_frame,text='contact',font=('times new roman',16,'bold'))
                           contact.grid(row=2,column=0,padx=10,pady=10,sticky=W)
                           # text box for contact
                           contact_entry=ttk.Entry(main_frame,font=('times new roman',16,'bold'),width=25)
                           contact_entry.grid(row=2,column=1,padx=10,pady=10,sticky=W)
                           #gender
                        
                           # id number
                           id=Label(main_frame,text='id number',font=('times new roman',16,'bold'))
                           id.grid(row=3,column=0,padx=10,pady=10,sticky=W)
                           
                           

                           # text boxidnumber
                           id_entry=ttk.Entry(main_frame,font=('times new roman',16,'bold'),width=25)
                           id_entry.grid(row=3,column=1,padx=10,pady=10,sticky=W)
                           # password

                           Password=Label(main_frame,text='password',font=('times new roman',16,'bold'))
                           Password.grid(row=4,column=0,padx=10,pady=10,sticky=W)
                           Password_entry=ttk.Entry(main_frame,font=('times new roman',16,'bold'),width=25)
                           Password_entry.grid(row=4,column=1,padx=10,pady=10,sticky=W)
                           #gender
                           gender=Label(main_frame,text='password',font=('times new roman',16,'bold'))
                           gender.grid(row=4,column=0,padx=10,pady=10,sticky=W)
                           



                           



                           
                           
                           

                           
                            








if __name__=='__main__':
        root=Tk()
        obj=LoginWindow(root)
        root.mainloop()

        
                      


                     
