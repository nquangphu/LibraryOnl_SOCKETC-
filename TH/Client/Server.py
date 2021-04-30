from tkinter import *
from tkinter import Tk
from tkinter import messagebox
import pyautogui
import socket
import threading
from _thread import *
from PIL import Image,ImageTk
from tkinter.ttk import Frame, Style
sc = "Success"
er = "Error"

def create_list_book():
    mylist = list()
    with open('Database\list_book.txt') as file:
        for line in file:
            data = line.rstrip('\n')
            tup = (data)
            mylist.append(tup)

    return mylist

def create_list_search(index):
    mylist = list()
    for i in list_book:
        data = (ID, name, author, pbsh, Type) = i.split(',')
        info = list(data)
        check = info[index] in mylist
        if check == False:
            mylist.append(info[index])
        info.clear()

    return mylist

list_book = create_list_book()

list_author = create_list_search(2)
list_type = create_list_search(4)

def open_server():
    host = socket.gethostname()
    local_ip = socket.gethostbyname(host)
    print("IP address: ", local_ip)
    port = 80
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((local_ip, port))
    print("Socket binded to port ", port)
    return s

def check_account_signin(username, password):
    check = False
    with open('list_account.txt') as file:
        for line in file:
            (user, pw) = line.split()
            if username == user and password == pw:
                check = True
                break
    return check

def check_account_signup(username):
    check = True
    with open('list_account.txt') as file:
        for line in file:
            (user, pw) = line.split()
            if username == user:
                check = False
                break
    return check

def search_book(conn, data_str):
    (ID, name, author, pbsh, Type) = data_str.split('+')
    filename = "Database\Book\B" + ID + ".txt"
    f = open(filename, 'r')
    data = f.read()
    conn.send(data.encode())

def handle_client(conn, addr):
    print("[NEW CONNECTION] {addr} connected.")

    while True:
        data = conn.recv(1024)
        if not data:
            print("[EXIT] Not data!")
            break
        str_data = data.decode('utf-8')
        print(str_data)
        (method, username, password) = str_data.split('+')
        if method == "Signin":
            if check_account_signin(username, password) == True:
                print("Sign in thanh cong")
                print(username, password)
                conn.sendall(sc.encode())
                data_sch = conn.recv(1024).decode('utf-8')
                search_book(conn, data_sch)
            else:
                
                print("Sign in that bai")
                print(username, password)
                conn.sendall(er.encode())
        else:
            if check_account_signup(username) == True:
                print("Sign up thanh cong")
                print(username, password)

                conn.send(sc.encode())
            else:
                print("Sign up that bai")
                print(username, password)
                conn.send(er.encode())
    
    conn.close()


def start(s):
    s.listen(5)
  
    while True:
        conn, addr = s.accept()
        print('Connected to :', addr[0], ':', addr[1])
        thread = threading.Thread(target = handle_client, args = (conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}") 

    return s

def click_btn_open():
    s = open_server()
    btn_open['fg'] = "white"
    btn_open['bg'] = "royalblue"
    btn_open['text'] = "Tắt Server"
    messagebox.showinfo("Thông báo", "Mở server thành công")
    
    s = start(s)
    s.close()

window = Tk()
window.title("Server")
window.geometry("600x400")
window.configure(bg = 'blue')

img_tmp = Image.open("image.jpg")
img_tmp = img_tmp.resize((500, 135), Image.ANTIALIAS)
img = ImageTk.PhotoImage(img_tmp)
panel = Label(window, image = img)
panel.pack(ipady = 10)

btn_open = Button(window, text = "Mở Server", pady = 15, padx = 15, font = "Arial",
                    bd = 3, bg = "firebrick")
btn_open['command'] = click_btn_open
btn_open.place(relx = 0.5, rely = 0.5, anchor = CENTER)

window.mainloop()
