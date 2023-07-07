import requests
import json

base_url = "https://dcloud-dna-center-inst-rtp.cisco.com/dna/"
# base_url = "https://sandbox-iosxe-recomm-1.cisco.com"
auth_endpoint = "system/api/v1/auth/token"

# user = 'developer'
# password = 'lastorangerestoreball8876!'
user = 'demo'
password = 'demo1234!'

auth_response = requests.post(
    url=f"{base_url}{auth_endpoint}", auth=(user, password)).json()
token = auth_response['Token']

headers = {
    "x-auth-token": token,
    "Accept": "application/json",
    "Content-Type": "application/json"
}
#################### THIS BLOCK IS USED TO GET THE CLI CERDENTIALS (REMEMBER, THEY ARE SET GLOBALLY IN DNA CENTER) ####################
cred_cli_endpoint = "intent/api/v1/global-credential?credentialSubType=CLI"

cli_response = requests.get(url=f"{base_url}{cred_cli_endpoint}", headers=headers).json()['response'][0]
# print(cli_response)
cli_cred = cli_response['id']

cred_snmp_endpoint = "intent/api/v1/global-credential?credentialSubType=SNMPV2_WRITE_COMMUNITY"


#################### THIS BLOCK IS USED TO GET THE SNMP CERDENTIALS (REMEMBER, THEY ARE SET GLOBALLY IN DNA CENTER) ####################
snmp_response = requests.get(url=f"{base_url}{cred_snmp_endpoint}", headers=headers).json()#['response'][0]
# print(snmp_response)
# snmp_cred = snmp_response['id']

payload ={
    "name": "Micah's device discovery",
    "discoveryType": "Range",
    "ipAddressList": "10.10.20.20-10.10.20.254",
    "timeout":1,
    "protocolOrder":"ssh,telnet",
    "preferredMgmtIpMethod":"None",
    "globalCredentialList": [cli_cred, # snmp_cred
                             ]  
}

discovery_endpoint = "intent/api/v1/discovery"

dicovery_response = requests.post(url=f"{base_url}{discovery_endpoint}", headers=headers, data=json.dumps(payload))
print(dicovery_response)
print(dicovery_response.text)
