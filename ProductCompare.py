#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 29 11:09:30 2025

@author: ashcash

webscraping cost comparison between 
two types of beats
"""
import requests
from bs4 import BeautifulSoup

def product_compare(url1,url2):
    r1 = requests.get(url1)
    r2 = requests.get(url2)
    
    if r1.status_code != 200:
        print("Error with the first URL")
    elif r2.status_code !=200:
        print("Error with the second URL")
    
    else:
        html_content1 = r1.text
        html_content2 = r2.text
        soup1 = BeautifulSoup(html_content1, "html.parser")
        soup2 =  BeautifulSoup(html_content2, "html.parser")
        data1 = {"Name": soup1.find(id="title").text.strip(),
            "Price": soup1.find(class_="a-offscreen").text.strip()}
        data2 = {"Name": soup2.find(id="title").text.strip(),
            "Price": soup2.find(class_="a-offscreen").text.strip()}
    x = data1["Price"]
    y = data2["Price"]
    x1 = data1["Name"]
    y1 = data2["Name"]
    
    price1=float(x[1:])
    price2 = float(y[1:])
    
    if price1 > price2:
        print(x1[0:13],"costs more than ",y1[0:16])
    else:
        print(y1[0:16],"costs more than ",x1[0:13])

product_compare("https://www.amazon.com/Beats-Solo-Wireless-Headphones-Matte/dp/B0CZPLV566/ref=sr_1_1?crid=353TJGY4NBPVX&dib=eyJ2IjoiMSJ9.e2UYILmhBcsYdakOQeB0qE3umsRqKFp9WsonNClY9I7LEdeisvVGXBikD3DQ4P6XPS7qshsnXE6NKrFbyTqDRACQLLsxWbQ1VzERuNMrDmbz7RZPCAqUWLCHs79p0GEfQCBYCsgfxKePBTnpHXy8sGpxr2Cw0klaJ6pKr-acwFX8itt035gD4gwg9nhkIVl-Ik86AG9fwR3nlkAvKDmt4-TPBWWaBbwgjsLQMqhQLbU.zmonbK5CGgeTyHxpJVYsno0fAZWvh9dM3HRkZ2m6LPw&dib_tag=se&keywords=beats%2Bheadphones&qid=1743272752&sprefix=beats%2Caps%2C188&sr=8-1&th=1", 
                "https://www.amazon.com/Beats-Studio-Pro-Personalized-Compatibility/dp/B0C8PSMPTH/ref=sr_1_2_sspa?crid=3NYMYVJ1EXHC0&dib=eyJ2IjoiMSJ9.e2UYILmhBcsYdakOQeB0qPknM0izKlX5BACc6bdluRRp9N9gW2yRwkQDTAaxKKtY8v8_kD9FKGE-JEVzyND8Lq0gaZYly6g6h1E97-jMSgkMwad-w6V2HlKbhN3hNer1wNCeQGB5pK7vw7KLGeUZ-hn9HGUHWoKC1FaqIGByv_-Ol_aBeLyId5QiD-u5R8MyyKv4OkGVTGKWbSPfUwq8rkrhUnbOyDnwEO3T5YnopYI.3f7P2DePeNfbwkjtNvKu5XtDP8KcMN0QwNLnJnLIG7A&dib_tag=se&keywords=beats&qid=1743288147&sprefix=beats%2Caps%2C325&sr=8-2-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1")
##float(string[1:])