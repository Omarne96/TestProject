from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Firefox()
driver.get("https://visa.vfsglobal.com/dza/fr/fra/interim-page")

try:
	donwto = WebDriverWait(driver,100).until(
		EC.presence_of_element_located((By.XPATH,'//*[@id="__layout"]/div[1]/main[1]/div[1]/div[1]/div[2]/div[3]/div[2]')) 
		)
	donwto.click()

	fitstbtn = WebDriverWait(driver,100).until(
		EC.presence_of_element_located((By.XPATH,'//*[@id="colap1"]/div[1]/p[6]/a[1]')) 
		)
	fitstbtn.click()	
finally:
	pass
"""
#donwto = driver.find_element(By.XPATH,'//*[@id="__layout"]/div[1]/main[1]/div[1]/div[1]/div[2]/div[3]/div[2]')
#donwto.click()
time.sleep(1)
fitstbtn = driver.find_element(By.XPATH,'//*[@id="colap1"]/div[1]/p[6]/a[1]')
fitstbtn.click()
"""
try:
	enteremail = WebDriverWait(driver,100).until(
		EC.presence_of_element_located((By.ID,'EmailId')) 
		)

	pswd = WebDriverWait(driver,100).until(
		EC.presence_of_element_located((By.ID,'Password')) 
		)

	entaccbtn = WebDriverWait(driver,100).until(
	EC.presence_of_element_located((By.CSS_SELECTOR,'form#ApplicantListForm > div:nth-of-type(4) > input')) 
	)

except:
	print("erorrrrrrrrrrrrrrrrrrrrrrrrrrr")
	print("erorrrrrrrrrrrrrrrrrrrrrrrrrrr")
	print("erorrrrrrrrrrrrrrrrrrrrrrrrrrr")
	print("erorrrrrrrrrrrrrrrrrrrrrrrrrrr")


#enteremail = find_element(By.ID,'EmailId')
#pswd = find_element(By.ID,'Password')
#entaccbtn = find_element(By.XPATH,'//*[@id="Accordion1"]/div[1]/div[2]/div[1]/ul[1]/li[1]/a[1]')

email = "sidhoumali70@gmail.com"
password = 'Medea26000@'


enteremail.send_keys(email)
pswd.send_keys(password)
time.sleep(25)
entaccbtn.click()


time.sleep(20)
driver.quit()
