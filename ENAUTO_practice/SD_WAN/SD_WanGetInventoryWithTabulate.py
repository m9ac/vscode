import requests
import json
import urllib3
from tabulate import tabulate

urllib3.disable_warnings()

base_url = "https://sandbox-sdwan-2.cisco.com:443/"
auth_endpoint = "j_security_check"

login_body = {
    "j_username": "devnetuser",
    "j_password": "RG!_Yw919_83" 
}

sesh = requests.session()
login_response = sesh.post(
    url=f"{base_url}{auth_endpoint}", data=login_body, verify=False)

if not login_response.ok or login_response.text:
    print('login failed')
    import sys
    sys.exit(1)
else:
    print('login succeeded')
    
# teplate_url = "dataservice/template/device"

# template_response =sesh.get(url=f"{base_url}{teplate_url}",verify=False).json()
# print(json.dumps(template_response,indent=2))


# get device inventory

device_endpoint = "dataservice/device"

device_response = sesh.get(
    url=f"{base_url}{device_endpoint}", verify=False).json()

print(json.dumps(device_response,indent=2))

headers = ['System IP','Hostmane','Reachability','Device Type','Site ID', 'Device State']

table = list()
for data in device_response ['data']:
    table_row = data['system-ip'], data['host-name'], data['reachability'], data['device-type'], data['site-id'], data['state']
    table.append(table_row)

print(tabulate(table,headers, tablefmt='fancy.grid'))