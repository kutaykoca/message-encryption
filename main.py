from tkinter import *
import base64

root = Tk()
root.geometry('500x300')
root.resizable(0,0)
root.title("Mesaj Şifreleyici ve Çözücü - KT")
Label(root, text ='ENCODE DECODE', font = 'arial 20 bold').pack()
Label(root, text ='Made by KT', font = 'arial 20 bold').pack(side =BOTTOM)
Text = StringVar()
private_key = StringVar()
mode = StringVar()
Result = StringVar()

def Encode(key,message):
    enc=[]
    for i in range(len(message)):
        key_c = key[i % len(key)]
        enc.append(chr((ord(message[i]) + ord(key_c)) % 256))
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()


def Decode(key,message):
    dec=[]
    message = base64.urlsafe_b64decode(message).decode()
    for i in range(len(message)):
        key_c = key[i % len(key)]
        dec.append(chr((256 + ord(message[i])- ord(key_c)) % 256))
    return "".join(dec)


def Mode():
    if(mode.get() == 'e'):
        Result.set(Encode(private_key.get(), Text.get()))
    elif(mode.get() == 'd'):
        Result.set(Decode(private_key.get(), Text.get()))
    else:
        Result.set('"e" ya da "d" seçiniz')


def Exit():
    root.destroy()


def Reset():
    Text.set("")
    private_key.set("")
    mode.set("")
    Result.set("")


Label(root, font= 'arial 12 bold', text='MESAJ').place(x= 60,y=60)
Entry(root, font = 'arial 10', textvariable = Text, bg = 'ghost white').place(x=290, y = 60)
Label(root, font = 'arial 12 bold', text ='ŞİFRE').place(x=60, y = 90)
Entry(root, font = 'arial 10', textvariable = private_key , bg ='ghost white').place(x=290, y = 90)
Label(root, font = 'arial 12 bold', text ='MOD(e-encode, d-decode)').place(x=60, y = 120)
Entry(root, font = 'arial 10', textvariable = mode , bg= 'ghost white').place(x=290, y = 120)
Entry(root, font = 'arial 10 bold', textvariable = Result, bg ='ghost white').place(x=290, y = 150)
Button(root, font = 'arial 10 bold', text = 'SONUÇ'  ,padx =2,bg ='LightGray' ,command = Mode).place(x=60, y = 150)
Button(root, font = 'arial 10 bold' ,text ='SIFIRLA' ,width =6, command = Reset,bg = 'LimeGreen', padx=2).place(x=170, y = 200)
Button(root, font = 'arial 10 bold',text= 'ÇIKIŞ' , width = 6, command = Exit,bg = 'OrangeRed', padx=2, pady=2).place(x=270, y = 200)
root.mainloop()