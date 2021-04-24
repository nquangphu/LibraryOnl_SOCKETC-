import tkinter
import socket


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)



def Connect(Ipaddress):
    try: s.connect((Ipaddress.get() , 12345))
    except: print("Can't connect to server") 

def Send(typereq):
    try: 
        s.send(typereq.encode())
        return s.recv(10485760)
    except: print("Can't connect to server")


def Receive():
    return s.recv(1024)


#msg = s.recv(1024)
#print(msg.decode("utf-8"))