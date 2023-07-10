import requests
import json

base_url = "https://sandbox-sdwan-2.cisco.com:443/"
auth_endpoint = "j_security_check"

login_body = {
    "j_username": "devnetuser",
    "j_password": "RG!_Yw919_83"    
}

sesh = requests.session()
login_response = sesh.post(
    url=f"{base_url}{auth_endpoint}", data=login_body, verify=False)

#print(login_response.text)

if login_response.status_code != 200 or "Invalid credentials" in login_response.text:
    print("Login failed.")
    exit(1)
else:
    print("Login succeeded.")

# if not login_response.ok or login_response.text:
#     print('login failed')
#     import sys
#     sys.exit(1)
# else:
#     print('login succeeded')