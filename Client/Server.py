from tkinter import *
from tkinter import messagebox
from _thread import *
import socket
import threading
import os
import pyautogui


def takeScreenshot():
    
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save("screenshot.png")

def server_listen(server):
    server.listen(5)
    print("socket is listening")

    while True:
        c, addr = server.accept()
        print('Connected to :', addr[0], ':', addr[1])
        while True:
            data = c.recv(1024)
            if not data:
                print("not data")
                break
                
            str_data = data.decode("utf8")
            print(str_data)
            if str_data == "Shutdown":
                os.system('shutdown -s')
            else:
                if str_data == "Chup":
                    takeScreenshot()
                else:
                    if str_data == "Thoat":
                        break


    server.close()
    print("Thoat thanh cong")

def clickButton():
    btn['fg'] = "white"
    btn['bg'] = "royalblue"
    btn['text'] = "Đang mở..."
    btn['underline'] = 5
    messagebox.showinfo("Thông báo", "Mở server thành công")

    host = "192.168.1.21"
    port = 12345
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
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

