from selenium import webdriver
import time
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
driver = webdriver.Chrome(options=options)

# Load surf spot web cam, eg. Honolulu, HI
driver.get('https://www.surfline.com/surf-report/south-shore-ala-moana-park/5842041f4e65fad6a770889c?camId=583494d13421b20545c4b51e')

# Give time to insure page load
time.sleep(10)

# Locate play button within page
element = driver.find_element(By.CSS_SELECTOR, "[aria-label=Play]")
element.click()

# Give time to watch surfline AD 😉 (usually 15s)
time.sleep(30)
driver.save_screenshot("screenshot_surf_spot.png")
driver.close()