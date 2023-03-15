from selenium.webdriver.common.by import By


class MainPageLoc:
    ELEMENTS_FRAME = By.XPATH, '//h5[text()="Elements"] //ancestor:: *[contains(@class, "top-card")]'


class ElementsPageLoc:
    CHECK_BOX_BTN = By.XPATH, '//span[.="Check Box"]//parent::li'


class CheckBoxPage:
    HOME_BTN_COLLAPSED = By.XPATH, '//label[@for="tree-node-home"]//ancestor::*[@class="rct-text"]/button'
    HOME_BTN_EXPANDED = By.XPATH, '//span[.="Home"]//ancestor::li[contains(@class, "rct-node-expanded")]'

    DOWNLOADS_TOGGLE = By.XPATH, '//span[text()="Downloads"]//ancestor::span//button'
    DOWNLOADS_OPENED = By.XPATH, '//span[text()="Downloads"]//ancestor::span//button' \
                                 '//*[contains(@class, "rct-icon-expand-open")]'
    WORD_FILE_CHECKBOX = By.XPATH, '//span[text()="Word File.doc"]//parent::*/span[@class="rct-checkbox"]'
    WORD_FILE_CHECKBOX_SELECTED = By.XPATH, \
        '//span[text()="Word File.doc"]//parent::label//*[@class="rct-icon rct-icon-check"]'

    MESSAGE_CONSTANT_PART = By.XPATH, '//div[@id="result"]//span[.="You have selected :"]'
    MESSAGE_VARIABLE = By.XPATH, '//div[@id="result"]/span[@class="text-success"]'
