"""
https://stackoverflow.com/questions/72007762/how-do-i-click-and-press-keys-using-selenium
"""
from selenium.webdriver.support.wait import WebDriverWait

if __name__ == "__main__":
    import selenium
    import pandas as pd
    import time
    from selenium import webdriver
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys

    driver = webdriver.Chrome()
    Google_IDS = [
        "https://developers.google.com/maps/documentation/javascript/examples/places-placeid-finder#maps_places_placeid_finder-css"
    ]
    wait = WebDriverWait(driver, 10)
    for Google_ID in Google_IDS:
        driver.get(Google_ID)
        wait.until(EC.frame_to_be_available_and_switch_to_it(
            (By.XPATH, '//*[@id="gc-wrapper"]/main/devsite-content/article/div[2]/div/devsite-iframe/iframe')))
        Google_ID = driver.find_element(By.CSS_SELECTOR, '#pac-input')
        Google_ID.send_keys('Statue of Liberty National Monument')
        wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[3]")))
        Google_ID.send_keys(Keys.DOWN)
        Google_ID.send_keys(Keys.ENTER)
