def Payload_create_booking():
    payload = {
        "firstname":"Josh",
        "lastname":"Allen",
        "totalprice":111,
        "depositpaid":True,
        "bookingdates":
            {"checkin":"2018-01-01",
             "checkout":"2019-01-01"},
        "additionalneeds":"midnight snack"
    }
    return payload

def Payload_update_booking():
    payload = {
        {"firstname":"Parthi",
         "lastname":"ben",
         "totalprice":694,
         "depositpaid":False,
         "bookingdates":{"checkin":"2018-10-20",
                         "checkout":"2023-09-06"},
         "additionalneeds":"Breakfast"}
    }
    return payload

def Payload_create_token():
    payload = {
        "username": "admin",
        "password": "password123"
    }
    return  payload
