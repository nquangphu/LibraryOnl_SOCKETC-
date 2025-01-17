from tkinter import *
from tkinter import Tk
from tkinter import messagebox
import socket
import threading
from _thread import *
from PIL import Image,ImageTk
sc = "Success"
er = "Error"
nf = "Not found"

###############################################################
#---------------------- CREATE DATABASE ----------------------#
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

def check_ID(ID, _ID):
    if len(ID) == 0:
        return True
    else:
        if ID == _ID:
            return True
        else:
            return False

def check_Name(name, _name):
    if len(name) == 0:
        return True
    else:
        if name == _name:
            return True
        else:
            return False

def check_Author(author, _author):
    if len(author) == 0:
        return True
    else:
        if author == _author:
            return True
        else:
            return False

def check_Type(Type, _Type):
    if len(Type) == 0:
        return True
    else:
        if Type == _Type:
            return True
        else:
            return False

def search_book(conn, data_str):
    info = (ID, name, author, pbsh, Type) = data_str.split('+')

    if len(author) == 0 and len(Type) == 0 and len(ID) == 0 and len(name) == 0:
        conn.send(nf.encode())

    else:
        if len(ID) != 0 or len(name) != 0:
            check = False
            for x in list_book:
                (_ID, _name, _author, _pbsh, _Type) = x.split(',')
                if check_ID(ID, _ID) == True and check_Name(name, _name) == True and check_Author(author, _author) == True and check_Type(Type, _Type):
                    filename = "Database\Book\B" + _ID + ".txt"
                    f = open(filename, 'r')
                    data = f.read()
                    conn.send((_ID + '+' + _name + "||\n" + data).encode())
                    check = True
                    f.close()
                    break
            if check == False:
                conn.send(nf.encode())

        else:
            check = False
            filename = "Database\list_search.txt"
            fo = open(filename, 'w')
            fo.write("*list\n")
            for x in list_book:
                (_ID, _name, _author, _pbsh, _Type) = x.split(',')
                if check_Author(author, _author) == True and check_Type(Type, _Type) == True:     
                    fo.write(str(x) + '\n')
                    check = True
            fo.close()
            if check == False:
                conn.send(nf.encode())
            else:
                fi = open(filename, 'r')
                data = fi.read()
                conn.send(data.encode())
                fi.close()


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
    with open('Database\list_account.txt') as file:
        for line in file:
            (user, pw) = line.split()
            if username == user and password == pw:
                check = True
                break
    return check

def check_account_signup(username):
    check = True
    with open('Database\list_account.txt') as file:
        for line in file:
            (user, pw) = line.split()
            if username == user:
                check = False
                break
    return check

def update_account_file(username, password):
    f = open("Database\list_account.txt", 'a')
    data = '\n' + username + ' ' + password
    f.write(data)

    f.close()

def handle_client(conn, addr):
    print("[NEW CONNECTION] {addr} connected.")
    
    cl_sch = False
    while True:
        if cl_sch == False:
            data = conn.recv(1024000)
        cl_sch = False
        if not data:
            print("[EXIT] Not data!")
            break
        str_data = data.decode('utf-8')
        check = True
        
        (method, username, password) = str_data.split('+')

        #---------------------- SIGN IN ----------------------#
        if method == "Signin":
            if check_account_signin(username, password) == True:
                print("Sign in thanh cong")
                conn.sendall(sc.encode())

            else:
                print("Sign in that bai")
                conn.sendall(er.encode())
                check = False

        #---------------------- SIGN UP ----------------------#
        else:
            if check_account_signup(username) == True:
                print("Sign up thanh cong")
                update_account_file(username, password)
                conn.send(sc.encode())

            else:
                print("Sign up that bai")
                conn.send(er.encode())
                check = False

        while check == True:
            data = conn.recv(1024000)
            if not data:
                break
            in4 = data.decode('utf-8')
            c = in4.count('+')
            if c == 2:
                cl_sch = True
                break
            search_book(conn, in4)
 
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
window.configure(bg = 'pink')

img_tmp = Image.open("Image\image.jpg")
img_tmp = img_tmp.resize((500, 135), Image.ANTIALIAS)
img = ImageTk.PhotoImage(img_tmp)
panel = Label(window, image = img)
panel.pack(pady = 10)

btn_open = Button(window, text = "Mở Server", pady = 15, padx = 15, font = "Arial",
                    bd = 3, bg = "red")
btn_open['command'] = click_btn_open
btn_open.place(relx = 0.5, rely = 0.6, anchor = CENTER)

window.mainloop()
