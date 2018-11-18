import smtplib

user="pythonbootcamp"
password = "123!@qweQWE"

sent_from = "pythonbootcamp@wp.pl"
to = ["rkorzen@gmail.com"]
subject = "test"
body="to jest tresc"

email_text = f"""
From:{sent_from}
To: {",".join(to)}
Subject: {subject}

{body}
"""

try:
    server = smtplib.SMP_SSL("smtp.wp.pl",465)
    server.ehlo()
    server.login(user,password)
    server.sendmail(sent_from,to,email_text)

except Exception as e:
    print(e)
    print("Coś poszło źle")