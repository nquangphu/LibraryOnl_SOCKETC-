from tkinter import *
from PIL import Image,ImageTk
import socket
from tkinter import messagebox
import io
import tkinter.ttk
import os
from tkinter import filedialog
from configparser import ConfigParser
import pyautogui

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
window.geometry("450x400")
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

####################################
#--------- BUTTON KET NOI ---------#
def Connect():
    port = 80
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

btn_connect = Button(window, text = "Kết nối", width = 15, bg = "lightgrey", 
                        activebackground = "dimgray", activeforeground = "white")
btn_connect.grid(row = 0, column = 1)
btn_connect['command']  = Connect


####################################
#--------- BUTTON TẮT MÁY ---------#
def shutWind_cmd():
    Send("Shutdown")

btn_shdown = Button(window, text = "Tắt\nmáy", width = 6, height = 5, relief = GROOVE,  bg = "aqua",
                        activebackground = "royalblue", activeforeground = "white")
btn_shdown['command'] = shutWind_cmd
btn_shdown.place(relx = 0.275, rely = 0.43)


##################################
#--------- BUTTON THOÁT ---------#
def exit_cmd():
    Send("Thoat")
    s.close()
    window.destroy()

btn_ext = Button(window, text = "Thoát", width = 8, height = 4, relief = GROOVE,  bg = "red",
                        activebackground = "royalblue", activeforeground = "white")
btn_ext.place(relx = 0.78, rely = 0.73)
btn_ext['command'] = exit_cmd


##########################################
#--------- BUTTON CHỤP MÀN HÌNH ---------#

def Change(newwind, panel):
    my_img1 = pyautogui.screenshot()
    my_img1.save("image.png")

    screen_cap1 = Image.open("image.png")
    screen_cap1 = screen_cap1.resize((450, 360), Image.ANTIALIAS)
    img1 = ImageTk.PhotoImage(screen_cap1)

    panel.configure(image = img1)
    panel.image = img1


