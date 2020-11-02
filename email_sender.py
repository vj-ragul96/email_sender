import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Your_name'
email['to'] = 'receiver_email_id'
email['subject'] = 'Helloooo!!!!'

email.set_content(html.substitute({'name': 'receiver_name'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port='587') as smtp:
    smtp.ehlo()
    smtp.starttls()
# lines 14 to 16 are generic lines and are common for all... 14 to contact our email's server,
    # 15  to establish a connection  and 16 for sending the email securely...

    smtp.login('your_email', 'your_password')
    smtp.send_message(email)
    print('all done!!')




