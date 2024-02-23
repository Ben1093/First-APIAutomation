import openpyxl
import pytest
import requests
import os

from src.constants.api_constants import  API_constants
from src.helpers.api_request_wrapper import post_request, put_request, patch_request, get_request
from src.helpers.common_verification import verify_status_code, verify_response_headers, verify_response_key_should_not_be_none
from src.helpers.Payload_manager import Payload_create_token, Payload_create_booking, Payload_update_booking
from src.helpers.utilities import common_headers_json, common_headers_put_patch_delete


def test_create_token():
    response = post_request(url= API_constants.Create_token(),auth = None, headers= common_headers_json(), payload= Payload_create_token(USERNAME, ))