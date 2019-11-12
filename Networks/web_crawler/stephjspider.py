#!/usr/bin/python3
# Stephen Jones
# ohlittlebrain@gmail.com

# Simple Web Scraper, gets all links and images from a single webpage.

import requests
from parsel import Selector
import os
import time
start = time.time()


ScanDir = '/tmp/Web_Crawler'
# Check for directory and create one for output of scan
if not os.path.exists(ScanDir):
    os.mkdir(ScanDir)
    print("Directory" , ScanDir , " created.")
else:
    print("Directory" , ScanDir, " already exists!")

# Get input for website we would like to crawl

website = input("What site are we crawling? ")
# GET request to the site
response = requests.get(website)

## Setup for scraping tool

# "response.txt" contain all web page content
selector = Selector(response.text)

# Extracting href attribute from anchor tag <a href="*">
href_links = selector.xpath('//a/@href').getall()


#Extracting img src attribute from img tag <img src="*">
image_links = selector.xpath('//img/@src').getall()

# Print out the web page links in order, separated by line

print('***************************** Web Page Links ************************************')
print(*href_links, sep = "\n")
print(*href_links, file=open('/tmp/Web_Crawler/Web_links.txt', 'w'))
print('*****************************************************************')

# Print image links from website, separated by line

print('***************************** Image Links ************************************')
print(*image_links, sep = "\n")
print(*image_links, file=open('/tmp/Web_Crawler/Image_links.txt', 'w'))
print('*****************************************************************')


# Amount of time the spider took to crawl the site. 
end = time.time()
print("Time taken in seconds : ", (end-start))