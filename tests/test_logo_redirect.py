import allure
import pytest
from conftest import driver
from page_objects.main_page import MainPage


class TestLogoRedirect:
    @allure.title('Проверка перехода на главную страницу сервиса при клике на лого "Самокат" в шапке')
    def test_logo_redirect_to_main_page_success(self, driver):
        main_page = MainPage(driver)
        main_page.wait_visibility_of_order_button_in_header()
        main_page.click_on_order_button_in_header()
        main_page.wait_visibility_of_header_logo_scooter()
        main_page.click_on_header_logo_scooter()
        main_page.wait_visibility_of_main_header()
        assert main_page.check_displaying_of_main_header()

    @allure.title('Проверка перехода на страницу "Дзена" при клике на лого "Яндекс"')
    def test_logo_redirect_to_dzen_success(self, driver):
        main_page = MainPage(driver)
        main_page.wait_visibility_of_header_logo_yandex()
        main_page.click_on_header_logo_yandex()
        main_page.switch_to_next_tab()
        current_url = main_page.check_url()
        main_page.wait_visibility_of_dzen_header()
        assert 'dzen.ru' in main_page.check_dzen(), f"Текущий URL не содержит 'dzen.ru': {current_url}"