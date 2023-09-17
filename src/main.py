from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def init_driver(url):
    options = webdriver.FirefoxOptions()
    options.add_argument('--headless')
    
    driver = webdriver.Firefox(options=options)
    driver.maximize_window()

    try:
        driver.get(url)
    except TimeoutException:
        print("Network Error, Please Try Again")
        driver.quit()
        exit()

    return driver

def main():
    driver = init_driver("https://www.tradingview.com/symbols/TOTAL2/")
    
    try:
        # Wait until the span element is present in the DOM
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'div[data-symbol="CRYPTOCAP:TOTAL2"] div div span'))
        )
        
        # Wait for a couple of seconds to ensure that the dynamic content has loaded
        driver.implicitly_wait(2)

        # Get the text content of the span
        total2_data = element.text
        print(f"The Total2 (Crypto Total Market Cap Exclude BTC, $) is: ${total2_data}")

    except Exception as e:
        print(e)

    driver.quit()


if __name__ == "__main__":
    main()
