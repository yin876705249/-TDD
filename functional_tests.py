from selenium import webdriver
import unittest

class NewVistorTest(unittest.TestCase): #(1)

	def setUp(self): #(3)
		self.browser = webdriver.Firefox()
		
	def tearDown(self): #(3)
		self.browser.quit()
			
	def test_can_start_a_list_and_retrieve_it_later(self): #(2)
		# Edith has heard about a cool new online to-do app. She goes
		# to check out its homepage
		browser.get('http://localhost:8000')
		
		# she notices the page title and header mention to-do lists
		self.assertIn('To-Do',self.browser.title) #(4)
		self.fail('Finish the test!') #(5)
		browser = webdriver.Firefox()


if __name__=='__main__': #(6)
	unittest.main(warnings='ignore') #(7)





# She is invited to enter a to-do item straight away

# She types "Buy peacock feathers" into a text box(Edith's hobby
# is tying fly-fishing lures)

# when she hits enter, the page updates, and now the page lists
# "1: Buy peacock feathers" as an item in a to-do list

# There is still a text box inviting her to add another item. She
# enters "User peacock feathers to make a fly" (Edith is very methodical)

# The page updates again, and now shows both items on her list

# Edith wonders whether the site will remember her list. Then she sees
# that the site has generated a unique URL for her -- there is some
# explanatory text to that effect.

# She visits that URL - her to-do list is still there.

# Satisfied, she goes back to sleep


