# selenium is a web framwork that allows us to execute cross-browser tests.
from selenium import webdriver 
  
  
driver = webdriver.Firefox() 
driver.get("https://google.co.in") 