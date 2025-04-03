
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup

# Replace these with your Instagram login credentials
USERNAME = ""
PASSWORD = ""

# Initialize WebDriver (use Chrome or Firefox)
driver = webdriver.Chrome()  # Use webdriver.Firefox() if using Firefox

# Open Instagram
driver.get("https://www.instagram.com/accounts/login/")
time.sleep(5)  # Wait for page to load

# Find username and password fields and enter credentials
username_field = driver.find_element(By.NAME, "username")
password_field = driver.find_element(By.NAME, "password")

username_field.send_keys(USERNAME)
password_field.send_keys(PASSWORD)
password_field.send_keys(Keys.RETURN)  # Press Enter to login
time.sleep(5) 
driver.get("https://www.instagram.com/tags/mahendra/")
time.sleep(10) 
last_height = driver.execute_script("return document.body.scrollHeight")
count=0
usernames_list = []
while True:
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        links = [a["href"] for a in soup.find_all("a", class_="x1i10hfl xjbqb8w x1ejq31n xd10rxx x1sy0etr x17r0tee x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz x4gyw5p _a6hd") if "href" in a.attrs]
        
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        for link in links:
            print(link)
            count+=1
            usernames_list.append(link)
            
        # Wait to load page
        time.sleep(5)
        if count>40:
            break
        
        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
        
for link in usernames_list:
        print(link)
        driver.get("https://www.instagram.com/"+link)
        time.sleep(5)
        soup = BeautifulSoup(driver.page_source, "html.parser")
        t=soup.find('span',{'class':'_ap3a _aaco _aacw _aacx _aad7 _aade'})
        print("username : ",t.text)
        count+=1
        if(count==40):
                break     


 # Wait for login to complete

# Optional: Close browser after login
# driver.quit()

