import socket
from tkinter import *
from tkinter import messagebox
window1 = Tk()
window1.title("Client")
window1.geometry("400x200")
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
######################## IP CONNECT ####################
def Send():
    s.send(data.encode())

def Receive():
    return s.recv(1024)

def Connect():
    port = 80
    while True:
        try:
            s.connect((host.get(),port))
            messagebox.showinfo("Status", "Successfully")
            return 1
            break
        except:
           messagebox.showinfo("Status", "Unsuccessfully")
           return 0
           break

host = StringVar(window1)
Label_IP = Label(window1, text = "IP", fg = "blue2", font = "Arial")
Label_IP.place(x = 10, y = 30)

Entry_IP = Entry(window1, bd = 3,textvariable = host, bg = "AntiqueWhite4", width = 30)
Entry_IP.place(x = 50, y = 30)

btn_cnt = Button(window1, text = "Connect", fg = "navy", bg = "snow")
btn_cnt.place(x = 250, y = 30) 
btn_cnt["command"] = Connect

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
    Send("signin"+str(usn)+str(pwd))
    window_lgin.mainloop()
# if Connect() == 1:
#     btn_lgin['command'] = LogIn

######################### SIGN IN ###########################
# def CheckAndSend(a,b,c):
#     if a == b:
#         messagebox.showinfo("Status","Sign in success")
#         Send("signup"+str(c),str(b))

#     else:
#         messagebox.showinfo("Status","Sign in error")
       
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
    btn_submit['command'] =  Send("signup"+str(usn),str(pwd2))
    
    window_sgin.mainloop()
if Connect() == 1:
    btn_sgin['command'] = SignIn
    btn_lgin['command'] = LogIn
############# SEARCH ###############################
# window_sch = Tk()
# window_sch.title("Search")
# window_sch.geometry("400x400")

# F_ID = StringVar(window_sch)
# F_Name = StringVar(window_sch)
# F_Type = StringVar(window_sch)
# F_Author = StringVar(window_sch)

# Label_sch = Label(window_sch, text = "ONLINE LIBRARY", font = "Arial", fg = "maroon2")
# Label_sch.place(x = 130, y = 30)

# Label_ID = Label(window_sch, text = "F_ID", fg = "light sea green", font = "Arial")
# Label_ID.place(x = 20, y = 80)

# Label_Name = Label(window_sch, text = "F_Name", fg = "light sea green", font = "Arial")
# Label_Name.place(x = 20, y = 130)

# Label_Type = Label(window_sch, text = "F_Type", fg = "light sea green", font = "Arial")
# Label_Type.place(x = 20, y = 180)

# Label_Author = Label(window_sch, text = "F_Author", fg = "light sea green", font = "Arial")
# Label_Author.place(x = 20, y = 230)

# Entry_ID = Entry(window_sch, textvariable = F_ID, width = 30)
# Entry_ID.place(x = 100, y = 80)

# Entry_Name = Entry(window_sch, textvariable = F_Name, width = 30)
# Entry_Name.place(x = 100, y = 130)

# Entry_Type = Entry(window_sch, textvariable = F_Type, width = 30)
# Entry_Type.place(x = 100, y = 180)

# Entry_Author = Entry(window_sch, textvariable = F_Author, width = 30)
# Entry_Author.place(x = 100, y = 230)

# btn_sch = Button(window_sch, text = "Search", font = "Arial", bg = "green2", width = 10)
# btn_sch.place(x = 40, y = 300)

# btn_ext = Button(window_sch, text = "Exit", font = "Arial", bg = "red2", width = 10)
# btn_ext.place(x = 240, y = 300)


# window_sch.mainloop()
################################# VIEW ############################

window1.mainloop()