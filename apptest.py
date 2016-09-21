# -*- coding: utf-8 -*-
import unittest
from appium import webdriver
import page
from time import sleep
import HTMLTestRunner
import send_email 

class Apptest(unittest.TestCase):
	desired_caps = {}
	desired_caps['platformName'] = 'Android'
	desired_caps['platformVersion'] = "6.0.1"
	desired_caps['deviceName'] = 'Nexus6'
	#不重新签名
	desired_caps['noSign'] = 'true'
	desired_caps['app'] = 'C:\Users\yxg\Desktop\\appTest\helloworld\\test.apk'
	desired_caps['newCommandTimeout'] = '30'
	desired_caps['noReset'] = 'true'
	#测试结束卸载app
	#desired_caps['fullReset'] = 'true'
	#desired_caps['unicodeKeyboard'] = 'true'
	desired_caps['appPackage'] = 'cn.buding.martin'
	desired_caps['appActivity'] = '.activity.SplashActivity'

	driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
		

	def setUp(self):
		print 'setup'
		
	def tearDown(self):
		print 'tearDown'

	def test_1(self):
		print(self.driver.get_window_size())
		sleep(6)
		link_page = page.LinkPage(self.driver)
		link_page.swipertl()
		sleep(1)
		link_page.swipertl()
		sleep(1)
		
	def test_2(self):
		begin_page = page.BeginPage(self.driver)
		begin_page.click_begin_button()
		sleep(1)
		print self.driver.current_activity
		
	def test_3(self):
	    #卸载安装的app
		self.driver.remove_app('io.appium.unlock')
		self.driver.remove_app('io.appium.settings')
		self.driver.remove_app('io.appium.android.im')
		self.driver.remove_app('cn.buding.martin')
		
	
		
if __name__== '__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase(Apptest)
	#unittest.TextTestRunner(verbosity=2).run(suite)
	filename = 'd:\\result.html'
	fp = file(filename, 'wb')
	runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Test result of cn.buding.martin', 
	description='Test_Report')
	#unittest.main(defaultTest = 'suite')]
	runner.run(suite)
	Apptest.driver.quit()
	send_email.send_report()