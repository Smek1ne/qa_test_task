import locators.locators
from pages.base_page import BasePage


class CheckboxPage(BasePage):
    loc = locators.locators.CheckBoxPage

    def should_be_checkbox_url(self):
        assert 'checkbox' in self.browser.current_url, 'No "checkbox" in url'

    def open_home_list(self):
        self.browser.find_element(*self.loc.HOME_BTN_COLLAPSED).click()

    def home_list_should_be_opened(self):
        self.browser.find_element(*self.loc.HOME_BTN_EXPANDED)

    def open_downloads_dir(self):
        self.browser.find_element(*self.loc.DOWNLOADS_TOGGLE).click()

    def downloads_should_be_opened(self):
        self.browser.find_element(*self.loc.DOWNLOADS_OPENED)

    def click_word_file_checkbox(self):
        self.browser.find_element(*self.loc.WORD_FILE_CHECKBOX).click()

    def word_file_selected(self):
        self.browser.find_element(*self.loc.WORD_FILE_CHECKBOX_SELECTED)

    def should_be_message(self, message):
        """result message consists of constant part and variable part - checked checkboxes"""
        result_constant = self.browser.find_element(*self.loc.MESSAGE_CONSTANT_PART).text
        result_variable = self.browser.find_element(*self.loc.MESSAGE_VARIABLE).text
        result = result_constant + result_variable
        assert result == message, f'Wrong message, "{result}" but not "{message}"!'
