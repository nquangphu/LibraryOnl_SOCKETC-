from tkinter import *
from tkinter import messagebox
import socket
import threading
import os
import pyautogui
import datetime
import time
from PIL import Image

def takeScreenshot():
    
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save("screenshot.png")
    txt = "screenshot.png"
    return txt
def runFunc(data):
    print(data, ":: Successfully!!!")

def server_listen(server):
    server.listen(5)
    print("Socket is listening...")

    while True:
        c, addr = server.accept()
        print('Connected to :', addr[0], ':', addr[1])
        while True:
            data = c.recv(1024)
            if not data:
                print("not data")
                break
                
            str_data = data.decode("utf8")

            #----------------- Shutdown -----------------
            if str_data == "Shutdown":
                os.system('shutdown -s')

            #----------------- Screenshot -----------------
            else:
                if str_data == "Chup":
                    while True:
                        data1 = c.recv(1024)
                        if not data1:
                            break
                        else: 
                            str_data1 = data1.decode("utf8")
                            if str_data1 == "Chup":
                                name_img = takeScreenshot()
                                f = open(name_img, 'rb')
                                l = f.read(1024)
                                c.send(l)
                                print("Image successfully sent to client")
                
                #----------------- Thoat -----------------
                else:
                    if str_data == "Thoat":
                        break

                    #----------------- App running -----------------
                    else:
                        if str_data == "App":
                            runFunc(str_data)

                        #----------------- Process running -----------------
                        else:
                            if str_data == "Process":
                                runFunc(str_data)

                            #----------------- Keystroke -----------------
                            else:
                                if str_data == "Keystroke":
                                    runFunc(str_data)

                                #----------------- Sua Registry -----------------
                                else:
                                    if str_data == "Registry":
                                        runFunc(str_data)
                            


    server.close()
    print("Thoat thanh cong")

def clickButton():
    btn['fg'] = "white"
    btn['bg'] = "royalblue"
    btn['text'] = "Đang mở..."
    btn['underline'] = 5
    messagebox.showinfo("Thông báo", "Mở server thành công")

    host = socket.gethostname()
    local_ip = socket.gethostbyname(host)
    print("IP address: ", local_ip)
    port = 80
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((local_ip, port))
    print("Socket binded to port ", port)

    server_listen(s)

window = Tk()
window.title("Server")
window.geometry("250x100")

btn = Button(window, text = "Mở Server", pady = 15, padx = 15, font = "Arial", bd = 3, bg = "firebrick")
btn['underline'] = 3
btn['command'] = clickButton
btn.place(relx = 0.5, rely = 0.5, anchor = CENTER)

window.mainloop()
