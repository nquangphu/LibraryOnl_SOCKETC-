from tkinter import *
from tkinter import Tk
from tkinter import messagebox
import pyautogui
import socket
import threading
from _thread import *

def open_server():
    host = socket.gethostname()
    local_ip = socket.gethostbyname(host)
    print("IP address: ", local_ip)
    port = 80
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((local_ip, port))
    print("Socket binded to port ", port)
    return s

def threaded(c):
    while True:
        data = c.recv(1024)
        if not data:
            print('Not data')
            print_lock.release()
            break
        str_data = data.decode('ascii')
        print(str_data)
        if str_data == "Thoat":
            print_lock.release()
            break
        strig = input("Server: ")
        c.send(strig.encode('ascii'))

    c.close()

def server_listen(s):
    s.listen(5)
    print("socket is listening...")
  
    while True:
        c, addr = s.accept()
        print('Connected to :', addr[0], ':', addr[1])
  
        start_new_thread(threaded, (c,))
    s.close()    

    return s

def click_btn_open():
    s = open_server()
    btn_open['fg'] = "white"
    btn_open['bg'] = "royalblue"
    btn_open['text'] = "Tắt Server"
    messagebox.showinfo("Thông báo", "Mở server thành công")
    
    s = server_listen(s)


window = Tk()
window.title("Server")
window.geometry("200x200")
print_lock=threading.Lock()

btn_open = Button(window, text = "Mở Server", pady = 15, padx = 15, font = "Arial",
                    bd = 3, bg = "firebrick", command = click_btn_open)
btn_open.place(relx = 0.5, rely = 0.5, anchor = CENTER)

window.mainloop()