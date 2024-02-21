from selenium import webdriver
from time import sleep

dr = webdriver.Chrome()
dr.get('file:///C:/Users/barab/Dropbox/Work/04%20Education/DevOps%20Experts/Meeting%20%235%20-%20Testing/tip_calc/index.html')

billAmount = dr.find_element(by="id", value="billamt")
peopleAmount = dr.find_element(by="id", value="peopleamt")

billAmount.send_keys("100")
peopleAmount.send_keys("5")

dr.find_element(by="xpath", value="//*[@id=\"serviceQual\"]/option[3]").click()
dr.find_element(by="xpath", value="//*[@id=\"musicQual\"]/option[2]").click()

dr.find_element(by="id", value="calculate").click()

actualTip = dr.find_element(by="id", value="tip").text
expectedTip = "9"

assert expectedTip == actualTip

# if expectedTip == actualTip:
#     print("Tip calculated correctly")
# else:
#     print("We have an issue")

sleep(100)
