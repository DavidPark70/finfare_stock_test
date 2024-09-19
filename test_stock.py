import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options
from stock_page import StockPage

TEST_DATA = ["NFLX", "MSFT", "TSLA"]

@pytest.fixture(scope='module')
def driver():
    print('start driver')

     # Set up Chrome options
    chrome_options = Options()
    chrome_options.add_argument('--headless')  # Headless mode
    chrome_options.add_argument('--no-sandbox')  # Required in some CI environments
    chrome_options.add_argument('--disable-dev-shm-usage')  # Overcomes limited resource problems
    chrome_options.add_argument('--window-size=1920,1080')  # Set the window size

    # Initialize WebDriver with options
    driver = webdriver.Chrome(options=chrome_options)
    yield driver

    print('close driver')
    driver.quit()

def test_problem1(driver: WebDriver):
    page_object = StockPage(driver)

    assert page_object.open_page('https://www.google.com/finance/') != None, 'failed to find page title after opening'

    stock_symbols = page_object.get_stock_symbols()
    assert stock_symbols != [] or stock_symbols != None, 'failed to retrive stock symbols'
    
    stock_symbols_set = set(stock_symbols)
    for stock in stock_symbols_set:
        if stock not in TEST_DATA:
            print(f'retrieved stock \"{stock}\" not in test data')
    
    for stock in TEST_DATA:
        if stock not in stock_symbols_set:
            print(f'test data \"{stock}\" not in retrieved data')
