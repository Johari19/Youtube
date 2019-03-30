from wsinstalls import *

installModule()

# Text
print("\nBasic Web Scraper (BWS) by Johari19\n")
print("\nYou need to have a basic understanding of html elements and classes to use this properly!\n")
print("Script made by: https://github.com/Johari19\n")
print("This script only uses elements and classes. Using ids and javascript will not work!\n")

# Variables
url = str(input("Enter url of the site you would like to scrape (USE: https://websitename.com): "))
element = str(input("\nEnter the element you would like to scrape: "))
raw_html = get_URL(url)
html = BeautifulSoup(raw_html, 'html.parser')
classes = str(input("Enter element's class: "))


# Script
print("I found:\n")
for element in html.find_all(element, classes):
    print (element.get_text())


os.system('pause')