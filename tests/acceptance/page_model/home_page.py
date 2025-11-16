from tests.acceptance.locators.home_page import HomePageLocators


class HomePage:
    def __int__(self, driver):
        self.driver = driver

    @property
    def url(self):
        return 'http://127.0.0.1:5000/'

    @property
    def blog_link(self):
        return self.driver.find_element(*HomePageLocators.NAVIGATION_LINK)


class BasePage:
    pass