import socket
from tkinter import *
from tkinter import messagebox
window1 = Tk()
window1.title("Client")
window1.geometry("400x200")
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
######################## IP CONNECT ####################
def Connect():
    port = 80
    while True:
        try:
            s.connect((host.get(),port))
            messagebox.showinfo("Status", "Successfully")
            break
        except:
           messagebox.showinfo("Status", "Unsuccessfully")
           break

host = StringVar(window1)
Label_IP = Label(window1, text = "IP", fg = "blue2", font = "Arial")
Label_IP.place(x = 10, y = 30)

Entry_IP = Entry(window1, bd = 3,textvariable = host, bg = "AntiqueWhite4", width = 30)
Entry_IP.place(x = 50, y = 30)

btn_cnt = Button(window1, text = "Connect", fg = "navy", bg = "snow")
btn_cnt.place(x = 250, y = 30) 
#btn_cnt["command"] = Connect

btn_lgin = Button(window1, text = "Log in", fg = "navy", bg = "snow", width = 10)
btn_lgin.place(x = 60, y = 80)

btn_sgin = Button(window1, text = "Sign in", fg = "navy", bg = "snow", width = 10)
btn_sgin.place(x = 140, y = 80)

################ LOG IN #########################
def LogIn():
    window_lgin = Toplevel(window1)
    window_lgin.title("Log in")
    window_lgin.geometry("400x200")

    usn = StringVar(window_lgin)
    pwd = StringVar(window_lgin)

    Label_usn = Label(window_lgin, text = "Username")
    Label_usn.place( x = 40, y = 60)

    Label_pwd = Label(window_lgin, text = "Password")
    Label_pwd.place( x = 40, y = 100)

    Entry_usn = Entry(window_lgin, textvariable = usn, width = 30)
    Entry_usn.place(x = 110, y = 60)

    Entry_pwd = Entry(window_lgin, textvariable = pwd, width = 30)
    Entry_pwd.place(x = 110, y = 100)

    btn_submit = Button(window_lgin, text = "Submit")
    btn_submit.place(x = 40, y = 130)
    window_lgin.mainloop()
btn_lgin['command'] = LogIn

######################### SIGN IN ###########################
def Check(a,b):
    if a == b:
        messagebox.showinfo("Status","Sign in success")
    else:
        messagebox.showinfo("Status","Sign in error")
def SignIn():
    window_sgin = Toplevel(window1)
    window_sgin.title("Sign in")
    window_sgin.geometry("400x200")

    usn = StringVar(window_sgin)
    pwd = StringVar(window_sgin)
    pwd2 = StringVar(window_sgin)

    Label_usn = Label(window_sgin, text = "Username")
    Label_usn.place( x = 40, y = 30)

    Label_pwd = Label(window_sgin, text = "Password")
    Label_pwd.place( x = 40, y = 70)

    Label_pwd2 = Label(window_sgin, text = "Re-enter password")
    Label_pwd2.place( x = 40, y = 110)

    Entry_usn = Entry(window_sgin, textvariable = usn, width = 30)
    Entry_usn.place(x = 150, y = 30)

    Entry_pwd = Entry(window_sgin, textvariable = pwd, width = 30)
    Entry_pwd.place(x = 150, y = 70)

    Entry_pwd2 = Entry(window_sgin, textvariable = pwd2, width = 30)
    Entry_pwd2.place(x = 150, y = 110)

    btn_submit = Button(window_sgin, text = "Submit")
    btn_submit.place(x = 40, y = 160)
    #btn_submit['command'] = lambda: Check(pwd, pwd2)

    window_sgin.mainloop()
btn_sgin['command'] = SignIn

window1.mainloop()