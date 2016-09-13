#coding:utf-8
from element import BasePageElement
from locators import BeginPageLocators

class BasePage(object):
	def __init__(self, driver):
		self.driver = driver
#引导页
class LinkPage(BasePage):
	def swipertl(self):
		self.driver.swipe(start_x=1000, start_y=1200, end_x =500, end_y=1200, duration=500)

#开始页		
class BeginPage(BasePage):
	def click_begin_button(self):
		element = self.driver.find_element(*BeginPageLocators.BEGIN_BUTTON)
		element.click()
		
