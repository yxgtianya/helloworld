import unittest
from appium import webdriver

class Apptest(unittest.TestCase):
	def setUp(self):
		desired_caps = {}
		desired_caps['platformName'] = 'Android'
		desired_caps['platformVersion'] = "6.0.1"
		desired_caps['deviceName'] = 'Nexus6'
		#desired_caps['app'] = PATH('')
		desired_caps['appPackage'] = 'cn.buding.martin'
		desired_caps['appActivity'] = '.activity.SplashActivity'

		self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

	def tearDown(self):
		self.driver.close_app()
		self.driver.remove_app('io.appium.unlock')
		self.driver.remove_app('io.appium.settings')
		self.driver.remove_app('io.appium.android.im')
		self.driver.quit()

	def test_1():
		driver.sleep(2000)
		driver.swipe(start_x=1300, start_y=1200, end_x =100, end_y=1200, duration=800)
		driver.swipe(start_x=1300, start_y=1200, end_x =100, end_y=1200, duration=800)

if __name__== '__main__':
	#suite = unittest.TestLoader().loadTestsFromTestCase(ContactsAndroidTests)
    unittest.main()