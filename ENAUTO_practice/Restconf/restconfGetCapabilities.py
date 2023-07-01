import requests
import json

router = {
    "host": "sandbox-iosxe-recomm-1.cisco.com",
    "port": "443",
    "user": "developer",
    "password": "lastorangerestoreball8876"
}

url =f"https://{router['host']}:{router['port']}/restconf/data/netconf-state/capabilities"

headers = {
    "Accept":"application/yang-data+json",
    "Content-Type":"appllication/yang-data+jason"    
}

response = requests.get(url=url, headers=headers, auth=(router["user"], router["password"]), verify=False)

if response.status_code == 200:
    response_dict = response.json()
    for capability in response_dict['ietf-netconf-monitoring:capabilities']['capability']:
        print(capability)