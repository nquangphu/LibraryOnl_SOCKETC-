import socket
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
window1 = Tk()
window1.title("Client")
window1.geometry("600x400")
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
######################## IP CONNECT ####################
def Exit(window):
    window.destroy()
def Send(data):
    s.send(data.encode())

def Connect(host):
    port = 80
    try:
        s.connect((str(host),port))
        messagebox.showinfo("Status", "Successfully")
    except:
        messagebox.showinfo("Status", "Unsuccessfully")
img_tmp = Image.open("image.jpg")
img_tmp = img_tmp.resize((500, 135), Image.ANTIALIAS)
img = ImageTk.PhotoImage(img_tmp)
panel = Label(window1, image = img)
panel.pack(ipady = 10)
Label_IP = Label(window1, text = "IP", fg = "blue2", font = "Arial")
Label_IP.place(x = 130, y = 155)


Entry_IP = Entry(window1, bd = 3, bg = "AntiqueWhite4", width = 40)
#Entry_IP.place(x = 50, y = 30
Entry_IP.pack()

btn_cnt = Button(window1, text = "Connect", fg = "navy", bg = "snow", width = 10)
btn_cnt.place(x = 450, y = 155)

btn_cnt["command"] = lambda: Connect(Entry_IP.get())


btn_sgin = Button(window1, text = "Sign in", fg = "navy", bg = "snow", width = 10)
btn_sgin.place(x = 220, y = 220)

btn_sgup = Button(window1, text = "Sign up", fg = "navy", bg = "snow", width = 10)
btn_sgup.place(x = 300, y = 220)

################ SIGN IN #########################
def Sub(kind,usn, pwd):
    print(kind + "+" + usn + "+" + pwd)
    Send(kind + "+" + usn + "+" + pwd)
    data = s.recv(1024).decode("utf-8")
    if data == "Success":
        messagebox.showinfo("Status", "Successfully")
        window_sch()

    else:
        messagebox.showinfo("Status", "Unsuccessfully")
def SignIn():
    window_sgin = Toplevel(window1)
    window_sgin.title("Sign in")
    window_sgin.geometry("400x200")

    Label_usn = Label(window_sgin, text = "Username")
    Label_usn.place( x = 40, y = 60)

    Label_pwd = Label(window_sgin, text = "Password")
    Label_pwd.place( x = 40, y = 100)

    Entry_usn = Entry(window_sgin, width = 30)
    Entry_usn.place(x = 110, y = 60)

    Entry_pwd = Entry(window_sgin, width = 30, show = '*')
    Entry_pwd.place(x = 110, y = 100)

    btn_submit = Button(window_sgin, text = "Submit", command = lambda: Sub("Signin",Entry_usn.get(), Entry_pwd.get()))
    btn_submit.place(x = 40, y = 130)
    
    window_sgin.mainloop()

#################### SIGN UP ####################################

def Check_pwd(usn, pwd1, pwd2):
    if pwd1 == pwd2:
        Sub("Signup", usn, pwd2)
    else:
        messagebox.showinfo("Status", "Password incorrect")
       
def SignUp():
    window_sgup = Toplevel(window1)
    window_sgup.title("Sign Up")
    window_sgup.geometry("400x200")
    

    Label_usn = Label(window_sgup, text = "Username")
    Label_usn.place( x = 40, y = 30)

    Label_pwd = Label(window_sgup, text = "Password")
    Label_pwd.place( x = 40, y = 70)

    Label_pwd2 = Label(window_sgup, text = "Re-enter password")
    Label_pwd2.place( x = 40, y = 110)

    Entry_usn = Entry(window_sgup, width = 30)
    Entry_usn.place(x = 150, y = 30)

    Entry_pwd = Entry(window_sgup, width = 30, show = '*')
    Entry_pwd.place(x = 150, y = 70)

    Entry_pwd2 = Entry(window_sgup, width = 30, show = '*')
    Entry_pwd2.place(x = 150, y = 110)

    btn_submit = Button(window_sgup, text = "Submit")
    btn_submit.place(x = 40, y = 160)
    btn_submit['command'] = lambda: Check_pwd(Entry_usn.get(), Entry_pwd.get(), Entry_pwd2.get())
    
    window_sgup.mainloop()
btn_sgin['command'] = SignIn
btn_sgup['command'] = SignUp
############# SEARCH ############################### id ten tacgia  namsx tl 1+tv1+NVA++GK
def Sub2(a,b,c,d):
    Send(a + "+" + b + "+" + c + "++" + d)
    data = s.recv(1024).decode("utf-8")
    if data == "Not found":
        messagebox.showinfo("Status", "Not found!")
    else:
        print(data)
        View(data)
def window_sch():
    window_sch = Tk()
    window_sch.title("Search")
    window_sch.geometry("400x400")
    Label_sch = Label(window_sch, text = "ONLINE LIBRARY", font = "Arial", fg = "maroon2")
    Label_sch.place(x = 130, y = 30)

    Label_ID = Label(window_sch, text = "F_ID", fg = "light sea green", font = "Arial")
    Label_ID.place(x = 20, y = 80)

    Label_Name = Label(window_sch, text = "F_Name", fg = "light sea green", font = "Arial")
    Label_Name.place(x = 20, y = 130)

    Label_Type = Label(window_sch, text = "F_Type", fg = "light sea green", font = "Arial")
    Label_Type.place(x = 20, y = 180)

    Label_Author = Label(window_sch, text = "F_Author", fg = "light sea green", font = "Arial")
    Label_Author.place(x = 20, y = 230)

    Entry_ID = Entry(window_sch, width = 30)
    Entry_ID.place(x = 130, y = 80)

    Entry_Name = Entry(window_sch, width = 30)
    Entry_Name.place(x = 130, y = 130)

    Entry_Type = Entry(window_sch, width = 30)
    Entry_Type.place(x = 130, y = 180)

    Entry_Author = Entry(window_sch, width = 30)
    Entry_Author.place(x = 130, y = 230)

    btn_sch = Button(window_sch, text = "Search", font = "Arial", bg = "green2", width = 10)
    btn_sch.place(x = 40, y = 300)
    btn_sch['command'] = lambda: Sub2(Entry_ID.get(), Entry_Name.get(), Entry_Author.get(), Entry_Type.get())


    btn_ext = Button(window_sch, text = "Exit", font = "Arial", bg = "red2", width = 10)
    btn_ext.place(x = 240, y = 300)
    btn_ext['command'] = lambda: Exit(window_sch)

    window_sch.mainloop()
################################# VIEW ############################
def View(data):        # 10.126.1.174
    window_view = Tk()
    window_view.title("Viewbook")
    window_view.geometry("1000x500")
    frame_view = Frame(window_view)
    frame_view.pack(side = TOP)
    Label_data = Label(frame_view, text = data)
    Label_data.pack(side = LEFT)
    #Label_data.grid(padx = 10, pady = 10)
    scrb_view = Scrollbar(frame_view, orient = VERTICAL)
    scrb_view.pack(side = RIGHT, fill = Y)
    window_view.mainloop()
window1.mainloop()