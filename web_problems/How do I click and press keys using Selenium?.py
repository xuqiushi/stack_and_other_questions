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

    for Google_ID in Google_IDS:
        driver.get(Google_ID)
        wait = WebDriverWait(driver, 10)
        Google_IDS = [
            'https://developers.google.com/maps/documentation/javascript/examples/places-placeid-finder#maps_places_placeid_finder-css']

        for Google_ID in Google_IDS:
            driver.get(Google_ID)
            wait.until(EC.frame_to_be_available_and_switch_to_it(
                (By.CSS_SELECTOR, "div.devsite-article-body.clearfix > div > devsite-iframe > iframe")))
            Google_ID = driver.find_element(By.CSS_SELECTOR, '#pac-input')
            Google_ID.send_keys('Statue of Liberty National Monument')
            Google_ID.send_keys(Keys.DOWN)
            Google_ID.send_keys(Keys.ENTER)
