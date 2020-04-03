# import the SMTP library. SMTP = simple main transfer protocol. its a protocol we must follow to send emails
import smtplib

# Which email is this being send from
sender_email = 'AaronSMTPsender@gmail.com'

# Password so we can log in to the senders account
password = 'senderpassword'

# Who is this email going to ve sent to
recipient_email = 'JohnSMTPreceiver1@gmail.com'

#
email_text = '''
    Dummy text. Yo whats's up.
'''

# Email sending function
def send_email():
    # Setup the email server. Gmail host, and use a common port (I googled these things)
    # Common smtp ports: 25 or 2525 or 587
    server = smtplib.SMTP('smtp.gmail.com', 587)  # hotmail: smtp.live.com   # aol: smtp.aol.com  #yahoo: smtp.mail.yahoo.com

    # Login to the senders email
    server.login(sender_email, password)
    pass


# Calling the function to send emails
send_email()
