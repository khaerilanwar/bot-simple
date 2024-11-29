import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class WebDriverManager(webdriver.Chrome):
    def __init__(self, options: Options = None, service: Service = None, keep_alive: bool = True) -> None:
        if not options:
            options = Options()
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--headless=new")
        super().__init__(options, service, keep_alive)

    def wait_until(self, locator, timeout=10):
        return WebDriverWait(self, timeout).until(
            EC.presence_of_element_located(locator)
        )
    
    def authentication(self, url, email, password):
        self.get(url)
        self.wait_until((By.NAME, 'email')).send_keys(email)
        time.sleep(3)
        self.wait_until((By.NAME, 'pass')).send_keys(password)
        time.sleep(3)
        self.wait_until((By.NAME, 'login')).click()

    def scroll(self, duration=5):
        end_time = time.time() + duration # duration detik
        body = self.find_element(By.TAG_NAME, 'body')
        while time.time() < end_time:
            body.send_keys(Keys.PAGE_DOWN)
            time.sleep(1)