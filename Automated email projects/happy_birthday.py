import datetime as dt
import pandas
import random
import smtplib


# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

def read_csv() -> pandas.DataFrame:
    df = pandas.read_csv("birthdays.csv", index_col=0)

    # convert the month and days series values into integers
    df["month"] = df["month"].astype(int)
    df["day"] = df["day"].astype(int)
    return df


def birthday_today() -> bool:
    """returns boolean indicating whether today is someone's birthday"""
    for (index, row) in data_df.iterrows():
        if row.month == now.month and row.day == now.day:
            return True
        else:
            return False


def get_name() -> str:
    """returns the name of the person whose birthday it is today"""
    for (index, row) in data_df.iterrows():
        if row.month == now.month and row.day == now.day:
            return row.name


def get_email() -> str:
    """returns the name of the person whose birthday it is today"""
    for (index, row) in data_df.iterrows():
        if row.month == now.month and row.day == now.day:
            return row.email


def write_letter(person: str) -> str:
    """returns a random stock birthday letter replacing [NAME] with the inputted argument: name

    Args: name - str argument, somebody's name"""
    num = random.randint(1, 3)
    with open(f"./letter_templates/letter_{num}.txt", "r") as letter:
        letter_contents = letter.read()
    email_contents = letter_contents.replace("[NAME]", person)
    return email_contents


def send_email(to_address: str, person:str) -> None:
    """Takes in email address as string and sends an email containing a randomly chosen quote to the adress, from
    testdodd4@gmail.com

    Args: to_address - string denoting an email address
          person - the name of the person email is sent to"""

    my_email = "testdodd4@gmail.com"
    password = "ejkfnemvhvomgnfc"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()  # secures connection to email server to prevent risk of email hacking. tls = Transport
        # Layer Security
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=to_address,
            msg=f"Subject: HAPPY BIRTHDAY {person.upper()}!, \n\n {write_letter(person)}"
        )


#=========== MAIN CODE ============

# create df
data_df = read_csv()

# get today's date
now = dt.datetime.now()

# get name and email if birthday today and send email to that person
if birthday_today():
    name = get_name()
    email = get_email()
    send_email(to_address=email, person=name)
