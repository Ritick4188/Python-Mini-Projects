import requests
import _json
from tkinter import *
from tkinter.messagebox import showinfo, showerror


def send_sms(number, message):
    url = 'https://www.fast2sms.com/dev/bulk'
    para = {
        'authorization': 'obfCrAtI5BdLp9VsKlYhTGE7MJ1vZa240mcUuxXjNHPkwRF6nOIpnTPMAVDEhdfrkJbG30goLuSvY8NU',
        'sender_id': 'FSTSMS',
        'message': message,
        'language': 'english',
        'route': 'p',
        'numbers': number,
    }

    response = requests.get(url, para)
    dic = response.json()
    print(dic)
    return dic.get('return')


def btn_click():
    num = text_number.get()
    msg = text_message.get('1.0',END)

    r = send_sms(num, msg)

    if r:
        showinfo('Send Successful','Successfully Send')
    else:
        showerror('Error','Something went wrong!')


# Creating GUI

root = Tk()
root.title('Message Sender ')
root.geometry('400x500')
font = ('Helvetica',22,'bold')

text_number = Entry(root,font=font)
text_number.pack(fill=X,pady=20)

text_message = Text(root)
text_message.pack(fill=X,pady=3)

send_btn = Button(root,text='SEND SMS',command=btn_click)
send_btn.pack()

root.mainloop()
