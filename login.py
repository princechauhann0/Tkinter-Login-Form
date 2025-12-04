from tkinter import *
import tkinter.messagebox as messagebox
from PIL import ImageTk,Image

def Handel_Btn():
    username = user_input.get()
    password = user_inputpass.get()

    if username and password :
        if username == "admin" and password == "1234" :
            messagebox.showinfo("valid","Succesfully Login!")
        else:
            messagebox.showerror("Invaild!","Wrong Creditionals")
       
    else:
        messagebox.showerror("Invalid","Empty Creditionals")


root = Tk()
root.title('Login Form')
root.iconbitmap(r"asdkhh1.ico")   # .ico file is used for logo other wuse iut will throw error
# root.geometry("300x300")
root.maxsize(500,500)
root.minsize(300,300)
# root.configure(background="aqua")



image_path = Image.open(r"asdkhh.jpg")
image_path = ImageTk.PhotoImage(image_path)
image_Label = Label(root, image=image_path )
image_Label.pack()



user_label=Label(root,text="Enter User id")
user_label.config(font=("Poppins",20),fg="red",bg="aqua")
user_label.pack(anchor=W, padx=10, pady=10)

# User input
user_input= Entry(root)
# user_input.config(ipadx=10,ipady=10)
user_input.pack(anchor=W, padx=10, pady=10, ipadx=20, ipady=10)

user_pass=Label(root,text="Enter password")
user_pass.config(font=("Poppins",20),fg="red",bg="aqua")
user_pass.pack(anchor=W, padx=10, pady=10)

# User Password
user_inputpass= Entry(root)
user_inputpass.pack(anchor=W, padx=10, pady=10 ,ipadx=20, ipady=10 )

variable_submitbtn = Button(text="submit",command=Handel_Btn)
variable_submitbtn.pack(anchor=W, padx=10, pady=10)


root.mainloop()