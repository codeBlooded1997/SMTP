# import the SMTP library. SMTP = simple main transfer protocol. its a protocol we must follow to send emails
import smtplib

# Import MIME test format library. MIME = Multipurpose Internet Mail Extrnsions. Its an internet standard we gollow to encode email contents, like attachements, pictures, links, text, etc...
from email.mime.text import  MIMEText

# Import pythons email utility package. using this library we can pass in the recipients name and email together
import email.utils

# Which email is this being send from
sender_email = 'ariannumber1@gmail.com'
sender_name = 'Arian A.'

# Password so we can log in to the senders account
password = 'hooman12'

# Who is this email going to ve sent to
recipient_email = 'arianaghnaei@gmail.com'
recipient_name = 'John Doe'


email_text = """
             Dummy text. Yo whats's up.
             """

# Email sending function
def send_email():
    print('\nSending email...\n')

    # Get message ready in email format
    message = MIMEText(email_text)

    #print(message)

    #
    message['To'] = email.utils.formataddr((recipient_name, recipient_email))
    message['From'] =
    message['Subject'] =


    # Setup the email server. Gmail host, and use a common port (I googled these things)
    # Common smtp ports: 25 or 2525 or 587
    server = smtplib.SMTP('smtp.gmail.com', 587)  # hotmail: smtp.live.com   # aol: smtp.aol.com  #yahoo: smtp.mail.yahoo.com

    # I asicly allow us encript what we are sending to server from this point on
    # Turn on Transport layer security. All commands after this will be encrypted.
    server.starttls()

    # Login to the senders email
    server.login(sender_email, password)

    # Send the email
    #server.sendmail(sender_email, recipient_email, email_text)

    # Cleanup
    server.quit()

    print('\nEmail sent.\n')

# Calling the function to send emails
send_email()
