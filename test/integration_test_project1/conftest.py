from src.helpers.api_request_wrapper import post_request
from src.constants.api_constants import API_constants
from src.helpers.utilities import common_headers_json, common_headers_put_patch_delete
from src.helpers.Payload_manager import Payload_create_booking, Payload_create_token
from src.helpers.common_verification import verify_response_key_should_not_be_none, verify_status_code,verify_response_headers



import pytest

class Testcreatebooking(object):
    def test_create_token(self):
       response = post_request(url=API_constants.Create_token(), auth=None, headers=common_headers_json(), payload=Payload_create_token(), in_json=False)
       verify_response_key_should_not_be_none(response.json()["token"])
       Token = response.json()["token"]
       print(Token)
       verify_status_code(response, 200)
       return Token


    def test_create_booking_tc1(self):
        #url, header, payload, auth
        response = post_request(url= API_constants.Create_booking(), auth= None, headers= common_headers_json(), payload= Payload_create_booking(), in_json= False)
        verify_response_key_should_not_be_none(response.json()["bookingid"])
        booking_id = response.json()["bookingid"]
        print(booking_id)
        verify_status_code(response,200)
        verify_response_headers(response, "application/json; charset=utf-8")
        return booking_id

    def test_create_booking_tc2(self):
        response = post_request(url= API_constants.Create_booking(), auth = None, headers= common_headers_json(), payload= {}, in_json= False)
        print(response)
        verify_status_code(response,500)


