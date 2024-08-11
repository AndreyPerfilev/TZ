import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()
