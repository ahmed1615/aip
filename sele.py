from selenium import webdriver
driver=webdriver.Chrome()
driver.get('https://www.thetestingworld.com/index.php?option=com_users&view=registration&Itemid=588')
driver.maximize_window()
driver.find_element_by_name("jform[name]").send_keys("hello worled")
driver.find_element_by_xpath("//input[@name='jform[username]']").send_keys("ahmed")
driver.find_element_by_name("jform[password1]").send_keys("hamoza2010")
driver.find_element_by_name("jform[password2]").send_keys("hamoza2010")
driver.find_element_by_xpath("//input[@name='jform[email1]']").send_keys("hamoza2010@yahoo.com")
driver.find_element_by_name("jform[name]").clear()
driver.find_element_by_name("jform[name]").send_keys("abc123")
driver.find_element_by_xpath("//input[@name='jform[email2]']").send_keys("hamoza2010@yahoo.com")
#driver.find_element_by_class_name("validate").click()
driver.find_element_by_link_text("Cancel").click()
#driver.close()
driver.get("https://www.booking.com/cars/index.en-gb.html?label=gen173nr-1DCAEoggI46AdIM1gEaAyIAQGYAQm4ARfIAQzYAQPoAQGIAgGoAgO4AsK_z_gFwAIB0gIkNDA3ZDU1OWUtZmI3OS00NTllLWE0ZmYtOTlmZDAzNGRjY2M02AIE4AIB")
driver.find_element_by_id("return-location-different").click()
#driver.quit()