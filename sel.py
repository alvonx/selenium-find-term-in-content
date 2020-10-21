import csv
import time
import random
from selenium import webdriver 

# open csv to load content  
with open('selenium.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    list_reader = list(reader)

total_rows = len(list_reader)

# randomly select any row from csv
random_row = random.randint(0,total_rows-1)
# extract the search term
search_term = list_reader[random_row]['searchterm']

# extract the search content
search_content = list_reader[random_row]['searchcontent']

# create webdriver object 
driver = webdriver.Chrome('D:/Tools/Software/chromedriver_win32/chromedriver_win32/chromedriver.exe')
driver.maximize_window()
driver.get("C:/Users/Deepak/Desktop/qa imapct/selenium/findtext.html") 
time.sleep(3)

search_term_element = driver.find_element_by_id("searchterm") 
search_term_element.send_keys(search_term)
time.sleep(3)

search_content_element = driver.find_element_by_id("searchcontent") 
search_content_element.send_keys(search_content)
time.sleep(3)

find_btn_element = driver.find_element_by_id("find") 
find_btn_element.click()
time.sleep(3)
driver.quit()
