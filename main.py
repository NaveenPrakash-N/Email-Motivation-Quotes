import smtplib
import datetime as dt
from random import randint 


today = dt.datetime.now()

with open('quotes.txt', 'r') as file:
    file_list = file.readlines()


random_index = randint(0, len(file_list) - 1)
random_quote = file_list[random_index]


email = input("Enter your email address: ")
password = input("Enter your app password: ")
recipient_email = input("Enter the recipient's email address: ")

with smtplib.SMTP('smtp.gmail.com', 587) as connection:
    connection.starttls()
    connection.login(user=email, password=password)
    connection.sendmail(
        from_addr=email,
        to_addrs=recipient_email,
        msg=f"Subject:Motivational Quote\n\n{random_quote}"
    )
print("Email sent successfully!")
