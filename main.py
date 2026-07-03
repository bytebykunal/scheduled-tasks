##################### Extra Hard Starting Project ######################
import smtplib
import pandas
import datetime as dt
import random

now = dt.datetime.now()
today = (now.month,now.day)

my_email = "kunal.ds.dev@gmail.com"
password = "ycjm hfeq kzxz lbzu"
# 1. Update the birthdays.csv

data = pandas.read_csv("birthdays.csv")


with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
# 2. Check if today matches a birthday in the birthdays.csv
    for index, row in data.iterrows():
        if today == (row['month'], row['day']):
    # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
            with open(f"letter_templates/letter_{random.randint(1, 3)}.txt") as file:
                message = file.read()
                birthday_wish = message.replace("[NAME]", row['name'])
    # 4. Send the letter generated in step 3 to that person's email address.
                connection.sendmail(
                    from_addr=my_email,
                    to_addrs= row['email'],
                    msg= f"Subject: Birthday Wish\n\n{birthday_wish}"
                )



