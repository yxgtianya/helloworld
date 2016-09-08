from selenium.webdriver.support.ui import WebDriverWait

class BasePageElement(object):
	def __set__(self, obj, value):
		driver = obj.driver
		WebDriverWait(driver, 500, 0.5).until(lambda driver£ºdriver.find_element_by_id(self.locator))
		driver.find_element_by_id(self.locator).send_keys(value)
	
	def __get__(self, obj, owner):
		driver = obj.driver
		WebDriverWait(driver, 500, 0.5).until(lambda driver: driver.find_element_by_id(self.locator))
		return driver.find_element_by_id(self.locator).get_attribute("value")