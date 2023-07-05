import requests
import json
#this will be used to get the x-auth-token
base_url = "https://dcloud-dna-center-inst-rtp.cisco.com/dna/"
auth_endpouint = "system/api/v1/auth/token"
#change the username and passwords PRN
user = "demo"
password = "demo1234!"
auth_response = requests.post(url=f"{base_url}{auth_endpouint}", auth=(user,password)).json()
#this stores the token response as a variable called token for later use
token = auth_response['Token']

# *** NOTICE THAT THE TOKEN GATHERED IN THE STEP BEFORE IS NOW PASSED AS A VAIRABLE IN THE HEADER ***
headers = {
    "x-auth-token" : token,
    "Accept": "application/json",
    "Content-Type" : "application/json"
}
#uncomment the next line to verify connectivity 
# print(token)


        #this portion of the url will change based on what you are needing to access in DNA Center. Refer to the API documentation
        # you will always see it as "intent/api/v1/XXXXXXXXX"

# sites_endpont = "intent/api/v1/site"

# site_response = requests.get(url=f"{base_url}{sites_endpont}",headers=headers).json()['response']
# print(json.dumps(site_response, indent=2))


topology_endpoint = "intent/api/v1/topology/site-topology"

topology_response = requests.get(url=f"{base_url}{topology_endpoint}",headers=headers).json()['response']
print(json.dumps(topology_response,indent=2))