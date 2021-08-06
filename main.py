import requests
from bs4 import BeautifulSoup
import smtplib


my_email = "your_gmail"  #or another mail
password = "your_password"

BUY_PRICE = 999 # the price that you wanna buy maximum

#### insert url below of any product in Amazon ####
URL = "https://www.amazon.com/LG-Gram-Laptop-Touchscreen-Thunderbolt/dp/B082XRQFZ7/ref=sr_1_5?dchild=1&keywords=lg+gram&qid=1628244664&sr=8-5"
URL_aspire5 = "https://www.amazon.com/Acer-A515-55-56VK-i5-1035G1-Fingerprint-Keyboard/dp/B08HN1WDWZ/ref=sr_1_2?dchild=1&keywords=acer%2Baspire%2B5&qid=1628248471&sr=8-2&th=1"
header = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
    "Accept-Language": "en-GB,en;q=0.9,ru-RU;q=0.8,ru;q=0.7,en-US;q=0.6,uz;q=0.5"
}

response = requests.get(URL, headers=header)
amzn_site = response.text
# print(amzn_site)
soup = BeautifulSoup(amzn_site, "html.parser")
laptop_price = soup.find_all(name="span", class_="priceBlockBuyingPriceString")[0].getText()
print(laptop_price)

price = laptop_price.split("$")[1]
if len(price) > 7:                     # if price >= $1000
    price = price.split(",")
    current_price = float(price[0]+price[1])
    print(current_price)
else:                                 # if price < $1000
    current_price = float(price)
    print(current_price)

if current_price <= BUY_PRICE:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="to any other of your address",
            msg=f"Subject:Big Sale!\n\nPrice of LG gram Laptop has been cut down to ${current_price} in Amazon. Do not let this chance a go!\n\n\nSpecifications: \n15.6Inch IPS Touchscreen, Intel 10th Gen Core i71065G7 CPU, 8GB RAM, 256GB M.2 NVMe SSD, 17 Hours Battery."
        )
