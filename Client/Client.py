from tkinter import *
from PIL import Image,ImageTk
import socket
from tkinter import messagebox

##
def Send(data):
    try: 
        s.send(data.encode())
    except:
        messagebox.showinfo("Thông báo", "Kết nối không thành công")
def Receive():
    return s.recv(1024)

window = Tk()
window.title("Client")
window.geometry("380x300")


#--------- BUTTON KET NOI ---------#
def Connect():
    port = 12345
    while True:
        try:
            s.connect((host.get(),port))
            messagebox.showinfo("Thông báo", "Kết nối thành công")
            break
        except:
           messagebox.showinfo("Thông báo", "Kết nối không thành công")
           break

host = StringVar(window)
host.set("Nhập IP")

ip_addr = Entry(window, textvariable =  host, bd = 3, bg = "oldlace")
ip_addr.grid(row = 0, column = 0, ipadx = 50, ipady = 4, padx = 10, pady = 10)
print(host.get())

btn_connect = Button(window, text = "Kết nối", width = 15, bg = "lightgrey", activebackground = "dimgray", activeforeground = "white")
btn_connect.grid(row = 0, column = 1)
btn_connect['command']  = Connect

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)


#--------- BUTTON TẮT MÁY ---------#
def shutWind_cmd():
    Send("Shutdown")

btn_shdown = Button(window, text = "Tắt\nmáy", width = 6, height = 5, relief = GROOVE, 
                        activebackground = "royalblue", activeforeground = "white")
btn_shdown['command'] = shutWind_cmd
btn_shdown.place(relx = 0.275, rely = 0.43)


#--------- BUTTON THOÁT ---------#
def exit_cmd():
    Send("Thoat")
    s.close()
    window.destroy()

btn_ext = Button(window, text = "Thoát", width = 8, height = 4, relief = GROOVE, 
                        activebackground = "royalblue", activeforeground = "white")
btn_ext.place(relx = 0.78, rely = 0.73)
btn_ext['command'] = exit_cmd


#--------- BUTTON CHỤP MÀN HÌNH ---------#
def screenShot_cmd():
    Send("Chup")

btn_scrst = Button(window, text = "Chụp\nmàn hình", width = 10, height = 5, relief = GROOVE, 
                        activebackground = "royalblue", activeforeground = "white")
btn_scrst.place(relx = 0.43, rely = 0.43)
btn_scrst['command'] = screenShot_cmd


#--------- BUTTON APP RUNNING ---------#
btn_app_rng = Button(window, text = "App Running", width = 18, height = 4, relief = GROOVE, 
                        activebackground = "royalblue", activeforeground = "white")
btn_app_rng.place(relx = 0.275, rely = 0.18)


#--------- BUTTON PROCESS RUNNING ---------#
btn_prcs_rng = Button(window, text = "Process\nRunning", width = 11, height = 15, relief = GROOVE, 
                        activebackground = "royalblue", activeforeground = "white")
btn_prcs_rng.place(relx = 0.03, rely = 0.18)

btn_keystrk = Button(window, text = "Keystroke", width = 15, height = 10, relief = GROOVE, 
                        activebackground = "royalblue", activeforeground = "white")
btn_keystrk.place(relx = 0.65, rely = 0.18)


#--------- BUTTON SỬA REGISTRY ---------#
btn_rgt = Button(window, text = "Sửa registry", width = 25, height = 4, relief = GROOVE, 
                        activebackground = "royalblue", activeforeground = "white")
btn_rgt.place(relx = 0.275, rely = 0.73)


window.mainloop()

