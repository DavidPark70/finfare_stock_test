from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

class StockPage():
    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver

    def open_page(self, url: str) -> str:
        self.driver.get(url)
        return self.driver.title

    def get_stock_symbols(self) -> list:
        els = self.driver.find_elements(By.XPATH, "//div[@class='H8Ch1']//div[@class='COaKTb']")
        stock_symbols = []
        for el in els:
            stock_symbols.append(el.text)
        return stock_symbols