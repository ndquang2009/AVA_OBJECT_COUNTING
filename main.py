import requests
from datetime import datetime

def dologin(base_url, username, password):
    url = str(base_url) + "/api/v1/dologin"
    account = {
        "password": password,
        "username": username
    }
    response = requests.post(url, json = account)
    if response.status_code == 200:
        print("OK!")
        return response.cookies
    else
        print("Login failed", response.status_code)
def convert_iso_time():
    current_datetime = datetime.utcnow()
    iso8601_time = current_datetime.isoformat()
    iso8601_time = iso8601_time.split(".")[0] + "Z"
    print(iso8601_time)

def get_countingAreas(base_url, cookies):
    url = str(base_url) + "/api/v1/countingAreas"
    print(url)
    response = requests.get(url, cookies=cookies)
    if response.status_code == 200:
        print("OK!")
        return response.json()
    else:
        print("HTTP error code:", response.status_code)
        return response.status_code

def get_id_name_type_countingAreas(countingAreas):
    countingAreas_list = []
    countingAreas_profile = {
        "countingAreas_id": "",
        "countingAreas_name": "",
        "countingAreas_type": ""
    }
    #print(countingAreas)
    length = len(countingAreas)
    print(length)
    for i in range(0,length):
        countingAreas_profile = {
            "countingAreas_id": countingAreas[i]["id"],
            "countingAreas_name": countingAreas[i]["name"],
            "countingAreas_type": countingAreas[i]["type"]
        }
        #print(countingAreas_profile)
        countingAreas_list.append(countingAreas_profile)
    return countingAreas_list


def get_live_counting(base_url, countingArea_id,cookies):
    url = str(base_url) + "/api/v1/countingAreas/{}/counts".format(countingArea_id)
    current_iso_time = convert_iso_time()
    params = {
        "end": "",
        "start": current_iso_time,
        "step": "",
        "time_location": "Asia/Ho_Chi_Minh"
    }
    response = requests.get(url, params=params, cookies=cookies)
    if response.status_code == 200:
        print("OK!")
        temp = response.json()
        return temp
    else:
        print("HTTP code error:", response.status_code)

