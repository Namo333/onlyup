from bs4 import BeautifulSoup
import cloudscraper
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def getDynamicSoup(url, proxy):
    scraper = cloudscraper.create_scraper( 
        interpreter='nodejs', 
        delay=10, 
        browser={ 
            'browser': 'chrome', 
            'platform': 'android', 
            'desktop': False, 
        }, 
    )

    response = scraper.get(url, proxies=proxy)
    print(f"{url} статус: {response.status_code}\n")
    soup = BeautifulSoup(response.text, 'lxml')

    options = webdriver.ChromeOptions()
    options.add_argument('--headless') 
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    time.sleep(5)

    try:
        iframe = driver.find_element(By.ID, "marquiz__frame_64db22a98437040025d353c9")
        driver.switch_to.frame(iframe)

        show_more_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "objects-link")))

        driver.execute_script("arguments[0].scrollIntoView(true);", show_more_button)

        show_more_button.click()
        time.sleep(5)

        soup = BeautifulSoup(driver.page_source, 'html.parser')

    except Exception as e:
        print(f"Ошибка при нажатии на кнопку 'objects-link': {e}")

    driver.quit()

    return soup