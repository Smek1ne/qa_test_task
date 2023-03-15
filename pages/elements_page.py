from pages.base_page import BasePage
from locators.locators import ElementsPageLoc


class ElementsPage(BasePage):
    loc = ElementsPageLoc

    def should_be_elements_url(self):
        assert 'elements' in self.browser.current_url, 'No "elements" in url'

    def click_checkbox_btn(self):
        self.browser.find_element(*self.loc.CHECK_BOX_BTN).click()
