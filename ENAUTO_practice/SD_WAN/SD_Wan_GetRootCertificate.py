import requests
import json
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def login():
    base_url = 'https://10.10.20.90:443/'
    login_action = '/j_security_check'

    # Format data for loginForm
    login_data = {'j_username': 'admin', 'j_password': 'C1sco12345'}

    # URL for posting login data
    login_url = base_url + login_action

    # URL for retrieving client token
    token_url = base_url + 'dataservice/client/token'

    sess = requests.session()

    # If the vmanage has a certificate signed by a trusted authority, change verify to True
    login_response = sess.post(url=login_url, data=login_data, verify=False)
    if b'<html>' in login_response.content:
        print("Login Failed")
        exit(0)

    # Update token to session headers
    login_token = sess.get(url=token_url, verify=False)

    if login_token.status_code == 200:
        if b'<html>' in login_token.content:
            print("Login Token Failed")
            exit(0)

        sess.headers['X-XSRF-TOKEN'] = login_token.content
        return sess

sess = login()  # Call the login function to obtain the session

base_url = 'https://10.10.20.90:443/'  # Move this line outside the login function

cert_endpoint = "dataservice/certificate/vsmart/list"

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
}


root_endpoint = "dataservice/certificate/rootcertificate"

response = sess.get(url=f"{base_url}{root_endpoint}", headers=headers).json()
print(json.dumps(response, indent=2))