# -*- coding: utf-8 -*-
import unittest
from appium import webdriver
import time

class Apptest(unittest.TestCase):
	def setUp(self):
		desired_caps = {}
		desired_caps['platformName'] = 'Android'
		desired_caps['platformVersion'] = "6.0.1"
		desired_caps['deviceName'] = 'Nexus6'
		desired_caps['noSign'] = 'true'
		desired_caps['app'] = ('C:\Users\yxg\Desktop\\appTest\helloworld\\test.apk')
		desired_caps['fullReset'] = 'true'
		#desired_caps['unicodeKeyboard'] = 'true'
		#desired_caps['appPackage'] = 'cn.buding.martin'
		#desired_caps['appActivity'] = '.activity.SplashActivity'

		self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

	def tearDown(self):
		#self.driver.close_app()
		self.driver.remove_app('io.appium.unlock')
		self.driver.remove_app('io.appium.settings')
		self.driver.remove_app('io.appium.android.im')
		self.driver.quit()

	def test_1(self):
		print(self.driver.get_window_size())
		time.sleep(4)
		self.driver.swipe(start_x=1000, start_y=1200, end_x =500, end_y=1200, duration=500)
		time.sleep(1)
		self.driver.swipe(start_x=1000, start_y=1200, end_x =500, end_y=1200, duration=500)
		time.sleep(1)
		start = self.driver.find_element_by_id('cn.buding.martin:id/start')
		start.click()
		time.sleep(1)
		print self.driver.current_activity

def suite():
	suite = unittest.TestSuite()
	suite.addTest(Apptest("test_1"))
	return suite

if __name__== '__main__':
	unittest.main(defaultTest = 'suite')