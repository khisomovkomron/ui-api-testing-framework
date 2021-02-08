from selenium import webdriver


class WebDriverFactory():
    def __init__(self, browser):
        self.browser = browser

    def getWebDriverInstance(self):
        base_url = "https://letskodeit.teachable.com/"
        if self.browser == "iexplorer":
            driver = webdriver.Ie()
        elif self.browser == "firefox":
            driver = webdriver.Firefox()
        elif self.browser == "chrome":
            driver = webdriver.Chrome("C:/webdrivers/chromedriver.exe")
            driver.set_window_size(1440, 900)
        else:
            driver = webdriver.Chrome("C:/webdrivers/chromedriver.exe")

        driver.implicitly_wait(3)
        driver.maximize_window()
        driver.get(base_url)
        return driver

