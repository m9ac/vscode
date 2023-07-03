import requests
import json
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

router = {
    "host": "sandbox-iosxe-recomm-1.cisco.com",
    "port": "443",
    "user": "developer",
    "password": "lastorangerestoreball8876"
}


headers = {
    "Accept": "application/yang-data+json",
    "Content-Type": "application/yang-data+json"
}

url =f"https://{router['host']}:{router['port']}/restconf/data/ietf-interfaces:interfaces/interface=Loopback99"




response = requests.delete(url=url, headers=headers, auth=(router['user'], router['password']),  verify=False)

if response.status_code >= 200:
    print(response)
    # print(response.text)
# print(response)