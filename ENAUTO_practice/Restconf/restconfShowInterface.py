import requests
import json

router = {
    "host": "sandbox-iosxe-recomm-1.cisco.com",
    "port": "443",
    "user": "developer",
    "password": "lastorangerestoreball8876"
}


headers = {
    "Accept":"application/yang-data+json",
    "Content-Type":"appllication/yang-data+jason"    
}


url =f"https://{router['host']}:{router['port']}/restconf/data/Cisco-IOS-XE-interfaces-oper:interfaces/interface=Loopback99"

response = requests.get(url=url, headers=headers, auth=(router["user"], router["password"]), verify=False).json()

print(json.dumps(response, indent=2))

