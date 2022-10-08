#!/usr/bin/python3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import time

options = FirefoxOptions()
options.add_argument("--headless")
driver = webdriver.Firefox(options=options)
driver.get("http://localhost:5000/login")

e_input = driver.find_element_by_name("email")
p_input = driver.find_element_by_name("password")

e_input.send_keys("admin@tes.tr")
p_input.send_keys("$$7e75r$$4dm1n$$2021")

p_input.send_keys(Keys.RETURN)

time.sleep(5)
driver.execute_script("""
var x = document.getElementsByTagName('tr');
for (i=0;i<x.length;i++) {
  var y = x[i].children[2].children;
  if (y.length>0) {
    window.open(y[0].href,'_blank');
  }
}
""")
time.sleep(10)
driver.close()
driver.quit()
