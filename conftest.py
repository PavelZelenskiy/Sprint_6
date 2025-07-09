import pytest
from selenium import webdriver

from .urls import*

@pytest.fixture(scope="function")
def driver_func(request):

    driver = webdriver.Firefox()
    driver.maximize_window()
    request.cls.driver = driver
    driver.get(BASE_URL)
    yield driver
    driver.quit()

@pytest.fixture(scope="class")
def driver_cls(request):

    driver = webdriver.Firefox()
    driver.maximize_window()
    request.cls.driver = driver
    driver.get(BASE_URL)
    yield driver
    driver.quit()