from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time
import pandas as pd

# define the website to scrape and path where the chromediver is located
website = 'https://collegedunia.com/btech-colleges'
# define 'driver' variable
driver = webdriver.Chrome()
# open Google Chrome with chromedriver
driver.get(website)

# locate and click on a butto

# select dropdown and select element inside by visible text
# select elements in the table
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(3)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(3)

clg_name = driver.find_elements(By.XPATH,"//h3[@class='jsx-3175684501 font-weight-medium text-lg mb-0']")
fees = driver.find_elements(By.XPATH,'//span[@class="jsx-3175684501 text-lg text-green d-block font-weight-bold mb-1"]')
rating = driver.find_elements(By.XPATH,'//span[@class="jsx-3175684501 lr-key text-lg text-primary d-block font-weight-medium mb-1"]')
avg_pkg = driver.find_elements(By.XPATH,"//span[@class='jsx-914129990 text-green d-block font-weight-bold mb-1']")


# storage data in lists
cl_nm = []
fs = []
rt =[]
avg_pk = []
for i in clg_name:
    cl_nm.append(i.text)
for i in fees:
    fs.append(i.text)
for i in rating:
    rt.append(i.text)
for i in avg_pkg:
    avg_pk.append(i.text)

# looping through the matches list

df = pd.DataFrame(list(zip(cl_nm,fs,avg_pk,rt)),columns=['clg_name','fees','avg_pkg','rating'])
df.to_csv('/Users/Shriram/Desktop/Website/new.csv')