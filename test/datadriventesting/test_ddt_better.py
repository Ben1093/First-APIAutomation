from dotenv import load_dotenv
import openpyxl
import pytest
import requests
import os

from src.constants.api_constants import  API_constants
from src.helpers.api_request_wrapper import post_request, put_request, patch_request, get_request
from src.helpers.common_verification import verify_status_code, verify_response_headers, verify_response_key_should_not_be_none
from src.helpers.Payload_manager import Payload_create_token, Payload_create_booking, Payload_update_booking
from src.helpers.utilities import common_headers_json, common_headers_put_patch_delete

def read_credentials_from_excel(file_path):
    credentials = []
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active

    for row in sheet.iter_rows(min_row=2, values_only= True):
        username, password = row
        credentials.append({"username": username, "password": password})
    return credentials

# def make_request_auth(username, password):
#     response = post_request(url = API_constants.Create_token(), headers= common_headers_json(), auth = Payload_create_token(), payload= None, in_json=False)
#     verify_status_code(response, 200)
#     return response

def make_request_auth(username, password):
    payload = {
        username: os.getenv("USERNAME"),
        password: os.getenv("PASSWORD")
    }
    response = post_request(url=API_constants.Create_token(), headers=common_headers_json(), payload = payload, auth = None, in_json=False)
    return response


@pytest.mark.parametrize("user_cred", read_credentials_from_excel("Test_case_1.xlsx"))
def test_post_create_token(user_cred):
    username = user_cred["username"]
    password = user_cred["password"]
    print(username, password)
    response = make_request_auth(username, password)
    print(response)
    # here we can change logic for negative and positive
    verify_status_code(response, 200)

