import socket


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)



def Connect(IP_address):
    try: s.connect((IP_address.get() , 11111))
    except: print("Cannot access to server") 

def Send(typereq):
    try: 
        s.send(typereq.encode())
        return s.recv(20971520)
    except: print("Cannot access to server")


def Receive():
    return s.recv(1024)


