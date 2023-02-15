import smtplib

from_email = "graemeapitesting@gmail.com"
to_email = "graeme.m.balint@gmail.com"
password = "zruohqzwigpdgpeo"

connection = smtplib.SMTP("smtp.gmail.com",port=587)
connection.starttls()
connection.login(user=from_email, password=password)
connection.sendmail(from_addr=from_email, to_addrs=to_email, msg="Subject:This is a test\n\nDid you get it?!")
connection.close()