print("[Loading Library and Environment...]")
import env
import time, os
import pickle
import pyautogui
import keyboard
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options

email = env.EMAIL
password = env.PASSWORD
if email == "" and password == "":
    print("[ File .env is Empty ]")
    exit()
print(f"[ Email: {email} | Password: {password} ]")

LinkLogin = (
    "https://www.coursera.org/login"
)

def stop_execution():
    print("\nKombinasi tombol terdeteksi. Menghentikan loop...")
    global stop_loop
    stop_loop = True

first = True
while True:
    inputLink = input("Input link course (Banyak link, pisahkan dengan spasi): ")
    Link = inputLink.split()
    print(f"\nJumlah Course yng di Input: {len(Link)}")

    def login():
        print("[Memuat login...]")
        profile_path = r"C:\Users\runneradmin\AppData\Roaming\Mozilla\Firefox\Profiles\406qyncq.default-release"

        firefox_options = Options()
        firefox_options.set_preference("profile", profile_path)
        driver = webdriver.Firefox(options=firefox_options)
        driver.get(LinkLogin)

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "cds-react-aria-2")))
        driver.find_element(By.ID, "cds-react-aria-2").send_keys(email)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "cds-react-aria-3")))
        driver.find_element(By.ID, "cds-react-aria-3").send_keys(password)
        WebDriverWait(driver, 1000).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-e2e='page-nav-link-my_learning']")))
        indikasi = driver.find_element(By.CSS_SELECTOR, "[data-e2e='page-nav-link-my_learning']")
        if indikasi:
            print("[Menyimpan Cookie Chaptcha...]")
            pickle.dump(driver.get_cookies(), open("cookies.pkl", "wb"))
            time.sleep(2)
            print("[Refresh Webdriver...]")
            driver.quit()

    if first:
        login()
        first = False
        
    print("[Memuat ulang webdriver...]")
    for index, course in enumerate(Link):
        driver = webdriver.Firefox()
        driver.get(course)
        cookies = pickle.load(open("cookies.pkl", "rb"))
        for cookie in cookies:
            driver.add_cookie(cookie)
        driver.refresh()
        stop_loop = False
        try:
            while not stop_loop:
                try:
                    WebDriverWait(driver, 5).until(
                        EC.visibility_of_element_located((By.CLASS_NAME, "css-y3t86r"))
                    )
                    ul_element = driver.find_element(By.CLASS_NAME, "css-y3t86r")
                    if ul_element:
                        list_items = ul_element.find_elements(By.TAG_NAME, "li")
                        print(f"Jumlah Module di Course {index+1}: {len(list_items)}")
                        break
                except:
                    print("Tidak Menemukan Elemen Ul")
                    break
            
            print(f"Eksekusi Course [{course}]")
            while not stop_loop:
                time.sleep(3)
                try:
                    WebDriverWait(driver, 10).until(
                        EC.visibility_of_element_located((By.CSS_SELECTOR, ".css-ra3hwj"))
                    )
                    driver.find_element(By.CSS_SELECTOR, ".css-ra3hwj").click()
                except:
                    pyautogui.click(500, 500)
                time.sleep(3)
                # --------------------------
                while True:
                    try:
                        popupAwal = driver.find_element(By.CSS_SELECTOR, ".c-modal-x-out")
                        if popupAwal:
                            popupAwal.click()
                    except:
                        pass

                    try:
                        WebDriverWait(driver, 3).until(
                            EC.visibility_of_element_located((By.TAG_NAME, "video"))
                        )
                        video = driver.find_element(By.TAG_NAME, "video")
                        if video:
                            time.sleep(2)
                            pyautogui.click(1291, 590)
                            time.sleep(1)
                            pyautogui.click(1291, 590)
                            time.sleep(1.5)
                            pyautogui.click(1000, 550)
                            time.sleep(1.5)
                            print("Video Mark as Done")
                    except Exception as e:
                        pass
                    try:
                        WebDriverWait(driver, 2).until(
                            EC.visibility_of_element_located(
                                (
                                    By.XPATH,
                                    "//span[@class='cds-button-label' and text()='Mark as completed']",
                                )
                            )
                        )
                        mark = driver.find_element(
                            By.XPATH,
                            "//span[@class='cds-button-label' and text()='Mark as completed']",
                        )
                        if mark:
                            mark.click()
                            print("Reading Mark as Done")
                    except Exception as e:
                        pass

                    try:
                        WebDriverWait(driver, 3).until(
                            EC.visibility_of_element_located(
                                (By.XPATH, "//button[@aria-label='Next Item']")
                            )
                        )
                        driver.find_element(
                            By.XPATH, "//button[@aria-label='Next Item']"
                        ).click()
                        print("[Next]")
                    except Exception as e:
                        try:
                            popupAwal = driver.find_element(
                                By.CSS_SELECTOR, ".c-modal-x-out"
                            )
                            if popupAwal:
                                popupAwal.click()
                        except:
                            pass
                        try:
                            popup = driver.find_element(
                                By.XPATH,
                                "//span[@class='cds-button-label' and text()='Close']",
                            )
                            if popup:
                                popup.click()
                        except:
                            driver.quit()
                            break

                    try:
                        popup = driver.find_element(
                            By.XPATH, "//span[@class='cds-button-label' and text()='Close']"
                        )
                        if popup:
                            popup.click()
                    except:
                        pass
                break
        except KeyboardInterrupt:
            print("[Proses dihentikan oleh pengguna]")
            driver.quit()
            continue
        
    print("COURSE SUDAH SELESAI DI BOT")
    again = input("Mau Input Course Lgi [y/n]? ")
    if again == "n" or again == "N":
        break
    print("\n")
