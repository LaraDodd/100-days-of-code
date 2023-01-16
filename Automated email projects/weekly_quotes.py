"""this program sends a motivational quote if it is a Monday"""

import smtplib
import datetime as dt
import random


def get_quote() -> str:
    """opens quotes text file and randomly chooses a quote, returns this quote"""
    with open("quotes.txt", "r") as quotes_file:
        data = quotes_file.readlines()
    rand_quote = random.choice(data)
    return (rand_quote)


def send_email(to_address) -> None:
    """Takes in email address as string and sends an email containing a randomly chosen quote to the adress, from
    testdodd4@gmail.com

    Args: to_address - string denoting an email address """

    my_email = "testdodd4@gmail.com"
    password = "ejkfnemvhvomgnfc"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()  # secures connection to email server to prevent risk of email hacking. tls = Transport
        # Layer Security
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=to_address,
            msg=f"Subject: HAPPY MONDAY!, \n\n {get_quote()}"
        )


def is_monday() -> bool:
    """returns true if it is monday"""

    now = dt.datetime.now()  # create now object from date_time

    if now.weekday() == 0:
        return True
    else:
        return False


email_list = ["laradodd97@gmail.com", "richardjdodd@gmail.com", "isaacrayment123@gmail.com", "laratest246@yahoo.com", "dmeryldodd@gmail.com"]

# if it is monday, email everyone in email list
if is_monday():
    for email in email_list:
        send_email(email)
