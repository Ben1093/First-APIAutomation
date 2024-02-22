def verify_status_code(response_data,expect_data):
    assert response_data.status_code == expect_data, "Expected status code is" + str(expect_data)


def verify_json_key_for_not_null(key):
    assert key != 0, "key is not empty" + key
    assert key > 0, "key is greater than zero"

def verify_response_key_should_not_be_none(key):
    assert key is not None

# def verify_headers(content_type):
#     assert content_type == expected_data, "unexpected content type:" + content_type

def verify_response_headers(actual_content_type, expected_content_type):
    # expected_content_type = "application/json; charset=utf-8"
    actual_content_type = actual_content_type.headers.get("Content-Type")
    assert actual_content_type == expected_content_type, "Unexpected Content-Type: " + str(expected_content_type)
    # assert response_data.data == expected_data, "Unexpected Content-Type: " + expected_data
    # if 'Content-Type' in response_data.headers and response_data.headers['Content-Type']== 'text/html':
    #     print("Content-Type present in header and has the correct value")
    # else:
    #     print("Content-Type not present in header and doesn't have the correct value")



# headers
# data verification
#json schema