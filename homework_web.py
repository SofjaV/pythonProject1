import time
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.maximize_window()
url = 'https://www.saucedemo.com/'
driver.get(url)

#login
username = driver.find_element('id', 'user-name')
# name_accepted = driver.find_element('full xpath', '/html/body/div/div/div[2]/div[2]/div/div[1]/text()[1]')
username.send_keys('standard_user')

password = driver.find_element('id', 'password')
# password_for_all = driver.find_element('full xpath', '/html/body/div/div/div[2]/div[2]/div/div[2]/text()')
password.send_keys('secret_sauce')
time.sleep(3)

login_btn = driver.find_element('xpath', '//*[@id="login-button"]')
login_btn.click()

#items
time.sleep(3)
item1 = driver.find_element('xpath', '//*[@id="add-to-cart-sauce-labs-backpack"]')
item1.click()

item2 = driver.find_element('xpath', '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')
item2.click()
time.sleep(3)

#basket
basket_btn = driver.find_element('xpath', '//*[@id="shopping_cart_container"]/a')
basket_btn.click()
time.sleep(3)
# saucedemo = driver.current_window_handle

#screenshoots
# driver.switch_to.new_window('tab')
# driver.get('https://www.saucedemo.com/inventory-item.html?id=4')
div = driver.find_element('xpath', '//*[@id="cart_contents_container"]/div/div[1]/div[3]/div[2]')
div.screenshot('screenshot1.png')

# driver.switch_to.new_window('tab')
# driver.get('https://www.saucedemo.com/inventory-item.html?id=1')
div = driver.find_element('xpath', '//*[@id="cart_contents_container"]/div/div[1]/div[4]')
div.screenshot('screenshot2.png')
time.sleep(3)

# driver.switch_to.window(saucedemo)
check_out = driver.find_element('xpath','//*[@id="checkout"]')
check_out.click()
time.sleep(5)

first_name = driver.find_element('id', 'first-name')
first_name.send_keys('John')

last_name = driver.find_element('id', 'last-name')
last_name.send_keys('Smith')

postal_code = driver.find_element('id', 'postal-code')
postal_code.send_keys('11111')
time.sleep(5)

continue_btn = driver.find_element('xpath', '//*[@id="continue"]')
continue_btn.click()
time.sleep(5)

finish_btn = driver.find_element('xpath', '//*[@id="finish"]')
finish_btn.click()
time.sleep(5)

back_home = driver.find_element('xpath', '//*[@id="back-to-products"]')
back_home.click()
time.sleep(5)

home = driver.find_element('xpath','//*[@id="react-burger-menu-btn"]')
home.click()
time.sleep(5)


logout = driver.find_element('id','logout_sidebar_link')
logout.click()
time.sleep(5)
driver.quit()









