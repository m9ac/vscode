from netmiko import ConnectHandler
from pprint import pprint

router = {
    "host": "sandbox-iosxe-recomm-1.cisco.com",
    "port": 22,
    "username": "developer",
    "password": "lastorangerestoreball8876",
    "device_type": "cisco_ios"    
}

# configs = ['interface loopback101', 'ip address 101.101.101.101 255.255.255.255', 'no shut']
configs = ['no interface loopback101']

try:
    c = ConnectHandler(**router)
    c.enable()
    c.send_config_set(configs)
    # it is also possible to send in a configuration that you've downloaded from one device and saved 
    # to a text file using the following command so long as you point to the text file
    # c.send_config_from_file(pathToConfigTextFileOnYourDevice)
    
    response = c.send_command("show ip inter ",use_textfsm=True)
    c.disconnect
except Exception as ex:
    pprint(ex)
else:
    pprint(response)
    