def screenShot_cmd():
    newwind = Toplevel(window)
    newwind.title("ScreenShot")
    newwind.geometry("650x400")
    my_img = pyautogui.screenshot()
    my_img.save("image.png")

    screen_cap = Image.open("image.png")
    screen_cap = screen_cap.resize((450, 360), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(screen_cap)
    panel = Label(newwind, image = img)
    panel.place(relx = 0.05, rely = 0.04)

    btn_pic_scrst = Button(newwind, text = "Chụp", width = 10, height = 11, relief = GROOVE, bg = "bisque",
                        activebackground = "royalblue", activeforeground = "white")
    btn_pic_scrst.place(relx = 0.8, rely = 0.04)
    btn_pic_scrst['command'] = lambda:Change(newwind, panel)

    btn_pic_save = Button(newwind, text = "Lưu", width = 10, height = 5, relief = GROOVE, bg = "bisque",
                        activebackground = "royalblue", activeforeground = "white")
    btn_pic_save.place(relx = 0.8, rely = 0.67)

    newwind.mainloop()

#----------------------------------#
btn_scrst = Button(window, text = "Chụp\nmàn hình", width = 10, height = 5, relief = GROOVE,  bg = "deeppink",
                        activebackground = "royalblue", activeforeground = "white")
btn_scrst.place(relx = 0.43, rely = 0.43)
btn_scrst['command'] = screenShot_cmd



########################################
#--------- BUTTON APP RUNNING ---------#
def wind_app():
    procwind = Toplevel(window)
    procwind.title("Process")
    procwind.geometry("450x380")

    btn_proc_kill = Button(procwind, text = "Kill", width = 8, height = 3, relief = GROOVE, bg = "bisque", 
                        activebackground = "royalblue", activeforeground = "white")
    btn_proc_kill.place(relx = 0.03, rely = 0.06)

    btn_proc_view = Button(procwind, text = "Xem", width = 8, height = 3, relief = GROOVE, bg = "bisque", 
                        activebackground = "royalblue", activeforeground = "white")
    btn_proc_view.place(relx = 0.28, rely = 0.06)

    btn_proc_del = Button(procwind, text = "Xóa", width = 8, height = 3, relief = GROOVE, bg = "bisque", 
                        activebackground = "royalblue", activeforeground = "white")
    btn_proc_del.place(relx = 0.53, rely = 0.06)

    btn_proc_start = Button(procwind, text = "Start", width = 8, height = 3, relief = GROOVE, bg = "bisque", 
                        activebackground = "royalblue", activeforeground = "white")
    btn_proc_start.place(relx = 0.78, rely = 0.06)

    procwind.mainloop()

btn_app_rng = Button(window, text = "App Running", width = 18, height = 4, relief = GROOVE, bg = "bisque", 
                        activebackground = "royalblue", activeforeground = "white")
btn_app_rng.place(relx = 0.275, rely = 0.18)
btn_app_rng['command'] = wind_app


############################################
#--------- BUTTON PROCESS RUNNING ---------#
def wind_proc():
    procwind = Toplevel(window)
    procwind.title("Process")
    procwind.geometry("450x380")

    btn_proc_kill = Button(procwind, text = "Kill", width = 8, height = 3, relief = GROOVE, bg = "bisque", 
                        activebackground = "royalblue", activeforeground = "white")
    btn_proc_kill.place(relx = 0.03, rely = 0.06)

    btn_proc_view = Button(procwind, text = "Xem", width = 8, height = 3, relief = GROOVE, bg = "bisque", 
                        activebackground = "royalblue", activeforeground = "white")
    btn_proc_view.place(relx = 0.28, rely = 0.06)

    btn_proc_del = Button(procwind, text = "Xóa", width = 8, height = 3, relief = GROOVE, bg = "bisque", 
                        activebackground = "royalblue", activeforeground = "white")
    btn_proc_del.place(relx = 0.53, rely = 0.06)

    btn_proc_start = Button(procwind, text = "Start", width = 8, height = 3, relief = GROOVE, bg = "bisque", 
                        activebackground = "royalblue", activeforeground = "white")
    btn_proc_start.place(relx = 0.78, rely = 0.06)

    procwind.mainloop()


btn_prcs_rng = Button(window, text = "Process\nRunning", width = 11, height = 15, relief = GROOVE,  bg = "lightgreen",
                        activebackground = "royalblue", activeforeground = "white")
btn_prcs_rng.place(relx = 0.03, rely = 0.18)

btn_prcs_rng['command'] = wind_proc


########################################
#--------- BUTTON KEYSTROKE ---------#
def wind_keystrk():
    procwind = Toplevel(window)
    procwind.title("Keystroke")
    procwind.geometry("450x380")

    btn_proc_kill = Button(procwind, text = "Hook", width = 8, height = 3, relief = GROOVE, bg = "bisque", 
                        activebackground = "royalblue", activeforeground = "white")
    btn_proc_kill.place(relx = 0.03, rely = 0.06)

    btn_proc_view = Button(procwind, text = "Unhook", width = 8, height = 3, relief = GROOVE, bg = "bisque", 
                        activebackground = "royalblue", activeforeground = "white")
    btn_proc_view.place(relx = 0.28, rely = 0.06)

    btn_proc_del = Button(procwind, text = "In phím", width = 8, height = 3, relief = GROOVE, bg = "bisque", 
                        activebackground = "royalblue", activeforeground = "white")
    btn_proc_del.place(relx = 0.53, rely = 0.06)

    btn_proc_start = Button(procwind, text = "Xóa", width = 8, height = 3, relief = GROOVE, bg = "bisque", 
                        activebackground = "royalblue", activeforeground = "white")
    btn_proc_start.place(relx = 0.78, rely = 0.06)

    #listbox_proc = Listbox(procwind,width = 40, height = )
    procwind.mainloop()


btn_keystrk = Button(window, text = "Keystroke", width = 15, height = 10, relief = GROOVE,  bg = "lightblue",
                        activebackground = "royalblue", activeforeground = "white")
btn_keystrk.place(relx = 0.65, rely = 0.18)
btn_keystrk['command'] = wind_keystrk


#########################################
#--------- BUTTON SỬA REGISTRY ---------#
btn_rgt = Button(window, text = "Sửa registry", width = 25, height = 4, relief = GROOVE, bg = "darkviolet",
                        activebackground = "royalblue", activeforeground = "white")
btn_rgt.place(relx = 0.275, rely = 0.73)


window.mainloop()
