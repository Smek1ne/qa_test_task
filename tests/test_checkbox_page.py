from pages.main_page import MainPage, BasePage
from pages.elements_page import ElementsPage
from pages.check_box import CheckboxPage


def test_check_box(browser):
    """default browser is chrome, if you want firefox:
    add --browser_name=firefox in request
    example: pytest -v --browser_name=firefox tests\test_checkbox_page.py """
    
    link = 'https://demoqa.com/'
    main_page = MainPage(browser, link)
    main_page.open()
    main_page.test_go_to_elements_page()

    elements_page = ElementsPage(browser, browser.current_url)
    elements_page.should_be_elements_url()
    elements_page.click_checkbox_btn()

    checkbox_page = CheckboxPage(browser, browser.current_url)
    checkbox_page.should_be_checkbox_url()
    checkbox_page.open_home_list()
    checkbox_page.home_list_should_be_opened()
    checkbox_page.open_downloads_dir()
    checkbox_page.downloads_should_be_opened()
    checkbox_page.click_word_file_checkbox()
    checkbox_page.word_file_selected()

    # в ТЗ сообщение написано как "You have selected: wordFile" - нет пробела перед <:>
    # На деле там стоит пробел и нет после, но мы здесь проверяем наличие сообщения и выбранный чекбокс в нем
    checkbox_page.should_be_message("You have selected :wordFile")
