from tkinter import *
import smtplib
from email.message import EmailMessage

def send_message():
    email = EmailMessage()
    email['from'] = 'VijayRagul'
    email['to'] = address.get()
    email['subject'] = subject_box.get()
    email.set_content(message_box_entry.get("1.0",END))

    with smtplib.SMTP(host='smtp.gmail.com', port='587') as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login('vijrag96@gmail.com', 'vijay1996')
        smtp.send_message(email)

        print('message sent..')

    email_entry.delete(0, END)
    subject_box_entry.delete(0, END)
    message_box_entry.delete('1.0', END)

app = Tk()
app.geometry("750x500")
app.title('Email Sender')

heading = Label(text='Python Mail Sender', bg='pink', fg='black', font='10', width="500", height='3')
heading.pack()

address_field = Label(text='Recepient Email Address:')
subject_field = Label(text='Subject:')
message_field = Label(text='Message:')

address_field.place(x=15, y=80)
subject_field.place(x=15, y=140)
message_field.place(x=15, y=210)

address = StringVar()
subject_box = StringVar()
message_box = Text()

email_entry = Entry(textvariable=address, width="30")
subject_box_entry = Entry(textvariable=subject_box, width="30")
message_box_entry = Text(app, width='30', height='5')

email_entry.place(x=15, y=100)
subject_box_entry.place(x=15, y=160)
message_box_entry.place(x=15, y=230)

send_button = Button(app, text="Send Message", command = send_message, width="15", height='2', bg='blue')
send_button.place(x=15, y=350)

mainloop()