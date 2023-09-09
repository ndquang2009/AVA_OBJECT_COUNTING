import requests
from datetime import datetime
import json
# ------------------- Login function --------------------------------------
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
    else:
        print("Login failed", response.status_code)
# ------------------- Get all counting areas information -----------------

# --------------------Print a beautify json string ----------------------
def json_print(json_string):
    pretty_json = json.dumps(json_string, indent=4)
    print(pretty_json)
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
# ------------------ Reformat all counting areas information -------------------
def get_id_name_type_countingAreas(countingAreas):
    countingAreas_list = []
    countingAreas_profile = {
        "countingAreas_id": "",
        "countingAreas_name": "",
        "countingAreas_type": ""
    }
    #print(countingAreas)
    length = len(countingAreas)
    # print(length)
    for i in range(0,length):
        countingAreas_profile = {
            "countingAreas_id": countingAreas[i]["id"],
            "countingAreas_name": countingAreas[i]["name"],
            "countingAreas_type": countingAreas[i]["type"]
        }
        countingAreas_list.append(countingAreas_profile)
    return countingAreas_list

# ------------------ Perform live counting on a specify area -------------------------
def get_live_counting(base_url, countingArea_id, cookies):
    url = str(base_url) + "/api/v1/countingAreas/{}/counts".format(countingArea_id)
    current_datetime = datetime.utcnow()
    current_iso8601_time = current_datetime.isoformat()
    current_iso8601_time = current_iso8601_time.split(".")[0] + "Z"
    params = {
        "end": "",
        "start": current_iso8601_time,
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

# -------------------- Main program -------------------------------------------------------
# -------------------- Declare deployment and account information -------------------------
base_url = "https://msi-apac.au1.aware.avasecurity.com"

# Please input your account here
username = ""
password = ""

# Login to get the authentication cookies
auth_cookies = dologin(base_url,username,password)

# Get all counting areas information
counting_areas_list = get_countingAreas(base_url, auth_cookies)

# Issue new data records with area name - id - type
counting_areas_id = get_id_name_type_countingAreas(counting_areas_list)

#Print the new list
json_print(counting_areas_id)

# Get area id from user input
user_input = input("Please copy the area ID and paste here:")

# Perform live counting
tmp = get_live_counting(base_url, str(user_input), auth_cookies)
print("Current person:", tmp["totals"][0]["countPerson"])








