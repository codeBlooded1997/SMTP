# import the SMTP library. SMTP = simple main transfer protocol. its a protocol we must follow to send emails
import smtplib

# Import MIME test format library. MIME = Multipurpose Internet Mail Extrnsions. Its an internet standard we gollow to encode email contents, like attachements, pictures, links, text, etc...
from email.mime.text import  MIMEText

# Import pythons email utility package. using this library we can pass in the recipients name and email together
import email.utils

# For reading csv files
import pandas as pd

# Which email is this being send from
sender_email = 'arthurSMPT372@gmail.com'
sender_name = 'Arthur'

# Password so we can log in to the senders account
password = 'test01SMTP'

# Read csv using pandas
column_names = ['name', 'email']
data = pd.read_csv('source/Email_List.csv', names=column_names)

# Who is this email going to ve sent to
recipient_emails = data.email.tolist()[1:]
recipient_names = data.name.tolist()[1:]

# Read in html file
html_file = open("source/Email_Contents.html","r")

# Message body
email_html = html_file.read()

# Email sending function
def broadcast_email():
    print('\nBroadcasting email...\n')

    # Loop through entire emails list
    # zip() takes 2 lists and comines them (takes first elements of each list and put together in a tuple.)
    for recipient_name, recipient_email in zip(recipient_names, recipient_emails):

        # Get message ready in email format. Give us html functionality
        message = MIMEText(email_html, 'html')
        message.add_header('Content-Type', 'text/html')

        # Populate the message object with data. Good pracyice. Follow protocol and industry standard please.
        message['To'] = email.utils.formataddr((recipient_name, recipient_email))
        message['From'] = email.utils.formataddr((sender_name, sender_email))
        message['Subject'] = "Sent using an email automation software."

        # Setup the email server. Gmail host, and use a common port (I googled these things)
        # Common smtp ports: 25 or 2525 or 587
        server = smtplib.SMTP('smtp.gmail.com', 587)  # hotmail: smtp.live.com   # aol: smtp.aol.com  #yahoo: smtp.mail.yahoo.com

        # I asicly allow us encript what we are sending to server from this point on
        # Turn on Transport layer security. All commands after this will be encrypted.
        server.starttls()

        # Login to the senders email
        server.login(sender_email, password)

        # Send the email
        server.sendmail(sender_email, recipient_email, message.as_string())

        # Cleanup
        server.quit()

        # Confirm it was sent to client
        print('Sent to {} at {}.'.format(recipient_name, recipient_email))

    print('\nEmails Broadcasted.\n')


# Calling the function to send emails
broadcast_email()
