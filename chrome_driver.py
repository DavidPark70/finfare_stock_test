from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options

class ChromeDriver:
    def __init__(self) -> None:
        # Set up Chrome options
        self.chrome_options = Options()
        self.chrome_options.add_argument('--headless')  # Headless mode
        self.chrome_options.add_argument('--no-sandbox')  # Required in some CI environments
        self.chrome_options.add_argument('--disable-dev-shm-usage')  # Overcomes limited resource problems
        self.chrome_options.add_argument('--window-size=1920,1080')  # Set the window size
        
        self.driver = webdriver.Chrome(options=self.chrome_options)
        
    def get_driver(self) -> WebDriver:
        return self.driver 

    def quit(self):
        self.driver.quit()