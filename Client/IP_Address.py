from tkinter import *
import Connection


table=Tk()
table.title("Client")
##
enter_IP=StringVar(table)
IP_address=Entry(table,textvariable=enter_IP,width=20)
IP_address.grid(row=0,column=0)
def connect_click():
    Connection.Connect(IP_address)

connect_button= Button(table,text="Kết nối",width=10)
connect_button.grid(row=0,column=1,pady=2)
##
app_running_button=Button(table,text="App Running",width=10,height=2)
app_running_button.grid(row=1,column=0,pady=2)
##
process_running_button=Button(table,text="Process Running",width=12,height=2)
process_running_button.grid(row=1,column=1,pady=2)
##

shut_down_button=Button(table,text="Tắt máy",width=10,height=2)
shut_down_button.grid(row=2,column=0,pady=2)
##

screen_shot_button=Button(table,text="Chụp màn hình",width=15,height=2)
screen_shot_button.grid(row=2,column=1,pady=2)
##
keystroke_button=Button(table,text="Keystroke",width=10,height=2)
keystroke_button.grid(row=1,column=2,pady=2)
##
registry_button=Button(table,text="Sửa registry",width=12,height=2)
registry_button.grid(row=2,column=2,pady=2)
##
def shutWind():
    Connection.Send("Shutdown")
exit_button=Button(table,text="Thoát",command=shutWind,width=10,height=2)
exit_button.grid(row=3,column=2,pady=2)
table.mainloop()