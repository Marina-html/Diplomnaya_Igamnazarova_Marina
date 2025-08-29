import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.feature("Authentication Tests")
@allure.story("User Login")
def test_auth_1():
    with allure.step("Open the website"):
        driver = webdriver.Chrome()
        driver.get("https://fstravel.com/")
        driver.maximize_window()
        driver.implicitly_wait(10)

    with allure.step("Click on the button"):
        second_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '//*[contains(@class, "v-icon-user-14")]'))
        )
        second_button.click()

    with allure.step("Enter username"):
        username_input = WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '#email')))
        username_input.clear()
        username_input.send_keys("dan4@yandex.ru")


    with allure.step("Enter password"):
        password_input = WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '#password'))
        )
        password_input.clear()
        password_input.send_keys("Alina2011")

    with allure.step("Check if the login button is enabled"):
        login_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '//input[contains(@class, "new-button")]'))
        )
        assert login_button.is_enabled()

    with allure.step("Close the browser"):
        driver.quit()


@allure.feature("Authentication Tests")
@allure.story("Invalid User Login")
def test_auth_block():
    with allure.step("Open the website"):
        driver = webdriver.Chrome()
        driver.get("https://fstravel.com/")
        driver.maximize_window()
        driver.implicitly_wait(10)


    with allure.step("Click on the button"):
        second_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '//*[contains(@class, "v-icon-user-14")]'))
        )
        second_button.click()

    with allure.step("Enter invalid email"):
        username_input = WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '#email')))
        username_input.clear()
        username_input.send_keys("dan4@yandex.co")

    with allure.step("Enter password"):
        password_input = WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '#password'))
        )
        password_input.clear()
        password_input.send_keys("Alina2011")

    with allure.step("Click on the login button"):
        login_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '//input[contains(@class, "new-button")]'))
        )
        assert login_button.is_enabled()

    with allure.step("Close the browser"):
        driver.quit()


@allure.feature("Booking Tests")
@allure.story("Minimum Night Count")
def test_min_count():
    with allure.step("Open the website"):
        driver = webdriver.Chrome()
        driver.get("https://fstravel.com/")
        driver.maximize_window()
        driver.implicitly_wait(10)


    with allure.step("Click on the nights field"):
        night_press = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '//div[contains(@class, "nights-field")]'))
        )
        night_press.click()

    with allure.step("Select minimum number of nights(1 night)"):
        night_find = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable(
                (By.XPATH, '//div[contains(@class, "nights-popup__body_cell") and normalize-space(text())="1"]'))
        )
        night_find.click()

    with allure.step("Check if the search button is enabled"):
        enter_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '//button[contains(@class, "v-btn-yellow tour-search__button h-64")]'))
        )
        assert enter_button.is_enabled()

    with allure.step("Close the browser"):
        driver.quit()


@allure.feature("Booking Tests")
@allure.story("Departure City Input")
def test_from_city():
    with allure.step("Open the website"):
        driver = webdriver.Chrome()
        driver.get("https://fstravel.com/")
        driver.maximize_window()
        driver.implicitly_wait(10)


    with allure.step("Wait for and input the departure city"):
        city_input = WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, '//input[contains(@class, "departure-city-field__pinput_input")]'))
        )
        city_input.clear()
        city_input.send_keys("Сочи")

    with allure.step("Check if the search button is enabled"):
        enter_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '//button[contains(@class, "v-btn-yellow tour-search__button h-64")]'))
        )
        assert enter_button.is_enabled()

    with allure.step("Close the browser"):
        driver.quit()

@allure.feature("Booking Tests")
@allure.story("Arrival City Input")
def test_to_city():
    with allure.step("Open the website"):
        driver = webdriver.Chrome()
        driver.get("https://fstravel.com/")
        driver.maximize_window()
        driver.implicitly_wait(10)


    with allure.step("Wait for and input the arrival city"):
        city_input_to = WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, '//input[contains(@class, "arrival-country-field__pinput_input")]'))
        )
        city_input_to.clear()
        city_input_to.send_keys("Китай")

    with allure.step("Check if search button is enabled"):
        enter_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '//button[contains(@class, "v-btn-yellow tour-search__button h-64")]'))
        )
        assert enter_button.is_enabled()

    with allure.step("Close the browser"):
        driver.quit()
