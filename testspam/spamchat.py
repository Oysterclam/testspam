from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import tkinter


chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.implicitly_wait(20)
driver.get('https://www.messenger.com/')
email="ay20019@pausd.us"
password="iamveryfat"
driver.find_element_by_xpath("//*[@id='email']").send_keys(email)
driver.find_element_by_xpath("//*[@id='pass']").send_keys(password)
driver.find_element_by_xpath("//*[@id='loginbutton']").click()

def createChat(times):
	for a in range(times):
		driver.find_element_by_xpath('//*[@id="u_0_0"]/div/div/div[1]/div[1]/a').click()
		driver.find_elements_by_class_name('_58al')[1].send_keys('Andy J Yang')
		time.sleep(0.75)
		driver.find_elements_by_class_name('_58al')[1].send_keys(Keys.RETURN)
		driver.find_elements_by_class_name('_58al')[1].send_keys('Oscar Chou')
		time.sleep(0.75)
		driver.find_elements_by_class_name('_58al')[1].send_keys(Keys.RETURN)
		driver.find_element_by_class_name('notranslate').send_keys('create_chat')
		driver.find_element_by_class_name('notranslate').send_keys(Keys.RETURN)
		time.sleep(1)
		driver.find_element_by_class_name('_2jnv').click()
		time.sleep(0.25)
		driver.find_elements_by_class_name('notranslate')[0].send_keys('000'+str(a))
		driver.find_elements_by_class_name('notranslate')[0].send_keys(Keys.RETURN)
		time.sleep(2)

	# driver.find_elements_by_class_name('')
createChat(5)
print('succeed')
