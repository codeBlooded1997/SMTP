# import the SMTP library. SMTP = simple main transfer protocol. its a protocol we must follow to send emails
import smtplib

# Which email is this being send from
sender_email = 'ariannumber1@gmail.com'

# Password so we can log in to the senders account
password = 'hooman12'

# Who is this email going to ve sent to
recipient_email = 'arianaghnaei@gmail.com'


email_text = '''
    Dummy text. Yo whats's up.
'''

# Email sending function
def send_email():
    # Setup the email server. Gmail host, and use a common port (I googled these things)
    # Common smtp ports: 25 or 2525 or 587
    server = smtplib.SMTP('smtp.gmail.com', 587)  # hotmail: smtp.live.com   # aol: smtp.aol.com  #yahoo: smtp.mail.yahoo.com

    # I asicly allow us encript what we are sending to server from this point on
    # Turn on Transport layer security. All commands after this will be encrypted.
    server.starttls()

    # Login to the senders email
    server.login(sender_email, password)

    # Send the email
    server.sendmail(sender_email, recipient_email, email_text)

    # Cleanup
    server.quit()

    
# Calling the function to send emails
send_email()
