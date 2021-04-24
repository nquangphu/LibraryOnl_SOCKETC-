from tkinter import *
from PIL import Image,ImageTk
import socket
from tkinter import messagebox

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

def Connect():
    port = 12345
    while True:
        try:
            s.connect((host.get(),port))
            messagebox.showinfo("Thông báo", "Kết nối thành công")
            break
        except:
           messagebox.showinfo("Thông báo", "Kết nối không thành công")
##
def Send(data):
    try: 
        s.send(data.encode())
    except:
        messagebox.showinfo("Thông báo", "Kết nối không thành công")
def Receive():
    return s.recv(1024)

table=Tk()
table.title("Client")
##nut ket noi
host=StringVar(table)

IP_address=Entry(table,textvariable=host,width=20)
IP_address.grid(row=0,column=0)

btn_cn= Button(table,text="Kết nối",width=10)
btn_cn.grid(row=0,column=1,pady=2)
btn_cn['command']  = Connect

##shutdown
def shutWind_cmd():
    Send("Shutdown")
btn_std=Button(table,text="Tắt máy",width=10,height=2,command=shutWind_cmd)
btn_std.grid(row=2,column=0,pady=2)
##
def exit_cmd():
    Send("Thoat")
    s.close()
    table.destroy()
btn_ext=Button(table,text="Thoát",width=10,height=2,command=exit_cmd)
btn_ext.grid(row=3,column=2,pady=2)
##
def screenShot_cmd():
    Send("Chup")
btn_scrst=Button(table,text="Chụp màn hình",width=15,height=2,command=screenShot_cmd)
btn_scrst.grid(row=2,column=1,pady=2)
##















##
app_running_button=Button(table,text="App Running",width=10,height=2)
app_running_button.grid(row=1,column=0,pady=2)
##


process_running_button=Button(table,text="Process Running",width=12,height=2)
process_running_button.grid(row=1,column=1,pady=2)




##








keystroke_button=Button(table,text="Keystroke",width=10,height=2)
keystroke_button.grid(row=1,column=2,pady=2)
##
registry_button=Button(table,text="Sửa registry",width=12,height=2)
registry_button.grid(row=2,column=2,pady=2)
##


table.mainloop()

