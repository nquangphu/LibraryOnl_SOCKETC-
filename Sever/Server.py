from tkinter import *
from tkinter import messagebox
from _thread import *
import socket
import threading

# thread function
def threaded(c):
    while True:
        # data received from client
        data = c.recv(1024)
        if not data:
            print('Bye')

            # lock released on exit
            lock.release()
            break
    c.close()

def server_listen(s):
    s.listen(5)
    print("socket is listening")
    while True:
        c, addr = s.accept()
        #lock.acquire()
        print('Connected to :', addr[0], ':', addr[1])
        data = c.recv(1024)
        if not data:
            print("Bye")
        
        str_data = data.decode("utf8")
        print(str_data)
        #start_new_thread(threaded, (c,))
    s.close()
    window.destroy()

def clickButton():
    btn['fg'] = "white"
    btn['bg'] = "royalblue"
    messagebox.showinfo("Thông báo", "Mở server thành công")
    btn['text'] = "Đang mở..."
    btn['underline'] = 6

    host = "10.126.5.172"
    port = 12345
    lock = threading.Lock()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    print("Socket binded to port ", port)

    server_listen(s)

window = Tk()
window.title("Server")
window.geometry("250x100")

btn = Button(window, text = "Mở Server", pady = 15, padx = 15, font = "Arial", bd = 3, bg = "firebrick")
btn['command'] = clickButton
btn['underline'] = 3
btn.place(relx = 0.5, rely = 0.5, anchor = CENTER)

window.mainloop()

