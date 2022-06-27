import smtplib, ssl
from email_scheduler_app.models import Email

smtp_server = "smtp.mail.yahoo.com"
port =465
sender_email = "lester_lecong@yahoo.com"
password = "vdsoztluoosgopql"

def send_email(email):
    subject = 'Subject:' + email.subject + '\n\n'
    content = ' ' + email.message

    context = ssl.create_default_context()

    try:
        server = smtplib.SMTP_SSL(smtp_server, port)
        server.ehlo()
        #server.starttls(context=context)
        server.login(sender_email, password)
        server.sendmail(sender_email, email.receiver, subject + content)
        server.quit()

        return 0
    except Exception as e:
        print(e)
        return -1
#finally:
    #server.quit()
