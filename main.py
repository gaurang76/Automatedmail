##################### Hard Starting Project ######################
import pandas as pd
import datetime as dt
import smtplib
import random

# Reading CSV file
file = pd.read_csv('birthdays.csv')
birthday_dictionary = {(file_row['month'], file_row['day']): file_row for (index, file_row) in file.iterrows()}

# 2. Saving today's day and month in tuple
now = dt.datetime.now()
today = (now.month, now.day)
# Checking if today there is any birthday if yes then choosing random letter from template and emailing it

if today in birthday_dictionary:
    name = (birthday_dictionary[today]['name'])
    letters = ("letter_1", "letter_2", "letter_3")
    letter_chosen = random.choice(letters)

    file_path = f"letter_templates\{letter_chosen}.txt"

    with open(file_path, "r") as letter:
        letter_to_send = letter.read()

    correct_letter = letter_to_send.replace("[NAME]",name)

    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user="gaurangsharma79@gmail.com",password="ohyesabhi")
    connection.sendmail(
                    from_addr="gaurangsharma79@gmail.com",
                    to_addrs= birthday_dictionary[today]['email'],
                    msg = correct_letter

    )

    connection.close()