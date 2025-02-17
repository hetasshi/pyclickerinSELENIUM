from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


def clickname(item):
    cart = driver.find_element(By.NAME, item)
    cart.click()
    time.sleep(1)

def clickid(item):
    cart = driver.find_element(By.ID, item)
    cart.click()
    time.sleep(1)

driver = webdriver.Chrome()

  
google_url = "https://www.saucedemo.com/"

driver.get(google_url)

search_query1 = "standard_user"
search_query2 = "secret_sauce"

box1 = driver.find_element(By.ID, "user-name")
box1.send_keys(search_query1)

box2 = driver.find_element(By.ID, "password")
box2.send_keys(search_query2)
time.sleep(1)
box3 = driver.find_element(By.ID, "login-button")
box3.click()
time.sleep(2)

clickname("add-to-cart-sauce-labs-backpack")
clickname("add-to-cart-sauce-labs-bike-light")
clickname("add-to-cart-sauce-labs-bolt-t-shirt")
clickid("shopping_cart_container")
clickid("checkout")

time.sleep(60)

driver.quit()
