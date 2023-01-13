import pytest
from selenium import webdriver



@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome('/Users/Roman_Golovin1/Downloads/chromedriver')
    driver.maximize_window()
    yield driver
    driver.quit()
