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



##### USE THIS CODE SNIPPET TO GET THE TEMPLATE ID FROM YOUR DEVICES, THEN RUN THE SUBSEQUENT CODE TO MAKE TEMPLAES ######
template_url = "dataservice/template/feature?templateType=aaa"

template_response = sess.get(
    url=f"{base_url}{template_url}", verify=False).json()['data']

print(json.dumps(template_response, indent=2))

# create_template_url = "dataservice/template/device/feature"

# payload = {
#     "templateName": "vManage_template",
#     "templateDescription": "vmanage demo",
#     "deviceType": "vmanage",
#     "configType": "template",
#     "factoryDefault": False,
#     "policyId": "",
#     "featureTemplateUidRange": [],
#     "generalTemplates": [
#         {
#             "templateId": "a3dcd195-1eb5-4c97-b862-fdc447be27cf",
#             "templateType": "aaa"
#         },
#         {
#             "templateId": "777f1262-1ae7-4dea-82d1-b24b2132d548",
#             "templateType": "system-vedge"
#         },
#         {
#             "templateId": "bf3fcac8-8ab3-46a3-9ab5-c0d3e6107826",
#             "templateType": "vpn-vsmart"
#         },
#     ]

# }

# headers = {
#     "Accept": "application/json",
#     "Content-Type": "application/json",
# }

# response = sess.post(url=f"{base_url}{create_template_url}", headers=headers).json()
# print(json.dumps(response, indent=2))