import socket
  
  
def Main():
    # local host IP '127.0.0.1'
    host = '192.168.1.92'
  
    # Define the port on which you want to connect
    port = 80
  
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
  
    # connect to server on local computer
    s.connect((host,port))
  
    # message you send to server
    while True:
        strig = input("Client: ")
        s.send(strig.encode('ascii'))
        data = s.recv(1024)
        print(str(data.decode('ascii')))
  
    s.close()
  
if __name__ == '__main__':
    Main()