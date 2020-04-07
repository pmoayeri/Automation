from Base import InitiateDriver
from Library import ConfigReader

def test_Registration_Invalid_data():
    driver = InitiateDriver.startBrowser()

    driver.close()