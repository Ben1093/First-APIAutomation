def common_headers_json():
    headers = {
        "Content-Type": "application/json",
    }
    return headers

def common_headers_xml():
    headers = {
        "Content-Type": "application/xml",
    }
    return headers

def common_headers_put_patch_delete():
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Basic YWRtaW46cGFzc3dvcmQxMjM=",

    }
    return headers

# keep the common functions in future
# read data from excel, csv, json, yaml