import smtplib


my_email = "testdodd4@gmail.com"
password = "ejkfnemvhvomgnfc"


with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()  # secures connection to email server to prevent risk of email hacking. tls = Transport
                           # Layer Security
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="laratest246@yahoo.com",
        msg="Subject: Hello, \n\n This is the body of my email"
    )

import datetime as dt
now = dt.datetime.now()
print(now.year)

month = now.month
print(month)

day_of_week = now.weekday()
print(day_of_week)

dob = dt.datetime(year=1997, month=7, day=22)
print(dob)