from src.constants.api_constants import API_constants
from src.helpers.api_request_wrapper import post_request, put_request,patch_request,delete_request
from src.helpers.Payload_manager import Payload_create_token, Payload_create_booking, Payload_update_booking, Payload_create_booking_dynamic
from src.helpers.common_verification import verify_status_code, verify_response_headers
from src.helpers.utilities import common_headers_json, common_headers_put_patch_delete


import pytest

def test_create_booking():
    response = post_request(url=API_constants.Create_booking(), auth= None, headers= common_headers_json(), payload= Payload_create_booking_dynamic(), in_json=False)
    verify_status_code(response, 200)
    print(response)
