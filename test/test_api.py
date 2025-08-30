import allure
import requests

from config import base_url, Cookie, headers


@allure.feature("API Tests")
@allure.story("Nights Availability Check")
def test_nights():
    with allure.step("Send GET request to fetch nights availability"):
        resp = requests.get(
            base_url + 'api/service-api/f-s/fields/get-nights-by-freight-type?arrivalCountryId=18803&departureCityId=274286&checkinBeg=2025-09-05&checkinEnd=2025-09-05&adult=2&child=0&freightType=0',  headers=headers)

    with allure.step("Check response status code"):
        assert resp.status_code == 200


@allure.feature("API Tests")
@allure.story("Departure Cities Check")

def test_cities():
    with allure.step("Send GET request to fetch cities availability"):
        resp = requests.get(
            base_url + 'api/filters/DepartureCities',  headers=headers)

    with allure.step("Check response status code"):
        assert resp.status_code == 200


@allure.feature("API Tests")
@allure.story("Tours Check")
def test_get_positive_cities():
    with allure.step("Send GET request to fetch tours availability"):
        resp = requests.get(
            base_url + 'api/service-api/f-s/fields/get-arrival?departureCityId=274286&whoRequest=tours',  headers=headers)

    with allure.step("Check response status code"):
        assert resp.status_code == 200


@allure.feature("API Tests")
@allure.story("Status authentication")
def test_auth():
    with allure.step("Send POST request to get authentication"):
        resp = requests.post(
            base_url + 'api/login/auth-status',  headers=headers)

    with allure.step("Check response status code"):
        assert resp.status_code == 200


@allure.feature("API Tests")
@allure.story("Send POST Check Advice Hotel")
def test_get_hotel():
    with allure.step('Send POST request to Check Advice Hotel'):
        resp = requests.post(
            base_url + 'api/service-api/f-s/search/get-for-crm-advice-hotels',  headers=headers)

    with allure.step("Check response status code"):
        assert resp.status_code == 200