import smtplib
from email.message import EmailMessage

msg = EmailMessage()
msg.set_content(input(str('Enter your message: ')))

sender = input(str('Enter the sender email: '))
password = input (str('Enter the your password: '))

msg['Subject'] = input(str('Enter the subject of the mail: '))
msg['From'] = sender
msg['To'] = input (str('Enter the receiver email: '))


# Send the message via our own SMTP server.
try: 
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(msg['From'], password)
    server.send_message(msg)
    server.quit()

    print ('Message has been sent to ', msg['To'])
except:
    print ("Incorrect Email or password")




