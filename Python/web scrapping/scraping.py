from email import message
from itertools import count
import requests
from bs4 import BeautifulSoup
import smtplib
import time


price_list = []

def check_price():
    url = "https://www.flipkart.com/samsung-galaxy-s22-ultra-5g-phantom-black-512-gb/p/itm03548d2bd4686?pid=MOBGGG2YMRSPFFSP&lid=LSTMOBGGG2YMRSPFFSPXOPRW4&marketplace=FLIPKART&q=samsung+s22&store=tyy%2F4io&srno=s_1_15&otracker=search&otracker1=search&fm=Search&iid=9edd063b-f541-4bce-b5d0-813b288fcb1a.MOBGGG2YMRSPFFSP.SEARCH&ppt=sp&ppn=sp&ssid=bm0cngp60g0000001666862295466&qH=c342c4d902c5d044"
    r = requests.get(url)

    soup = BeautifulSoup(r.content, 'html5lib')
    price = soup.find_all('div',attrs={'class':'_30jeq3 _16Jk6d'})
    for i in price:
        x=(i.text)
        x = float(x.replace("₹","").replace(",",""))
        price_list.append(x)
    return x    

def send_mail(message):
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login("checkemail299@gmail.com","poiglwjeoangqzxe")
    server.sendmail("checkemail299@gmail.com" , "tusharjain9929@gmail.com" , message )
    print("msg send sucessfully")
    server.quit()

def price_decrease_check():
    if price_list[-1]-price_list[-2]:
        return True
    else:
        return False

count = 1
while True:
    current_price = check_price()
    if count > 1:
        flag = price_decrease_check(price_list)
        if flag:
            dec = price_list[-1]-price_list[-2]
            message = f"Price is decreased please check it and price is decrease by {dec} amount!"
            send_mail(message)
    time.sleep(2500)
    count += 1
