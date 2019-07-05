##AIzaSyB84uRYc9lZMl8uGRx2oeT11vkAEli7F80
##selenium 
from bs4 import BeautifulSoup
import requests
import time
from selenium import webdriver
query = input('What are you searching for?:   ')
url ='http://www.google.com/search?q='
page = requests.get(url + query + "download torrent")
soup = BeautifulSoup(page.text, "html.parser")
h3 = soup.find_all("a")
links_array =[]
for elem in h3:
    link=("https://www.google.com" + elem["href"])
    if "/url?q=https://" in link and "youtube" not in link :
        links_array.append(link)
time.sleep(5)

driver = webdriver.Firefox(executable_path=r'C:\Program Files\Mozilla Firefox\geckodriver.exe')
window_counter = 0
for link in links_array:
        # Open a new window
        # This does not change focus to the new window for the driver.
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[window_counter])# Switch to the new window
        driver.get(link)
        window_counter=window_counter + 1 
        if window_counter > 5:
            break
                   