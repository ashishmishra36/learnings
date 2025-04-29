import smtplib
import getpass
import imaplib

# gmail app password: bthf rfoo efqn fgyr
# this file has set up to send an email from gmail account, for best results this file needs to be run from terminal

# first, create smtp object

smtp_object =  smtplib.SMTP('smtp.gmail.com',587)
# try to echo the server , to make sure connection is made before sending any email
smtp_object.ehlo()

# we need to start TLS to make sure encryption is enabled
smtp_object.starttls()

# take the email and password as input

email = getpass.getpass('Emails is :')
print(f"email captured successfully! {email}")

password = getpass.getpass('Password Please: ')
print(f"Password captured successfully! {password}")

# now login
smtp_object.login(email,password)

# add subject and to address and mail content and send an email

msg = 'subject: ' + 'python_test' + '\n' + 'hello world'

smtp_object.sendmail(email,email,msg)

# quit the object and close the connection
smtp_object.quit()

m = imaplib.IMAP4_SSL('imap.gmail.com')
m.login(email,password)
print(m.list())
