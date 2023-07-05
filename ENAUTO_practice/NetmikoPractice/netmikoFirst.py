from netmiko import ConnectHandler
from pprint import pprint

router = {
    "host": "sandbox-iosxe-recomm-1.cisco.com",
    "port": 22,
    "username": "developer",
    "password": "lastorangerestoreball8876",
    "device_type": "cisco_ios"    
}

try:
    c = ConnectHandler(**router)
    c.enable()
    response = c.send_command("show ip inter bri",use_textfsm=True)
    c.disconnect
except Exception as ex:
    pprint(ex)
else:
    pprint(response)
    