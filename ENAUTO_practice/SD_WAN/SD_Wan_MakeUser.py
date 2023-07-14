import requests
import json
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

protocol = "https"
ip_address = "10.10.20.90"
port = 443
base_url = f"{protocol}://{ip_address}:{port}/"

headers = {
    "Accept" : "application/json",
    "Content-Type" : "application/json",
}

def login():
    
    login_action = "/j_security_check"

    # Format data for loginForm
    login_data = {
        "j_username" : "admin",
        "j_password" : "C1sco12345"
        }

    # URL for retrieving client token
    token_endpoint = "dataservice/client/token"
    token_url = f"{base_url}{token_endpoint}"

    sess = requests.session()

    # If the vmanage has a certificate signed by a trusted authority, change verify to True
    login_response = sess.post(url=f"{base_url}{login_action}", data=login_data, verify=False)
    if b"<html>" in login_response.content:
        print("Login Failed")
        exit(0)

    # Update token to session headers
    login_token = sess.get(url=token_url, verify=False)

    if login_token.status_code == 200:
        if b"<html>" in login_token.content:
            print("Login Token Failed")
            exit(0)

        sess.headers["X-XSRF-TOKEN"] = login_token.content
        return sess

sess = login()  # Call the login function to obtain the session

payload = {
    "group": ["netadmin"],
    "description": "The Bigger FATTER Boss woman",
    "userName": "knox",
    "password": "password"
}

payload_update = {
    "userName": "knox",
    "password": "fnefAA!334"
}

pw_endpoint = "dataservice/admin/user/password/knox"

# response = sess.post(url=f"{base_url}{pw_endpoint}", headers=headers, data=json.dumps(payload), verify=False).json()
# response = sess.get(url=f"{base_url}{pw_endpoint}", headers=headers, verify=False).json()["data"]
# response = sess.delete(url=f"{base_url}{pw_endpoint}", headers=headers, verify=False).json()
response = sess.put(url=f"{base_url}{pw_endpoint}", data=json.dumps(payload_update), headers=headers, verify=False)

print(response)
# print(json.dumps(response,indent=2))
