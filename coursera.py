# pip install webdriver_manager
# pip install selenium
username = "fikri.armiafahmi@student.upj.ac.id"
password = "Alkhamdulillah27@"

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options

Link = r"https://www.coursera.org/learn/dynamic-programming-greedy-algorithms/home/week/1"
profile_path = r"C:\Users\Fikri\AppData\Roaming\Mozilla\Firefox\Profiles\gonw4ida.default-release"

firefox_options = Options()
firefox_options.set_preference("profile", profile_path)
driver = webdriver.Firefox(options=firefox_options)
driver.get(Link)

# Tunggu elemen input username hingga terlihat
WebDriverWait(driver, 100).until(EC.visibility_of_element_located((By.ID, "cds-react-aria-1")))
driver.find_element(By.ID, "cds-react-aria-1").send_keys(username)

# Tunggu elemen input password hingga terlihat
WebDriverWait(driver, 100).until(EC.visibility_of_element_located((By.ID, "cds-react-aria-2")))
driver.find_element(By.ID, "cds-react-aria-2").send_keys(password)

# Tunggu tombol submit hingga terlihat dan klik
WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".css-j6v0dd")))
driver.find_element(By.CSS_SELECTOR, ".css-j6v0dd").click()

WebDriverWait(driver, 100).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".css-ra3hwj")))
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, ".css-ra3hwj").click()

WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".css-1s4ge7s")))
#--------------------------
while True:
    try:
        video = driver.find_element(By.TAG_NAME, 'video')
        if video:
            duration = driver.execute_script("return arguments[0].duration;", video)
            driver.execute_script(f"arguments[0].currentTime = {duration};", video)

        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR, ".css-1s4ge7s").click()
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR, ".css-1s4ge7s").click()
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
