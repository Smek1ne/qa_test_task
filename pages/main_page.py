from locators.locators import MainPageLoc

from .base_page import BasePage


class MainPage(BasePage):
    loc = MainPageLoc

    def test_go_to_elements_page(self):
        elements = self.browser.find_element(*self.loc.ELEMENTS_FRAME)
        elements.click()
