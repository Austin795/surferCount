from selenium import webdriver
import time
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
driver = webdriver.Chrome(options=options)

driver.get('https://www.surfline.com/surf-report/south-shore-ala-moana-park/5842041f4e65fad6a770889c?camId=583494d13421b20545c4b51e')
time.sleep(10)
#element = driver.find_element(By.NAME, "jw-icon jw-icon-display jw-button-color jw-reset")
element = driver.find_element(By.CSS_SELECTOR, "[aria-label=Play]")
#element = driver.find_elements_by_css_selector("[aria-label=Play]")
element.click()
time.sleep(30)
driver.save_screenshot("screenshot.png")

driver.close()


# driver.implicitly_wait(20) 
# driver.switch_to.frame(0) 
# element = driver.find_element_by_xpath("//button[@class='ytp-large-play-button ytp-button']")
# element.click()