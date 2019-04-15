import pytest

@pytest.fixture(scope="class")
def test_setup(request):
    from selenium import webdriver
    driver = webdriver.Chrome(executable_path="C:/Users/Ibrahem Taha/PycharmProjects/bookingFramework2/drivers/chromedriver.exe")
    driver.implicitly_wait(15)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
    driver.quit()
    print("Test Comleted")