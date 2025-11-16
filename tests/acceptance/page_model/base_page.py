from tests.acceptance.locators.base_page import BasePageLocators
from tests.acceptance.locators.home_page import HomePageLocators
from tests.acceptance.page_model.home_page import HomePage, BasePage


class Homepage(BasePage):
    @property
    def url(self):
        return super(HomePage,self).url + '/'

    @property
    def title(self):
        return self.driver.find.element(*HomePageLocators.TITLE)