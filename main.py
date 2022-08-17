##################### Extra Hard Starting Project ######################
import pandas
import datetime as dt
import random
import smtplib

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
# Get today's month and day
now = dt.datetime.now()
now_month = now.month
now_day = now.day

# Read CSV file and get the birthday
birthday = pandas.read_csv("birthdays.csv")
birthday_dic = birthday.to_dict(orient="records")
# print(birthday_dic)
for birthday_one in birthday_dic:
    if birthday_one["month"] == now_month and birthday_one["day"] == now_day:
        birthday_name = birthday_one["name"]
        birthday_email = birthday_one["email"]
        # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
        letter_name = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
        letter_pick = random.choice(letter_name)
        with open(f"letter_templates\{letter_pick}") as letter:
            content = letter.read()
            new_letter = content.replace("[NAME]", birthday_name)
            new_letter = new_letter.replace("Angela", "Shuang")

    # 4. Send the letter generated in step 3 to that person's email address.
        my_email = "sophiameng88@gmail.com"
        password = "lfovowyqdgmguiqh"
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=f"{birthday_email}",
                msg=f"subject: Happy Birthday! \n\n{new_letter}"
            )
