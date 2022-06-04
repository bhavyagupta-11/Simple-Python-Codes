from email import message
from http import server
from bs4 import BeautifulSoup
import requests
import html5lib
import smtplib
import time

def userInput():
    global flipkartProductURL
    global amazonProductURL
    flipkartProductURL =input('Enter the flipkart product url: ')
    amazonProductURL=input('Enter the amazon product URL: ')

def trackPrices():
    flipkartProductURL =input('Enter the flipkart product url: ')
    amazonProductURL=input('Enter the amazon product URL: ')
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36'}

    if flipkartProductURL and amazonProductURL:
        flipkartResponse =requests.get(flipkartProductURL,headers=headers)
        amazonResponse =requests.get(amazonProductURL,headers=headers)
        flipkartSoup =BeautifulSoup(flipkartResponse.content,'html5lib')
        amazonSoup=BeautifulSoup(amazonResponse.content,'html5lib')
        flipkartProductPrice =float(flipkartSoup.find('div',attrs='_30jeq3 _16Jk6d').text.replace(',','')[1:])
        amazonProductPrice=float(amazonSoup.find('span',attrs='priceBlockDealPriceString').text.replace(',','')[1:])

        print('Flipkart product price is ',str(flipkartProductPrice))
        print('Amazon Product price is ',str(amazonProductPrice))

        if flipkartProductPrice and amazonProductPrice:
            sendEmail(amazonProductPrice,flipkartProductPrice)

def sendEmail(amazonPrice,flipkartPrice):
    message=''
    if amazonPrice and flipkartPrice and (amazonPrice>flipkartPrice):
        message='Flipkart price is lower. It is Rs. '+ str(flipkartPrice)
    elif flipkartPrice>amazonPrice:
         message='Amazon price is lower. It is Rs. '+ str(amazonPrice)
    fromEmail='bhavyagupta740@gmail.com'
    toEmail=input('to email:')
    password=input('enter password')
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(fromEmail,password)
    server.sendmail(fromEmail,toEmail,message)
    print('Mail sent')
    server.quit()

userInput()
while True:
    trackPrices()
    time.sleep(5)