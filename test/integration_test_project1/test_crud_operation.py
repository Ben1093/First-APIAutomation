from src.constants.api_constants import API_constants
from src.helpers.api_request_wrapper import post_request, put_request,patch_request,delete_request
from src.helpers.Payload_manager import Payload_create_token, Payload_create_booking, Payload_update_booking
from src.helpers.common_verification import verify_status_code, verify_response_headers
from src.helpers.utilities import common_headers_json, common_headers_put_patch_delete


import pytest

class TestCRUDoperation(object):
    def create_token(self):
        response = post_request(url=API_constants.Create_token(), auth = None, headers= common_headers_json(), payload= Payload_create_token(), in_json= True)
        verify_status_code(response, 200)
        print(response.json())

    def create_booking(self):
        response = post_request(url=API_constants.Create_token(), auth = None, headers= common_headers_json(), payload= Payload_create_booking, in_json= False)
        verify_status_code(response, 200)
        print(response.json())

    def test_update_booking(self, create_token, create_booking):
        bookingId = create_token, create_booking
        response = put_request(url=API_constants.patch_put_delete_booking(bookingId),auth= create_token, headers= common_headers_put_patch_delete(), payload= Payload_update_booking(), in_json= False)
        verify_status_code(response, 200)
        print(response.json())

    def test_delete_booking(self, create_token, create_booking):
        bookingId = create_token, create_booking
        response = delete_request(url=API_constants.patch_put_delete_booking(bookingId),auth= create_token, headers= common_headers_put_patch_delete(), payload= None, in_json= False)
        verify_status_code(response, 200)
        print(response.json())


