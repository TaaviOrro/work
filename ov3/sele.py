from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Määra veebidraiver (eeldades, et GeckoDriver on PATH-is)
driver = webdriver.Firefox()

try:
    # Ava Google
    driver.get("https://www.google.com")
    time.sleep(2)  # Oota lehe laadimist

    # Leia otsingukast ja sisesta päring
    search_box = driver.find_element(By.NAME, "q")
    search_query = "Selenium WebDriver Python"
    search_box.send_keys(search_query)
    search_box.send_keys(Keys.RETURN)  # Vajutab Enter

    time.sleep(3)  # Oota tulemuste laadimist

    # Klõpsa esimesel tulemuse lingil
    first_result = driver.find_element(By.XPATH, "//h3")
    first_result.click()

    time.sleep(5)  # Jäta leht avatuks paariks sekundiks

finally:
    # Sulge brauser
    driver.quit()
