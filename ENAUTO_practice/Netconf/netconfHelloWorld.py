from ncclient import manager

router = {
    "host":"sandbox-iosxe-recomm-1.cisco.com",
    "port":"830",
    "username":"developer",
    "password": "lastorangerestoreball8876",
}


with manager.connect(**router, hostkey_verify=False) as m:
    for capability in m.server_capabilities:
        print('*'*25)
        print(' ')
        print(capability)