from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector as mysql


def login():
    mysqldb=mysql.connect(host="localhost",user="root",password="Vikrant@23",database="lpu_db")
    mycursor=mysqldb.cursor()
    umsid=umsidval.get()
    password=passwordval.get()
    
    sql="select * from ums_login where umsid = %s and password = %s"
    mycursor.execute(sql,[(umsid),(password)])
    results = mycursor.fetchall()
    
    if results:
        MessageBox.showinfo("","login success")
    
        reg_page=Toplevel(root)
        reg_page.geometry('800x800')
        reg_page.config(bg="#FFD580")
        reg_page.title('REGISTRATION FORM FOR JOINING STUDENT ASSOCIATION')
    
    
        def on_click():
            f_name=f_nameval.get()
            l_name=l_nameval.get()
            email=emailval.get()
            address=addval.get()
            p_number=p_numberval.get()
    
            if(f_name=="" or l_name=="" or email=="" or address=="" or  p_number==""):
                MessageBox.showinfo("insert status","all fields are required");
            else:
                con=mysql.connect(host="localhost",user="root",password="Vikrant@23",database="lpu_db")
                cursor = con.cursor()
                cursor.execute("insert into reg_info values('{}','{}','{}','{}','{}')".format(f_name,l_name,email,address,p_number))
                cursor.execute("commit");
        
                MessageBox.showinfo("insert status"," inserted succesfully");
                con.close();
        
        
        
    #heading
        Label(reg_page,text="Registration Form",font ="ar 25 bold underline ",bg='yellow').grid(row=0,column=2)
    #field name
        f_name=Label(reg_page,text='FIRST NAME',font ="ar 15 bold",bg="orange").grid(row=1,column=0)
        l_name=Label(reg_page,text='LAST NAME',font ="ar 15 bold",bg="orange").grid(row=2,column=0)
        email=Label(reg_page,text='EMAIL',font ="ar 15 bold",bg="orange").grid(row=3,column=0,)
        add=Label(reg_page,text='ADDRESS',font ="ar 15 bold",bg="orange").grid(row=4,column=0)
        gender=Label(reg_page,text='GENDER',font ="ar 15 bold",bg="orange").grid(row=5,column=0)
        p_number=Label(reg_page,text='PHONE NUMBER',font ="ar 15 bold",bg="orange").grid(row=8,column=0)
    #variable for storing data
        f_nameval = StringVar()
        l_nameval = StringVar()
        emailval = StringVar()
        addval = StringVar()
        genderval = StringVar()
        p_numberval = StringVar()
    #viriable to store value for gender
        gen=IntVar()
    #creating entry field
        f_nameentry = Entry(reg_page , textvariable=f_nameval).grid(row=1,column=3)
        l_nameentry = Entry(reg_page , textvariable= l_nameval).grid(row=2,column=3)
        emailentry = Entry(reg_page , textvariable=emailval).grid(row=3,column=3)
        addentry = Entry(reg_page , textvariable=addval).grid(row=4,column=3)
    #radio button for gender
        gendermale = Radiobutton(reg_page,text='male',value=1,variable=gen).grid(row=5,column=3)
        grnderfemale= Radiobutton(reg_page,text='female',value=2,variable=gen).grid(row=5,column=4)
        grnderother= Radiobutton(reg_page,text='others',value=3,variable=gen).grid(row=5,column=5)
    
        p_numberentry = Entry(reg_page , textvariable= p_numberval).grid(row=8,column=3)
    
        Button(reg_page,text="submit",command=lambda:reg_page.destroy()).grid(row=10,column=2)
        Button(reg_page,text="update",command=on_click).grid(row=10,column=3)
    
    
        return true
    
    else:
        MessageBox.showinfo("","incorrect username or password")
        return false
    
    
    
root =Tk()


Label(root,text="login",font ="ar 25 bold underline ").grid(row=0,column=2)

umsid=Label(root,text='UMSID',font ="ar 15 bold",bg="orange").grid(row=1,column=0)
password=Label(root,text='PASSWORD',font ="ar 15 bold",bg="orange").grid(row=2,column=0)

umsidval = StringVar()
passwordval = StringVar()

umsidentry = Entry (root , textvariable=umsidval ).grid(row=1,column=3)
passwordentry = Entry (root , textvariable= passwordval,show="*").grid(row=2,column=3)

Button(text="login",command=login).grid(row=9,column=2)


root.geometry('800x500')
root.config(bg="#FFD580")
root.title('REGISTRATION FORM FOR JOINING STUDENT ASSOCIATION')


root.mainloop()
