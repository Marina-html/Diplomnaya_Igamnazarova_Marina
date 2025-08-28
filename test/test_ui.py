from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def test_auth_1():
    # Переход на сайт
    driver = webdriver.Chrome()
    driver.get("https://fstravel.com/")
    driver.maximize_window()
    driver.implicitly_wait(10)

    # Ожидание и клик по первой кнопке
    #first_button = WebDriverWait(driver, 30).until(
    #   EC.element_to_be_clickable((By.XPATH, '//button[contains(@class, "popmechanic-close")]'))
    #)
    #first_button.click()

    # Ожидание и клик по второй кнопке
    second_button = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, '//*[contains(@class, "v-icon-user-14")]'))
    )
    second_button.click()

    # Ввод имени пользователя
    username_input = WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '#email')))

    username_input.clear()  # Очистка поля перед вводом
    username_input.send_keys("dan4@yandex.ru")


  # Ввод пароля
    password_input = WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '#password'))
    )
    password_input.clear()  # Очистка поля перед вводом
    password_input.send_keys("Alina2011")

    # Ожидание и клик по кнопке входа
    login_button = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, '//input[contains(@class, "new-button")]'))
    )
    assert login_button.is_enabled()


    # Закрытие браузера
    driver.quit()


def test_auth_block():
    # Переход на сайт
    driver = webdriver.Chrome()
    driver.get("https://fstravel.com/")
    driver.maximize_window()
    driver.implicitly_wait(10)

    # Ожидание и клик по первой кнопке
    #first_button = WebDriverWait(driver, 30).until(
    #   EC.element_to_be_clickable((By.XPATH, '//button[contains(@class, "popmechanic-close")]'))
    #)
    #first_button.click()

    # Ожидание и клик по второй кнопке
    second_button = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, '//*[contains(@class, "v-icon-user-14")]'))
    )
    second_button.click()

    # Ввод имени  некорректного email пользователя
    username_input = WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '#email')))

    username_input.clear()  # Очистка поля перед вводом
    username_input.send_keys("dan4@yandex.co")

    # Ввод пароля
    password_input = WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '#password'))
    )
    password_input.clear()  # Очистка поля перед вводом
    password_input.send_keys("Alina2011")

    # Ожидание и клик по кнопке входа
    login_button = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, '//input[contains(@class, "new-button")]'))
    )
    assert login_button.is_enabled()


    # Закрытие браузера
    driver.quit()


def test_min_count():
    # Переход на сайт
    driver = webdriver.Chrome()
    driver.get("https://fstravel.com/")
    driver.maximize_window()
    driver.implicitly_wait(10)

    # Ожидание и клик по первой кнопке
    # first_button = WebDriverWait(driver, 30).until(
    #   EC.element_to_be_clickable((By.XPATH, '//button[contains(@class, "popmechanic-close")]'))
    # )
    # first_button.click()

    # Ожидание и выбор минимального количества суток (1 ночь)
    night_press = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, '//div[contains(@class, "nights-field")]'))
    )
    night_press.click()

    # Ожидание и выбор количества суток (1 ночь)
    night_find = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable(
            (By.XPATH, '//div[contains(@class, "nights-popup__body_cell") and normalize-space(text())="1"]'))
    )
    night_find.click()

    enter_button = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, '//button[contains(@class, "v-btn-yellow tour-search__button h-64")]'))
    )
    assert enter_button.is_enabled()


    # Закрытие браузера
    driver.quit()

def test_from_city():
    # Переход на сайт
    driver = webdriver.Chrome()
    driver.get("https://fstravel.com/")
    driver.maximize_window()
    driver.implicitly_wait(10)

    # Ожидание и клик по первой кнопке
    # first_button = WebDriverWait(driver, 30).until(
    #   EC.element_to_be_clickable((By.XPATH, '//button[contains(@class, "popmechanic-close")]'))
    # )
    # first_button.click()

    # Ожидание и ввод города
    city_input = WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.XPATH, '//input[contains(@class, "departure-city-field__pinput_input")]'))
    )

    city_input.clear()  # Очистка поля перед вводом
    city_input.send_keys("Сочи")

    enter_button = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, '//button[contains(@class, "v-btn-yellow tour-search__button h-64")]'))
    )
    assert enter_button.is_enabled()


    # Закрытие браузера
    driver.quit()

def test_to_city():
    # Переход на сайт
    driver = webdriver.Chrome()
    driver.get("https://fstravel.com/")
    driver.maximize_window()
    driver.implicitly_wait(10)

    # Ожидание и клик по первой кнопке
    # first_button = WebDriverWait(driver, 30).until(
    #   EC.element_to_be_clickable((By.XPATH, '//button[contains(@class, "popmechanic-close")]'))
    # )
    # first_button.click()

    # Ожидание и ввод города
    city_input_to = WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.XPATH, '//input[contains(@class, "arrival-country-field__pinput_input")]'))
    )

    city_input_to.clear()  # Очистка поля перед вводом
    city_input_to.send_keys("Китай")

    enter_button = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, '//button[contains(@class, "v-btn-yellow tour-search__button h-64")]'))
    )
    assert enter_button.is_enabled()

    # Закрытие браузера
    driver.quit()
