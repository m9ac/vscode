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

url =f"https://{router['host']}:{router['port']}/restconf/data/ietf-interfaces:interfaces/"

payload = {
    "ietf-interfaces:interface": {
        "name": "Loopback99",
        "description": "holy crap Batman and it works",
        "type": "iana-if-type:softwareLoopback",
        "enabled": True,
        "ietf-ip:ipv4": {
            "address": [
                {
                    "ip": "99.99.99.99",
                    "netmask": "255.255.255.255"
                }
            ]
        }
    }
}



response = requests.post(url=url, headers=headers, auth=(router["user"], router["password"]), data=json.dumps(payload), verify=False)


if response.status_code >= 200:
    print(response.text)
    print(response)
