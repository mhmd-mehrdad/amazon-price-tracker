from bs4 import BeautifulSoup
import requests
import smtplib
from email.message import EmailMessage
import os
from dotenv import load_dotenv

load_dotenv()

MY_EMAIL = os.getenv("MY_EMAIL")
PASSWORD = os.getenv("PASSWORD")

# print(MY_EMAIL)
# print(PASSWORD is None)

email = EmailMessage()

email["From"] = MY_EMAIL
email["To"] = MY_EMAIL
email["Subject"] = "Amazon Price Alert!"

URL = os.getenv("URL")

response = requests.get(URL)

website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

price = float(f"{soup.find(name="span", class_="a-price-whole").get_text()}{soup.find(name="span", class_="a-price-fraction").get_text()}")


print(price)
print(type(price))

preset_price = 100.00
print(type(preset_price))

product = soup.find(name="span", class_="a-size-large product-title-word-break").get_text()
product = " ".join(product.split())
print(product)

if price < preset_price:

    email.set_content(f"{product} is now {price}")

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, PASSWORD)

        connection.send_message(email)

    print("Email sent successfully!")










