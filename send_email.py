import smtplib, ssl
from private import PASSWORD, USERNAME

def send_email(user_email, message):
    host = "smtp.gmail.com"
    port = 465

    username = USERNAME
    password = PASSWORD

    receiver = "bart.bel8@gmail.com"
    my_context = ssl.create_default_context()

    # message = message + '\n' + user_email
    message = """\
Subject: New email from {0}

From: {0}
{1}
""".format(user_email, message)

    with smtplib.SMTP_SSL(host, port, context=my_context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)

if __name__ == "__main__":
    message = """\
Subject: Hi!
How are you? This is a test email.
"""
    email = "bart.bel8@gmail.com"
    send_email(email, message)

