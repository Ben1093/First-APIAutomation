from src.constants.api_constants import base_url, API_constants, BASE_URL

def test_constant():
    url = base_url
    print(url)

    constant = API_constants.base_url(22)
    print(constant)

    print(BASE_URL)


