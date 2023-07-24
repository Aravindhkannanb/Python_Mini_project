to=input("Enter the email:")
content=input("Enter the content:")
def email(to,content):
    import smtplib
    smtp=smtplib.SMTP('smtp.gmail.com',587)
    smtp.ehlo()
    smtp.starttls()
    smtp.login("sender@gmail.com",'password')
    smtp.sendmail("sender@gmail.com",to,content)
    smtp.close()
email(to,content)